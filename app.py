import streamlit as st
from src.resume_parser import extract_text_from_pdf
from src.text_preprocessing import clean_text
from src.skill_extractor import extract_skills
from src.matcher import calculate_similarity

st.set_page_config(page_title="AI Resume Scanner", layout="centered")

st.title("📄 AI Resume Scanner & Job Matcher")

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if uploaded_resume and job_description:
    resume_text = extract_text_from_pdf(uploaded_resume)
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_description)

    resume_skills = extract_skills(resume_clean)
    job_skills = extract_skills(job_clean)

    match_score = calculate_similarity(resume_clean, job_clean)

    st.subheader("✅ Results")

    st.write(f"### 🔥 Match Score: **{match_score}%**")

    st.write("### 🧠 Matched Skills")
    st.write(set(resume_skills).intersection(set(job_skills)))

    st.write("### ❌ Missing Skills")
    st.write(set(job_skills) - set(resume_skills))
