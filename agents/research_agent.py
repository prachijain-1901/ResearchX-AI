# ==============================================================
# Research Agent
# ==============================================================
# Handles text-based research report generation.
# Reuses the existing IBM watsonx integration from services/watsonx.py
# to avoid code duplication.
# ==============================================================

from services.watsonx import generate_research


def run(topic):
    """
    Execute the Research Agent.

    Accepts a research topic string and delegates to the existing
    IBM watsonx generate_research() function.

    Parameters
    ----------
    topic : str
        The research topic provided by the user.

    Returns
    -------
    dict
        A dictionary with agent metadata and the raw LLM output:
        {
            "agent": "ResearchAgent",
            "topic": <str>,
            "raw_output": <str>   ← the IBM watsonx response
        }
    """

    # Delegate to the existing watsonx service
    raw_output = generate_research(topic)

    return {
        "agent": "ResearchAgent",
        "topic": topic,
        "raw_output": raw_output
    }
