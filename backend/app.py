from flask import Flask, jsonify, request
from flask_cors import CORS
from PyPDF2 import PdfReader

from resume_analyzer import (
    analyze_resume,
    match_job_description,
    calculate_job_match_score,
    generate_job_suggestions,
)

import io


app = Flask(__name__)

CORS(app)


@app.route("/")
def home():

    return jsonify({
        "message": "AI Resume Analyzer Backend is Running!"
    })


@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:

        return jsonify({
            "message": "No resume uploaded."
        })


    resume = request.files["resume"]

    job_description = request.form.get(
        "job_description",
        ""
    )


    # Read uploaded PDF

    pdf_data = resume.read()


    # Create PDF reader

    reader = PdfReader(
        io.BytesIO(pdf_data)
    )


    # Extract text

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"


    # Analyze resume

    analysis = analyze_resume(text)


    # Compare resume with job description

    matched_keywords, missing_keywords = match_job_description(
        text,
        job_description
    )


    # Calculate job match score

    job_match_score = calculate_job_match_score(
        matched_keywords,
        missing_keywords
    )


    # Generate job suggestions

    job_suggestions = generate_job_suggestions(
        missing_keywords
    )


    # Calculate ATS score breakdown


    # Send results to frontend

    return jsonify({

        "message": "Resume analyzed successfully!",

        "filename": resume.filename,

        "text": text,

        "score": analysis["score"],

        "skills": analysis["skills"],

        "email": analysis["email"],

        "phone": analysis["phone"],

        "sections": analysis["sections"],

        "suggestions": analysis["suggestions"],

        "matched_keywords": matched_keywords,

        "missing_keywords": missing_keywords,

        "job_match_score": job_match_score,

        "job_suggestions": job_suggestions,

        "score_breakdown": analysis["breakdown"]

    })


if __name__ == "__main__":

    app.run(debug=True)