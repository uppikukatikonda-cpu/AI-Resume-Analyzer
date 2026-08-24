# AI Resume Analyzer

An AI-powered resume analysis web application that evaluates resumes for ATS compatibility, extracts important information, and compares a resume with a job description to identify matched and missing skills.

## 🚀 Features

### Resume Analysis

* Upload a PDF resume
* Extract resume text automatically
* Calculate an ATS compatibility score out of 100
* Detect technical skills
* Detect email address and phone number
* Check important resume sections
* Provide resume improvement suggestions

### ATS Score Breakdown

The ATS score is calculated using the following categories:

| Category            | Maximum Score |
| ------------------- | ------------: |
| Skills              |            30 |
| Contact Information |            15 |
| Education           |            15 |
| Projects            |            15 |
| Experience          |            10 |
| Certifications      |             5 |
| Skills Section      |            10 |
| **Total**           |       **100** |

### 🎯 Job Description Matching

The application can compare a resume against a job description and provide:

* Job Match Score
* Matched keywords
* Missing keywords
* Job-specific suggestions

## 🛠️ Technologies Used

### Backend

* Python
* Flask
* Flask-CORS
* PyPDF2

### Frontend

* HTML5
* CSS3
* JavaScript

### Development Tools

* Git
* GitHub
* Visual Studio Code

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│
├── .gitignore
├── README.md
├── architecture
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── resume_analyzer.py
│   └── test_ai.py
│
└── frontend/
    ├── index.html
    ├── script.js
    └── style.css
```

## ⚙️ How It Works

```text
User uploads resume
        ↓
Frontend sends resume + job description
        ↓
Flask backend receives the request
        ↓
PyPDF2 extracts text from PDF
        ↓
Resume analyzer processes the text
        ↓
ATS score is calculated
        ↓
Skills and resume sections are detected
        ↓
Resume is compared with job description
        ↓
Matched & missing keywords are identified
        ↓
Job match score is calculated
        ↓
Suggestions are generated
        ↓
Results are displayed in the frontend
```

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/uppikukatikonda-cpu/AI-Resume-Analyzer.git
```

### 2. Open the project

```bash
cd AI-Resume-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r backend/requirements.txt
```

## ▶️ Run the Application

Start the Flask backend:

```bash
python backend/app.py
```

The backend will run locally at:

```text
http://127.0.0.1:5000
```

Then open the frontend:
```text
frontend/index.html
``
in your browser.

## 📊 Example Analysis

The application can provide results such as:

* ATS Score: `92/100`
* Detected Skills: Python, Java, SQL, Flask, Git, etc.
* Job Match Score: `83/100`
* Matched Keywords
* Missing Keywords
* Resume Improvement Suggestions

> The scores are generated using the project's own rule-based scoring and keyword-matching logic. They are not official ATS scores from a recruiting platform.

## 🔐 Security

Sensitive information should not be committed to the repository.

The project `.gitignore` excludes files such as:

```text
.env
venv/
__pycache__/
.vscode/
*.log
```

API keys and other secrets should be stored in environment variables rather than directly inside the source code.

## 🔮 Future Improvements

Planned improvements include:

* AI-powered resume recommendations
* More advanced ATS keyword analysis
* Support for additional resume file formats
* Improved job-description matching
* Resume formatting analysis
* More detailed scoring visualizations
* Deployment as a public web application
* User-friendly dashboard

## 🎓 Learning Outcomes

This project helped me practice:

* Python programming
* Flask backend development
* REST API concepts
* PDF text extraction
* Frontend-backend integration
* Resume and keyword analysis
* Git and GitHub
* Building a practical AI/ML-oriented application

## 👨‍💻 Author

**Upendra**

B.Tech CSE (AI & ML)

## 🔗 Project Repository

GitHub: https://github.com/uppikukatikonda-cpu/AI-Resume-Analyzer
⭐ If you find this project useful, feel free to star the repository!
