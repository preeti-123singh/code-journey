from flask import Flask, request, jsonify
from flask_cors import CORS
import docx2txt
from PyPDF2 import PdfReader
import re

app = Flask(__name__)
CORS(app)

def extract_text(file):
    if file.filename.endswith('.pdf'):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + " "
        return text.lower()
    elif file.filename.endswith('.docx'):
        text = docx2txt.process(file)
        return text.lower()
    else:
        return file.read().decode("utf-8").lower()

def extract_keywords(text):
    # simple: split by non-alphabetic characters, remove short words
    words = re.findall(r'\b[a-zA-Z]{2,}\b', text)
    return set(words)

@app.route('/match', methods=['POST'])
def match_resumes():
    resumes = request.files.getlist('resumes')
    jd = request.form.get('job_description', '').lower()
    if not resumes or not jd.strip():
        return jsonify({"error": "No resumes or job description provided"}), 400

    jd_keywords = extract_keywords(jd)
    results = []

    for resume in resumes:
        resume_text = extract_text(resume)
        resume_keywords = extract_keywords(resume_text)

        matching_keywords = list(jd_keywords & resume_keywords)
        missing_keywords = list(jd_keywords - resume_keywords)
        match_percentage = int(len(matching_keywords) / max(len(jd_keywords), 1) * 100)

        future_suggestions = ", ".join(f"Learn {kw}" for kw in missing_keywords[:5])

        results.append({
            "name": resume.filename,
            "match_percentage": match_percentage,
            "matching_keywords": matching_keywords,
            "missing_keywords": missing_keywords,
            "future_suggestions": future_suggestions
        })

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
