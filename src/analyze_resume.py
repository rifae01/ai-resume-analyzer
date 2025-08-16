
import json
import math
import re
from typing import Dict, List, Tuple

def load_keywords(path: str) -> Dict[str, List[str]]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def normalize(text: str) -> str:
    # Lowercase, remove punctuation except +/#/.
    text = text.lower()
    text = re.sub(r"[^a-z0-9\+\/#\.\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def keyword_presence(resume_text: str, keywords: List[str]) -> Tuple[List[str], List[str]]:
    norm = normalize(resume_text)
    found, missing = [], []
    for kw in keywords:
        # Build a case-insensitive search that handles terms with special chars (e.g., "C++", "Node.js")
        pattern = re.escape(kw.lower())
        # Match whole word if alnum-only; else fallback to substring (for C++, Node.js, etc.)
        if re.match(r"^[a-z0-9 ]+$", kw.lower()):
            # word-boundary match for simple words/phrases
            exists = re.search(rf"(?<![a-z0-9]){pattern}(?![a-z0-9])", norm) is not None
        else:
            exists = pattern in norm
        (found if exists else missing).append(kw)
    return found, missing

def score(found: List[str], total: int) -> int:
    if total == 0:
        return 0
    return int(round((len(found) / total) * 100))

def quick_suggestions(found: List[str], missing: List[str], role: str) -> List[str]:
    tips = []
    if missing:
        tips.append(
    f"Consider integrating these {role} keywords naturally: "
    + ", ".join(missing[:8])
    + ("..." if len(missing) > 8 else ""))

    if len(found) < len(missing):
        tips.append("Add 2–3 bullet points per experience with measurable outcomes (e.g., 'improved accuracy by 7%').")
    if role.lower() in {"data scientist","data analyst","ai/ml engineer"}:
        tips.append("Include links to notebooks, demos, or repos that showcase models, EDA, or MLOps pipelines.")
    if role.lower() in {"web developer","android developer","devops engineer","ui/ux designer"}:
        tips.append("Add a Projects section with live links (GitHub Pages, Play Store, or deployed apps).")
    tips.append("Use active verbs: built, designed, optimized, automated, deployed, led.")
    tips.append("Keep resume to 1 page (fresher) or 2 pages (experienced), with clean, consistent formatting.")
    return tips

def analyze_resume(resume_text: str, role: str, keywords_dict: Dict[str, List[str]]):
    if role not in keywords_dict:
        raise ValueError("Unknown role selected.")
    role_keywords = keywords_dict[role]
    found, missing = keyword_presence(resume_text, role_keywords)
    match = score(found, len(role_keywords))
    suggestions = quick_suggestions(found, missing, role)
    return {
        "role": role,
        "match": match,
        "found": found,
        "missing": missing,
        "suggestions": suggestions,
    }
