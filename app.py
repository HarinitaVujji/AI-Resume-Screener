import streamlit as st
import pandas as pd

from utils.preprocessing import clean_text
from utils.pdf_reader import extract_text_from_pdf
from utils.matcher import match_resumes

st.title("AI-Powered Resume Screener")

# ---------- Resume Input ----------
st.subheader("Upload Resumes")

resume_type = st.radio("Resume Input Type", ["CSV File", "Multiple PDF Files"])

resumes = []

if resume_type == "CSV File":
    uploaded_csv = st.file_uploader("Upload resumes.csv", type=["csv"])
    if uploaded_csv:
        df = pd.read_csv(uploaded_csv)

        st.subheader("Preview of Uploaded Data")
        st.dataframe(df.head())

        st.subheader("Select Resume Text Column")
        column_name = st.selectbox("Choose the column that contains resume text:", df.columns)

        resumes = df[column_name].astype(str).tolist()
        st.success(f"{len(resumes)} resumes loaded from column: {column_name}")


elif resume_type == "Multiple PDF Files":
    uploaded_pdfs = st.file_uploader("Upload multiple PDF resumes", type=["pdf"], accept_multiple_files=True)
    if uploaded_pdfs:
        for pdf in uploaded_pdfs:
            text = extract_text_from_pdf(pdf)
            resumes.append(text)
        st.success(f"{len(resumes)} PDF resumes loaded.")

# ---------- Job Description ----------
st.subheader("Provide Job Description")

jd_type = st.radio("Job Description Input Type", ["Text", "Upload File"])
job_desc = ""

if jd_type == "Text":
    job_desc = st.text_area("Enter Job Description")

elif jd_type == "Upload File":
    jd_file = st.file_uploader("Upload Job Description File (txt/pdf)", type=["txt", "pdf"])
    if jd_file:
        if jd_file.name.endswith(".txt"):
            job_desc = jd_file.read().decode("utf-8")
        elif jd_file.name.endswith(".pdf"):
            job_desc = extract_text_from_pdf(jd_file)

# ---------- Matching ----------
if st.button("Match Resumes"):
    if len(resumes) == 0:
        st.warning("Please upload resumes first.")
    elif job_desc.strip() == "":
        st.warning("Please provide a job description.")
    else:
        clean_resumes = [clean_text(r) for r in resumes]
        clean_jd = clean_text(job_desc)

        scores = match_resumes(clean_resumes, clean_jd)

        results = pd.DataFrame({
            "Resume_ID": range(1, len(resumes) + 1),
            "Match Score": scores
        }).sort_values(by="Match Score", ascending=False)

        st.subheader("Top Matching Resumes")
        st.dataframe(results.head(10))

        st.download_button(
            "Download Results as CSV",
            results.to_csv(index=False),
            file_name="shortlisted_resumes.csv",
            mime="text/csv"
        )
