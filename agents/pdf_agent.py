# ==============================================================
# PDF Agent
# ==============================================================
# Handles analysis of uploaded research papers (PDFs).
# Reuses:
#   - services/pdf_service.py   → text extraction (PyMuPDF)
#   - services/watsonx.py       → LLM-based analysis
# ==============================================================

from services.pdf_service import extract_text
from services.watsonx import analyze_pdf


def run(filepath):
    """
    Execute the PDF Agent.

    Extracts text from the uploaded PDF and sends it to the
    existing IBM watsonx analyze_pdf() function.

    Parameters
    ----------
    filepath : str
        Absolute or relative path to the uploaded PDF file.

    Returns
    -------
    dict
        A dictionary with agent metadata and the raw LLM output:
        {
            "agent": "PDFAgent",
            "filepath": <str>,
            "raw_output": <str>   ← the IBM watsonx response
        }
    """

    # Step 1 — Extract text from the PDF using the existing service
    text = extract_text(filepath)

    # Step 2 — Analyze the extracted text via IBM watsonx
    raw_output = analyze_pdf(text)

    return {
        "agent": "PDFAgent",
        "filepath": filepath,
        "raw_output": raw_output
    }
