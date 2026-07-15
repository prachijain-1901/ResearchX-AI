from flask import Flask, render_template, request, jsonify
from services.watsonx import generate_research, analyze_pdf
from services.pdf_service import extract_text
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
@app.route("/api/research", methods=["POST"])
def api_research():

    data = request.get_json()

    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({
            "error": "Please enter a research topic."
        }), 400

    result = generate_research(topic)

    return jsonify({
        "research": result
    })


# ----------------------------
# Analyze Uploaded PDF
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

    text = extract_text(filepath)

    result = analyze_pdf(text)

    return jsonify({
        "research": result
    })


if __name__ == "__main__":
    app.run(debug=True)