# ==============================================================
# Report Agent
# ==============================================================
# Accepts the raw output produced by the Research Agent or
# PDF Agent and formats it into a clean, structured report.
#
# This agent does NOT call the LLM again — it performs
# lightweight text post-processing only.
# ==============================================================

import re


def _extract_section(text, heading):
    """
    Try to pull content under a heading like "1. Overview" or
    "## Overview" from the raw LLM output.

    Returns the extracted paragraph or an empty string.
    """

    # Match numbered headings (e.g. "1. Overview") or markdown headings (e.g. "## Overview")
    pattern = rf"(?:^|\n)\s*(?:\d+\.\s*)?(?:#+\s*)?{re.escape(heading)}\s*\n(.*?)(?=\n\s*(?:\d+\.\s*)?(?:#+\s*)?\S|\Z)"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)

    if match:
        return match.group(1).strip()

    return ""


def _build_key_points(text):
    """
    Extract bullet-pointed key points from the raw output.
    Looks for lines starting with '-', '*', or numbered items.
    Returns a list of strings.
    """

    points = []

    for line in text.split("\n"):
        stripped = line.strip()
        # Match lines that look like bullet points or numbered items
        if re.match(r"^[-*•]\s+", stripped) or re.match(r"^\d+[\.\)]\s+", stripped):
            # Clean the bullet prefix
            clean = re.sub(r"^[-*•\d\.\)]+\s*", "", stripped).strip()
            if clean:
                points.append(clean)

    return points


def format_report(agent_result):
    """
    Format the raw agent output into a structured report.

    Parameters
    ----------
    agent_result : dict
        Output from ResearchAgent or PDFAgent containing:
        - "agent"      : str  — which agent produced the output
        - "raw_output" : str  — the raw LLM response text
        - "topic"      : str  (only for ResearchAgent)
        - "filepath"   : str  (only for PDFAgent)

    Returns
    -------
    dict
        A structured report dictionary:
        {
            "title": str,
            "summary": str,
            "key_points": list[str],
            "conclusion": str,
            "full_report": str,
            "agent_used": str
        }
    """

    raw = agent_result.get("raw_output", "")
    agent_name = agent_result.get("agent", "Unknown")

    # ------------------------------------------------------------------
    # Title
    # ------------------------------------------------------------------
    if agent_name == "ResearchAgent":
        title = f"Research Report: {agent_result.get('topic', 'Untitled')}"
    else:
        title = "PDF Analysis Report"

    # ------------------------------------------------------------------
    # Summary — try to extract from known headings
    # ------------------------------------------------------------------
    summary = (
        _extract_section(raw, "Overview")
        or _extract_section(raw, "Paper Summary")
        or _extract_section(raw, "Summary")
    )

    # Fallback: use the first 500 characters as a summary
    if not summary:
        summary = raw[:500].strip()
        if len(raw) > 500:
            summary += "..."

    # ------------------------------------------------------------------
    # Key Points — gather bullet points from the entire output
    # ------------------------------------------------------------------
    key_points = _build_key_points(raw)

    # If no bullet points were found, try to extract "Key Findings"
    if not key_points:
        findings = _extract_section(raw, "Key Findings")
        if findings:
            key_points = [line.strip() for line in findings.split("\n") if line.strip()]

    # Final fallback — inform the reader
    if not key_points:
        key_points = ["Refer to the full report below for detailed findings."]

    # ------------------------------------------------------------------
    # Conclusion — pull from known headings
    # ------------------------------------------------------------------
    conclusion = (
        _extract_section(raw, "Conclusion")
        or _extract_section(raw, "Final Conclusion")
    )

    if not conclusion:
        conclusion = "Please refer to the full report for the conclusion."

    # ------------------------------------------------------------------
    # Assemble the structured report
    # ------------------------------------------------------------------
    return {
        "title": title,
        "summary": summary,
        "key_points": key_points,
        "conclusion": conclusion,
        "full_report": raw,
        "agent_used": agent_name
    }
