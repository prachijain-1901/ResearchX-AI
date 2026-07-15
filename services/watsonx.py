from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from config import *

credentials = Credentials(
    url=IBM_URL,
    api_key=IBM_API_KEY
)

model = ModelInference(
    model_id=IBM_MODEL_ID,
    credentials=credentials,
    project_id=IBM_PROJECT_ID
)

params = {
    "decoding_method": "greedy",
    "max_new_tokens": 1200,
    "min_new_tokens": 100,
    "temperature": 0.3
}


# ==========================================
# Generate Research from Topic
# ==========================================

def generate_research(topic):

    prompt = f"""
You are ResearchX AI.

Generate a professional research report on:

{topic}

Include the following headings:

1. Overview
2. Objectives
3. Background
4. Research Gap
5. Methodology
6. Future Scope
7. Recommended Papers
8. Conclusion

Write in professional English.
"""

    try:

        response = model.generate_text(
            prompt=prompt,
            params=params
        )

        print("\n========== RESEARCH RESPONSE ==========\n")
        print(response)

        return response

    except Exception as e:

        print("\n========== IBM ERROR ==========\n")
        print(e)

        return f"Error: {str(e)}"


# ==========================================
# Analyze Uploaded PDF
# ==========================================

def analyze_pdf(text):

    # Keep prompt size manageable
    text = text[:8000]

    prompt = f"""
You are ResearchX AI.

Analyze the following research paper.

{text}

Generate a professional report with these headings:

1. Paper Summary
2. Key Findings
3. Research Gap
4. Advantages
5. Limitations
6. Future Scope
7. Final Conclusion

Write in professional English.
"""

    try:

        response = model.generate_text(
            prompt=prompt,
            params=params
        )

        print("\n========== PDF ANALYSIS ==========\n")
        print(response)

        return response

    except Exception as e:

        print("\n========== IBM ERROR ==========\n")
        print(e)

        return f"Error: {str(e)}"