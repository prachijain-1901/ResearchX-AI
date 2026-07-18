# ==============================================================
# Agent Manager (Orchestrator)
# ==============================================================
# Central coordinator for the Multi-Agent pipeline:
#
#   1. Receives the incoming request type and data.
#   2. Calls the Planner Agent to decide which agent to invoke.
#   3. Executes the selected agent (Research or PDF).
#   4. Passes the raw output through the Report Agent.
#   5. Returns the final structured result.
#
# Flow:
#   Request → Planner → Research/PDF Agent → Report Agent → Response
# ==============================================================

from agents.planner import decide
from agents.research_agent import run as run_research
from agents.pdf_agent import run as run_pdf
from agents.report_agent import format_report


def handle_research(topic):
    """
    Handle a text-based research request through the full agent pipeline.

    Parameters
    ----------
    topic : str
        The research topic provided by the user.

    Returns
    -------
    dict
        The structured report from the Report Agent.
    """

    # Step 1 — Planner decides the agent
    agent_key = decide(request_type="topic")
    print(f"[AgentManager] Planner selected: {agent_key}")

    # Step 2 — Execute the Research Agent
    agent_result = run_research(topic)
    print(f"[AgentManager] {agent_result['agent']} completed.")

    # Step 3 — Post-process via Report Agent
    report = format_report(agent_result)
    print(f"[AgentManager] Report Agent formatted the output.")

    return report


def handle_pdf(filepath):
    """
    Handle a PDF analysis request through the full agent pipeline.

    Parameters
    ----------
    filepath : str
        Path to the uploaded PDF file.

    Returns
    -------
    dict
        The structured report from the Report Agent.
    """

    # Step 1 — Planner decides the agent
    agent_key = decide(request_type="pdf")
    print(f"[AgentManager] Planner selected: {agent_key}")

    # Step 2 — Execute the PDF Agent
    agent_result = run_pdf(filepath)
    print(f"[AgentManager] {agent_result['agent']} completed.")

    # Step 3 — Post-process via Report Agent
    report = format_report(agent_result)
    print(f"[AgentManager] Report Agent formatted the output.")

    return report
