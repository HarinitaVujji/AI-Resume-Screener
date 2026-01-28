# 🚀 AI-Resume-Screener

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

An **AI-powered Resume Screening system** that automatically analyzes and ranks resumes based on a given job description using **Natural Language Processing (NLP)** techniques.

---

## ✨ Features
- Upload resumes in **CSV** or **multiple PDF files**
- Upload job description as **text or file**
- Automatically adapts to **any CSV schema**
- TF-IDF based feature extraction
- Cosine similarity for resume-job matching
- Ranks resumes by relevance score
- Download shortlisted resumes as CSV
- Interactive **Streamlit** web interface

---

## 🧠 Tech Stack
- Python  
- NLP (NLTK)  
- Scikit-learn  
- Pandas  
- Streamlit  
- PDFPlumber / PyMuPDF  

---

## 📂 Project Structure
```
AI-Resume-Screener/
│
├── app.py
├── requirements.txt
├── utils/
│ ├── preprocessing.py
│ ├── matcher.py
│ └── pdf_reader.py
├── data/
└── README.md
```

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/HarinitaVujji/AI-Resume-Screener.git
cd AI-Resume-Screener

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
