# 🍽️ Amazon Fine Food Reviews — Aspect-Based Sentiment Analysis (ABSA)

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-app-orange.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 📌 Overview  
This project applies **Aspect-Based Sentiment Analysis (ABSA)** on the **Amazon Fine Food Reviews Dataset**.  
It extracts **specific aspects** from reviews (e.g., *taste, delivery, price*) and assigns **sentiment polarity** (*Positive, Negative, Neutral*) to each aspect.  

🔑 Core stack: **spaCy**, **KeyBERT**, **Streamlit**, and **ngrok (for Colab deployment)**.  

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
1. Open the notebook in **Google Colab**.  
2. Add your **NGROK token** to Colab Secrets (`NGROK_AUTH_TOKEN`).  
3. Run all notebook cells sequentially (Phases 1–6).  
4. For the **Streamlit App**:  
   - Execute Phase 6.  
   - Click the generated ngrok URL to open the live app.  

---

## 📊 Features  
- ✅ **Text Preprocessing** → Lowercasing, punctuation & stopword removal.  
- ✅ **Aspect Extraction** → Using **spaCy** + **KeyBERT**.  
- ✅ **Aspect-Level Sentiment** → Assigns polarity per aspect.  
- ✅ **Visualizations** → Bar charts & word clouds for interpretability.  
- ✅ **One-Click Deployment** → Run directly in Colab with ngrok public URL.  

---

## 📈 Evaluation (Optional for Labeled Data)  
- **Aspect Extraction** → Precision / Recall / F1-score.  
- **Sentiment Classification** → Accuracy, Macro-F1, Confusion Matrix.  
- **Learning Curves** → Detect overfitting / underfitting patterns.  

---

## 🔮 Future Improvements  
- 🌍 Multi-language support for non-English datasets.  
- 🤖 Fine-tuned transformer-based ABSA models.  
- 📅 Timeline-based sentiment tracking.  
- ☁️ Permanent deployment on **Streamlit Cloud** or **HuggingFace Spaces**.  

---

## 📜 License  
This project is licensed under the **MIT License** — free to use, modify, and share.  

---

## ✨ Recruiter Note  
This project demonstrates:  
- **Advanced NLP Techniques** → Aspect extraction + sentiment classification.  
- **Practical Application** → Turns raw reviews into actionable insights for businesses.  
- **Deployment Skills** → End-to-end pipeline with Colab + Streamlit app.  

🔗 Highly relevant for roles in **NLP Engineering, Data Science, and Machine Learning**.  



