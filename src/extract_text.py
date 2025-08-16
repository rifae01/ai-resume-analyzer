
import io
import re
from typing import Tuple

# PDF
from pdfminer.high_level import extract_text as pdf_extract_text
# DOCX
from docx import Document

def _clean_text(text: str) -> str:
    # Normalize whitespace and lower-case for analysis (keep original for display elsewhere if needed)
    text = text.replace("\x00", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_text_from_pdf(file_bytes: bytes) -> str:
    # pdfminer works with file paths; we adapt using a BytesIO temp
    with io.BytesIO(file_bytes) as bio:
        text = pdf_extract_text(bio)
    return _clean_text(text or "")

def extract_text_from_docx(file_bytes: bytes) -> str:
    with io.BytesIO(file_bytes) as bio:
        doc = Document(bio)
    text = "\n".join(p.text for p in doc.paragraphs)
    return _clean_text(text or "")

def extract_text(file_bytes: bytes, filename: str) -> Tuple[str, str]:
    """Return (text, ext). ext is one of {pdf, docx, txt}. Raises ValueError on unsupported."""
    lower = filename.lower()
    if lower.endswith(".pdf"):
        return extract_text_from_pdf(file_bytes), "pdf"
    if lower.endswith(".docx"):
        return extract_text_from_docx(file_bytes), "docx"
    if lower.endswith(".txt"):
        try:
            return _clean_text(file_bytes.decode("utf-8", errors="ignore")), "txt"
        except Exception:
            return _clean_text(file_bytes.decode("latin-1", errors="ignore")), "txt"
    raise ValueError("Unsupported file type. Please upload a PDF, DOCX, or TXT.")
