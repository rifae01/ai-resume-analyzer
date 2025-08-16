
import streamlit as st
import json
from src.extract_text import extract_text
from src.analyze_resume import load_keywords, analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧠", layout="centered")

st.title("🧠 AI Resume Analyzer")
st.write("Upload your resume and pick a target role to see a skill match score, missing keywords, and improvement tips.")

# Load role keywords
with open("data/job_keywords.json", "r", encoding="utf-8") as f:
    role_keywords = json.load(f)

with st.sidebar:
    st.header("⚙️ Settings")
    role = st.selectbox("Target Role", list(role_keywords.keys()))
    st.info("Tip: Choose the role you're applying for to get the right keyword match.", icon="💡")

uploaded = st.file_uploader("Upload Resume (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

if uploaded is not None:
    file_bytes = uploaded.read()
    try:
        resume_text, ext = extract_text(file_bytes, uploaded.name)
    except Exception as e:
        st.error(f"Could not read file: {e}")
        st.stop()

    st.success(f"Successfully extracted text from **.{ext}** file.")
    with st.expander("🔎 Preview extracted text"):
        st.write(resume_text[:2000] + ("..." if len(resume_text) > 2000 else ""))

    if st.button("Analyze Resume", type="primary"):
        result = analyze_resume(resume_text, role, role_keywords)

        st.subheader("📊 Match Score")
        st.metric(label="Overall Match", value=f"{result['match']}%")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**✅ Keywords Found**")
            if result["found"]:
                st.write(", ".join(sorted(set(result["found"]))))
            else:
                st.write("_None detected_")
        with col2:
            st.markdown("**❌ Missing Keywords**")
            if result["missing"]:
                st.write(", ".join(sorted(set(result["missing"]))))
            else:
                st.write("_Great! No obvious gaps for this role._")

        st.subheader("🛠️ Recommendations")
        for tip in result["suggestions"]:
            st.write(f"- {tip}")

        st.caption("Note: This is a simple keyword-based analyzer intended for quick feedback. Always tailor your resume manually for best results.")
else:
    st.info("Upload a resume to begin.", icon="📄")
