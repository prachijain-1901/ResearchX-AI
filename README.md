# ResearchX AI

ResearchX AI is an AI-powered research assistant built using **IBM watsonx AI**, **Flask**, **HTML**, **CSS**, and **JavaScript**. It helps researchers and students generate structured research reports and analyze research papers using Large Language Models (LLMs).

---

## Features

- AI Research Report Generator
- Research Paper (PDF) Analyzer
- IBM watsonx LLM Integration
- Clean and Responsive User Interface
- Download Research Reports
- Flask Backend with REST APIs

---

## Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Flask (Python)

### AI Model
- IBM watsonx AI
- Llama 3.3 70B Instruct

### Libraries
- ibm-watsonx-ai
- PyMuPDF
- python-docx
- reportlab
- python-dotenv

---

## Project Structure

```
ResearchX-AI/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── services/
│   ├── watsonx.py
│   └── pdf_service.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   └── index.html
│
├── uploads/
├── reports/
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/prachijain-1901/ResearchX-AI.git
```

Go to project directory

```bash
cd ResearchX-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
IBM_API_KEY=YOUR_API_KEY
IBM_PROJECT_ID=YOUR_PROJECT_ID
IBM_URL=https://au-syd.ml.cloud.ibm.com
IBM_MODEL_ID=meta-llama/llama-3-3-70b-instruct
```

Run the application

```bash
python app.py
```

Open in browser

```
http://127.0.0.1:5000
```

---

## Usage

### Generate Research

1. Enter a research topic.
2. Click **Generate Research**.
3. Receive a detailed AI-generated research report.

### Analyze PDF

1. Upload a research paper in PDF format.
2. Click **Analyze PDF**.
3. View the AI-generated summary and insights.

---

## Screenshots

### Home Page

_Add project screenshot here_

### AI Generated Research

_Add screenshot here_

### PDF Analysis

_Add screenshot here_

---

## Future Improvements

- Citation Generator (APA, MLA, IEEE)
- Literature Review Generation
- Research Gap Detection
- Multi-language Support
- Export to PDF and DOCX
- User Authentication
- Research Dashboard

---

## Author

**Prachi Jain**

B.Tech Computer Science Engineering

---

## Acknowledgements

- IBM watsonx AI
- Flask
- Python
- GitHub
