# ==============================================================
# Planner Agent
# ==============================================================
# A lightweight, rule-based agent that inspects the incoming
# request and decides which downstream agent should handle it.
#
# Decision logic:
#   - "pdf"      → the request contains a PDF file upload
#   - "research" → the request contains a text topic
# ==============================================================


def decide(request_type, data=None):
    """
    Decide which agent should handle the request.

    Parameters
    ----------
    request_type : str
        Either "topic" or "pdf" — indicates what the user submitted.
    data : dict, optional
        Extra context (not used in rule-based version, kept for
        future LLM-based planning).

    Returns
    -------
    str
        The agent key: "research" or "pdf".
    """

    if request_type == "pdf":
        return "pdf"

    # Default to research for any text-based request
    return "research"
