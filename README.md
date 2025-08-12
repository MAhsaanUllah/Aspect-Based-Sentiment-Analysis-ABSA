# 🍽️ Amazon Fine Food Reviews — Aspect-Based Sentiment Analysis (ABSA)

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-app-orange.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 📌 Overview  
This project performs **Aspect-Based Sentiment Analysis (ABSA)** on the **Amazon Fine Food Reviews Dataset**.  
It extracts **aspects** (e.g., "taste", "delivery", "price") from customer reviews and assigns **sentiment polarity** (*Positive, Negative, Neutral*) to each aspect.

---

## 📂 Folder Structure

Aspect-Based-Sentiment-Analysis-ABSA/
│── Amazon_Fine_Food_Analysis.ipynb # Main notebook (Phases 1–6)
│── app.py # Streamlit app for interactive ABSA
│── requirements.txt # Dependencies list
│── sample_reviews.csv # Demo dataset
│── screenshots/ # App screenshots
│ └── demo_screenshot.png
└── README.md # Documentation


---

## 📸 Demo  
![ABSA App Screenshot](screenshots/demo_screenshot.png)

---

## 🚀 How to Run (Google Colab)  
1. **Open the notebook in Google Colab**  
2. Add your **NGROK token** to Colab Secrets (`NGROK_AUTH_TOKEN`).  
3. Run the notebook cells in order (Phases 1–6).  
4. For the **Streamlit App**:  
   - Run Phase 6 cells.  
   - Click the ngrok URL to access the app.  

---

## 📊 Features  
✅ Text preprocessing (lowercasing, punctuation & stopword removal)  
✅ Aspect extraction using **spaCy** + **KeyBERT**  
✅ Aspect-level sentiment classification  
✅ Visualizations (bar charts, word clouds)  
✅ Runs directly in **Google Colab** with **ngrok** for public access  

---

## 📈 Evaluation (Optional for Labeled Data)  
- **Aspect Extraction** → Precision / Recall / F1-score  
- **Sentiment Classification** → Accuracy, Macro F1, Confusion Matrix  
- **Learning Curves** → Detect overfitting / underfitting  

---

## 🔮 Future Improvements  
- Multi-language support 🌍  
- Fine-tuned transformer models 🤖  
- Timeline-based sentiment trends 📅  
- Permanent deployment on **Streamlit Cloud** / **HuggingFace Spaces**  

---

## 📜 License  
This project is licensed under the **MIT License** — feel free to use and modify.


