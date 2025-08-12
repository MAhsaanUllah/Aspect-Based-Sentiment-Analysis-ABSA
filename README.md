# 🚀 Amazon Fine Food Reviews — Aspect-Based Sentiment Analysis (ABSA)

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-orange?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 📌 Overview
This project performs **Aspect-Based Sentiment Analysis (ABSA)** on Amazon Fine Food Reviews.  
It **extracts aspects** (product features) from reviews and determines sentiment *(Positive, Negative, Neutral)* for each aspect,  
with interactive visualizations.

---

## 📂 Folder Structure

project/
│
├── Amazon_Fine_Food_Analysis.ipynb # Main notebook (Phases 1–6)
├── app.py # Streamlit app for ABSA
├── requirements.txt # Dependencies
├── sample_reviews.csv # Demo dataset
│
├── screenshots/ # UI previews
│ └── demo_screenshot.png
└── README.md # Documentation




---

## 📸 Demo
![ABSA App Screenshot](screenshots/demo_screenshot.png)

---

## 🚀 How to Run (Google Colab)
1. **Upload** the notebook to Colab.
2. Add your **NGROK_AUTH_TOKEN** to Colab Secrets.
3. Run the cells in order *(Phases 1–6)*.
4. **For Streamlit App**:
   - Run Phase 6 cells.
   - Click the **ngrok public link** to open the app.

---

## ✨ Features
- 🧹 **Preprocessing** — lowercase, punctuation & stopword removal
- 📌 **Aspect Extraction** — spaCy + KeyBERT
- 💬 **Aspect-Level Sentiment** — Positive / Negative / Neutral
- 📊 **Visualizations** — Bar charts, pie charts, word clouds
- ☁ **Colab + ngrok** — Easy public deployment

---

## 📈 Evaluation (Optional for Labeled Data)
- **Aspect Extraction** — Precision / Recall / F1
- **Sentiment Classification** — Accuracy, Macro F1, Confusion Matrix
- **Learning Curves** — Detect overfitting / underfitting

---

## 🔮 Future Improvements
- 🌎 Multi-language support
- 🤖 Transformer-based fine-tuning
- ⏳ Timeline-based sentiment trends
- ☁ Permanent deployment (Streamlit Cloud / HuggingFace Spaces)

---

## 📜 License
This project is licensed under the **MIT License**.

