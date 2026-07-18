"""
ResearchX AI Service

Temporary Offline Mode

This file returns professional mock responses when IBM watsonx
Runtime is unavailable.

Later you can uncomment the IBM code and everything will work again.
"""

from config import *

# ============================================================
# OPTIONAL IBM IMPORTS
# ============================================================

IBM_AVAILABLE = False

try:
    from ibm_watsonx_ai import Credentials
    from ibm_watsonx_ai.foundation_models import ModelInference

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

    IBM_AVAILABLE = True

except Exception as e:
    print("\nRunning in Offline Demo Mode")
    print(e)


# ============================================================
# RESEARCH GENERATION
# ============================================================

def generate_research(topic):

    if IBM_AVAILABLE:
        try:

            prompt = f"""
You are ResearchX AI.

Generate a professional research report on:

{topic}

Include:

1. Overview
2. Objectives
3. Background
4. Research Gap
5. Methodology
6. Future Scope
7. Recommended Papers
8. Conclusion
"""

            response = model.generate_text(
                prompt=prompt,
                params=params
            )

            return response

        except Exception as e:

            print(e)

    # -------------------------
    # Offline Demo Response
    # -------------------------

    return f"""
# Research Report

## Topic
{topic}

## Overview
Artificial Intelligence is transforming industries through automation,
decision support, and intelligent data analysis.

## Objectives

• Understand the domain

• Study recent technologies

• Analyze current research

• Identify future opportunities

## Background

AI systems use machine learning, deep learning,
and large language models to solve complex problems.

## Research Gap

Most existing systems provide static research.
There is limited work on lightweight Multi-Agent AI
research assistants with modular architectures.

## Methodology

- Literature Review
- Comparative Analysis
- AI-based Report Generation
- Multi-Agent Workflow

## Future Scope

- Agentic AI
- RAG Integration
- Citation Generator
- Knowledge Graph
- Real-time Paper Search

## Recommended Papers

1. Attention Is All You Need

2. ReAct

3. Retrieval Augmented Generation

4. LangGraph Documentation

## Conclusion

This research demonstrates how Multi-Agent AI
can improve automated research generation.
"""


# ============================================================
# PDF ANALYSIS
# ============================================================

def analyze_pdf(text):

    if IBM_AVAILABLE:

        try:

            text = text[:8000]

            prompt = f"""
Analyze the following research paper.

{text}

Generate:

1. Paper Summary

2. Key Findings

3. Research Gap

4. Advantages

5. Limitations

6. Future Scope

7. Conclusion
"""

            response = model.generate_text(
                prompt=prompt,
                params=params
            )

            return response

        except Exception as e:

            print(e)

    # -------------------------
    # Offline Demo Response
    # -------------------------

    return """
# PDF Analysis Report

## Paper Summary

The uploaded paper discusses recent developments
in Artificial Intelligence and Machine Learning.

## Key Findings

• High prediction accuracy

• Efficient learning models

• Strong experimental evaluation

• Improved automation

## Research Gap

Existing research has limited focus on
Multi-Agent AI architectures,
lightweight orchestration,
and autonomous research assistants.

## Advantages

• Scalable

• Accurate

• Efficient

• Easy to extend

## Limitations

• Requires quality datasets

• Computationally intensive

• Limited real-time validation

## Future Scope

• Agentic AI

• Retrieval-Augmented Generation (RAG)

• AI Agents

• Knowledge Graph Integration

• Autonomous Literature Review

## Conclusion

The paper provides a strong foundation
for future AI-driven research systems
and intelligent automation.
"""