
# 🧠 AI Resume Analyzer

A small, internship-ready project: upload a resume (PDF / DOCX / TXT), pick a target role, and get:

- 📊 A keyword-based match score
- ✅ Keywords found
- ❌ Missing keywords to add
- 🛠️ Practical improvement tips

Built with **Python + Streamlit**. No heavy ML downloads required.

---

## ✨ Features
- Supports **PDF**, **DOCX**, and **TXT**
- Target roles included: Data Scientist, AI/ML Engineer, Web Developer, Android Developer, Data Analyst, DevOps Engineer, UI/UX Designer
- Clean UI with expandable text preview
- Fast, offline-friendly keyword matching

---

## 🗂️ Project Structure
```text
ai-resume-analyzer/
├─ app.py
├─ requirements.txt
├─ .gitignore
├─ data/
│  └─ job_keywords.json
└─ src/
   ├─ extract_text.py
  └─ analyze_resume.py
```

---

## 🚀 Run Locally

**Prereqs:** Python 3.9+

```bash
# 1) Clone the repo
git clone https://github.com/<your-username>/ai-resume-analyzer.git
cd ai-resume-analyzer

# 2) Create & activate a virtual env (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Run the app
streamlit run app.py
```

Streamlit will open a local URL (something like http://localhost:8501). Upload your resume and analyze.

---

## ☁️ Deploy (Free)

### Option A: Streamlit Community Cloud
1. Push this repo to GitHub.
2. Go to **share.streamlit.io** (or Streamlit Community Cloud) and click **New app**.
3. Connect your GitHub, pick this repo, set **Main file path** to `app.py`.
4. Click **Deploy**. Done!

### Option B: Hugging Face Spaces (Gradio or Streamlit)
1. Create a new Space → choose **Streamlit**.
2. Upload these project files.
3. App boots automatically.

---

## 🧰 Customize
- Edit `data/job_keywords.json` to add roles or change keywords.
- In `src/analyze_resume.py`, adjust scoring or add your own rules.
- Add a **Projects** or **Contact extraction** feature if you want extra credit.

---

## 🔒 Notes
- This is a keyword-based analyzer. It’s great for quick feedback but not a replacement for human review.
- Do not paste sensitive personal data into public issues or PRs.

---

## 🛡️ License
MIT
