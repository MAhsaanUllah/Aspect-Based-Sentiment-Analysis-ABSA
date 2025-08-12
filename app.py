# 📄 Advanced Streamlit App with Single & Multi-Aspect Sentiment Analysis

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import spacy
from keybert import KeyBERT
from textblob import TextBlob
import re

# Load NLP model and keyword extractor
@st.cache_resource
def load_models():
    nlp = spacy.load("en_core_web_sm")
    kw_model = KeyBERT()
    return nlp, kw_model

nlp, kw_model = load_models()

# Streamlit page settings
st.set_page_config(page_title="Amazon Review Analyzer", layout="wide")

st.title("🚀 Amazon Fine Food Reviews – Aspect-Based Sentiment Analysis")
st.markdown("""
Analyze reviews with **single** and **multi-aspect** sentiment detection,  
keyword extraction, and interactive visual insights.
""")

# Sidebar - file upload
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV with 'Text' column", type=['csv'])

# Load data
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    st.info("No file uploaded. Using sample data...")
    df = pd.DataFrame({
        "Text": [
            "The pasta was amazing and fresh! The service was quick.",
            "Terrible service and the food was cold.",
            "Loved the dessert, will come again.",
            "The coffee tasted burnt but the cake was delicious.",
            "Great ambiance and friendly staff."
        ]
    })

if "Text" not in df.columns:
    st.error("Uploaded file must contain a 'Text' column.")
    st.stop()

# Sentiment classification
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Aspect splitting
def split_aspects(text):
    return [sent.strip() for sent in re.split(r'[.!?]', text) if sent.strip()]

# Processing
aspect_data = []
overall_sentiments = []

for review in df["Text"]:
    aspects = split_aspects(review)
    aspect_sentiments = [(a, get_sentiment(a)) for a in aspects]
    aspect_data.extend([(review, a, s) for a, s in aspect_sentiments])

    overall_polarity = sum(TextBlob(a).sentiment.polarity for a in aspects) / len(aspects)
    if overall_polarity > 0:
        overall_sentiments.append("Positive")
    elif overall_polarity < 0:
        overall_sentiments.append("Negative")
    else:
        overall_sentiments.append("Neutral")

df["Overall Sentiment"] = overall_sentiments
aspect_df = pd.DataFrame(aspect_data, columns=["Review", "Aspect", "Aspect Sentiment"])

# Keyword extraction
def extract_keywords(text):
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2),
                                         stop_words="english", top_n=3)
    return ", ".join([kw[0] for kw in keywords])

df["Keywords"] = df["Text"].apply(extract_keywords)

# Layout: Sentiment Distribution + Word Cloud
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Overall Sentiment Distribution")
    sentiment_counts = df["Overall Sentiment"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(sentiment_counts, labels=sentiment_counts.index,
           autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

with col2:
    st.subheader("☁️ Keyword Word Cloud")
    all_keywords = " ".join(df["Keywords"])
    wc = WordCloud(width=800, height=400, background_color="white").generate(all_keywords)
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

# Sentiment trend chart
st.subheader("📈 Sentiment Trend (by Review Index)")
df["SentimentScore"] = df["Overall Sentiment"].map({"Positive": 1, "Neutral": 0, "Negative": -1})
st.line_chart(df["SentimentScore"])

# Data tables
st.subheader("📝 Processed Reviews (Overall)")
st.dataframe(df)

st.subheader("🔍 Aspect-Level Sentiment")
st.dataframe(aspect_df)

st.success("✅ Analysis Complete – Single & Multi-Aspect handled successfully!")
