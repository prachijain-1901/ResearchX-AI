from flask import Flask, render_template, request, jsonify
from agents.agent_manager import handle_research, handle_pdf
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


# ----------------------------
# Generate Research from Topic
# ----------------------------
# Now routed through the Multi-Agent pipeline:
#   Planner → Research Agent → Report Agent
# ----------------------------
@app.route("/api/research", methods=["POST"])
def api_research():

    data = request.get_json()

    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({
            "error": "Please enter a research topic."
        }), 400

    # Delegate to the Agent Manager
    report = handle_research(topic)

    # Return the full report as "research" to maintain backward compatibility
    return jsonify({
        "research": report.get("full_report", ""),
        "structured_report": report
    })


# ----------------------------
# Analyze Uploaded PDF
# ----------------------------
# Now routed through the Multi-Agent pipeline:
#   Planner → PDF Agent → Report Agent
# ----------------------------
@app.route("/api/analyze_pdf", methods=["POST"])
def analyze_pdf_route():

    if "pdf" not in request.files:
        return jsonify({
            "error": "No PDF uploaded."
        }), 400

    pdf = request.files["pdf"]

    if pdf.filename == "":
        return jsonify({
            "error": "Please select a PDF."
        }), 400

    filepath = os.path.join(UPLOAD_FOLDER, pdf.filename)

    pdf.save(filepath)

    # Delegate to the Agent Manager
    report = handle_pdf(filepath)

    # Return the full report as "research" to maintain backward compatibility
    return jsonify({
        "research": report.get("full_report", ""),
        "structured_report": report
    })


if __name__ == "__main__":
    app.run(debug=True)