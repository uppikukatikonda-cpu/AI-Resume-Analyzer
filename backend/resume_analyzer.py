import re


SKILLS = [
    "python",
    "java",
    "c++",
    "c",
    "html",
    "css",
    "javascript",
    "sql",
    "react",
    "flask",
    "django",
    "node.js",
    "mongodb",
    "mysql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",
    "scikit-learn",
    "git",
    "github",
    "aws",
    "docker"
]


def find_skills(text):

    text_lower = text.lower()

    found = []

    for skill in SKILLS:

        if skill in text_lower:
            found.append(skill)

    return found


def find_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def find_phone(text):

    pattern = r"\b(?:\+91[\s-]?)?[6-9]\d{9}\b"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def check_section(text, keywords):

    text_lower = text.lower()

    for keyword in keywords:

        if keyword in text_lower:
            return True

    return False


def analyze_resume(text):

    skills = find_skills(text)

    email = find_email(text)

    phone = find_phone(text)

    sections = {

        "education": check_section(
            text,
            ["education", "b.tech", "bachelor", "degree"]
        ),

        "projects": check_section(
            text,
            ["projects", "project"]
        ),

        "experience": check_section(
            text,
            ["experience", "internship", "intern"]
        ),

        "certifications": check_section(
            text,
            ["certifications", "certification", "certificate"]
        ),

        "skills": check_section(
            text,
            ["skills", "technical skills"]
        )
    }


    # ==============================
    # ATS SCORE BREAKDOWN
    # ==============================

    breakdown = {}


    # Skills: 30 points

    breakdown["Skills"] = min(
        len(skills) * 3,
        30
    )


    # Contact Information: 15 points

    contact_score = 0

    if email:
        contact_score += 8

    if phone:
        contact_score += 7

    breakdown["Contact Information"] = contact_score


    # Education: 15 points

    if sections["education"]:
        breakdown["Education"] = 15
    else:
        breakdown["Education"] = 0


    # Projects: 15 points

    if sections["projects"]:
        breakdown["Projects"] = 15
    else:
        breakdown["Projects"] = 0


    # Experience: 10 points

    if sections["experience"]:
        breakdown["Experience"] = 10
    else:
        breakdown["Experience"] = 0


    # Certifications: 5 points

    if sections["certifications"]:
        breakdown["Certifications"] = 5
    else:
        breakdown["Certifications"] = 0


    # Skills Section: 10 points

    if sections["skills"]:
        breakdown["Skills Section"] = 10
    else:
        breakdown["Skills Section"] = 0


    # ==============================
    # FINAL ATS SCORE
    # ==============================

    score = sum(breakdown.values())


    # ==============================
    # SUGGESTIONS
    # ==============================

    suggestions = []


    if not email:

        suggestions.append(
            "Add a professional email address."
        )


    if not phone:

        suggestions.append(
            "Add a phone number."
        )


    if not sections["education"]:

        suggestions.append(
            "Add an Education section."
        )


    if not sections["projects"]:

        suggestions.append(
            "Add a Projects section."
        )


    if not sections["experience"]:

        suggestions.append(
            "Add internship or experience details if applicable."
        )


    if not sections["certifications"]:

        suggestions.append(
            "Consider adding relevant certifications."
        )


    if len(skills) < 5:

        suggestions.append(
            "Add more relevant technical skills that you genuinely know."
        )


    return {

        "score": score,

        "skills": skills,

        "email": email,

        "phone": phone,

        "sections": sections,

        "suggestions": suggestions,

        "breakdown": breakdown
    }
def match_job_description(resume_text, job_description):
    resume_lower = resume_text.lower()
    job_lower = job_description.lower()

    matched = []
    missing = []

    for skill in SKILLS:
        if skill in job_lower:
            if skill in resume_lower:
                matched.append(skill)
            else:
                missing.append(skill)

    return matched, missing


def calculate_job_match_score(matched, missing):
    total = len(matched) + len(missing)

    if total == 0:
        return 0

    score = (len(matched) / total) * 100

    return round(score)
def generate_job_suggestions(missing_keywords):

    suggestions = []

    for keyword in missing_keywords:

        suggestions.append(
            f"If you have experience with {keyword}, "
            f"consider adding it to your resume."
        )

    if len(missing_keywords) == 0:

        suggestions.append(
            "Great! Your resume contains the main skills "
            "detected in the job description."
        )

    return suggestions