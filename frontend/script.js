async function analyzeResume() {

   const fileInput = document.getElementById("resumeFile");

const jobDescription = document.getElementById("jobDescription");

const result = document.getElementById("result");

    if (fileInput.files.length === 0) {
        result.innerHTML = "Please upload your resume first.";
        return;
    }

    const file = fileInput.files[0];

const jobText = jobDescription.value.trim();

    result.innerHTML = `
        <div class="loading">
            Analyzing your resume...
        </div>
    `;

    const formData = new FormData();

formData.append("resume", file);

formData.append("job_description", jobText);

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/analyze",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();


        /* -------------------------
           DETECTED SKILLS
        ------------------------- */

        let skillsHTML = "";

        if (data.skills.length > 0) {

            skillsHTML = data.skills
                .map(skill => `
                    <span class="skill-tag">
                        ${skill}
                    </span>
                `)
                .join("");

        } else {

            skillsHTML = `
                <p>No technical skills detected.</p>
            `;
        }


        /* -------------------------
           RESUME SECTIONS
        ------------------------- */

        let sectionsHTML = "";

        for (const section in data.sections) {

            const sectionName =
                section.charAt(0).toUpperCase() +
                section.slice(1);

            if (data.sections[section]) {

                sectionsHTML += `
                    <div class="section-item found">
                        ✓ ${sectionName}
                    </div>
                `;

            } else {

                sectionsHTML += `
                    <div class="section-item missing">
                        ✗ ${sectionName}
                    </div>
                `;
            }
        }


        /* -------------------------
           SUGGESTIONS
        ------------------------- */

        let suggestionsHTML = "";

        if (data.suggestions.length > 0) {

            suggestionsHTML = data.suggestions
                .map(suggestion => `
                    <li>${suggestion}</li>
                `)
                .join("");

        } else {

            suggestionsHTML = `
                <li>Your resume looks well structured!</li>
            `;
        }


        /* -------------------------
           DISPLAY RESULTS
        ------------------------- */

        result.innerHTML = `

            <div class="analysis">

                <h2>Resume Analysis</h2>


                <!-- ATS SCORE -->

                <div class="score-box">

    <div class="score-circle" style="--score: ${data.score}">

        <div class="score">
            ${data.score}
        </div>

        <span>/100</span>

    </div>

    <p>ATS Compatibility Score</p>

</div>


                <!-- DETECTED SKILLS -->

<div class="analysis-section">

    <h3>Detected Skills</h3>

    <div class="skills">
        ${skillsHTML}
    </div>

</div>


<!-- ATS SCORE BREAKDOWN -->

<div class="analysis-section">

    <h3>ATS Score Breakdown</h3>

    <div class="score-breakdown">

        ${Object.entries(data.score_breakdown)
            .map(([category, score]) => {

                const maximums = {
    "Skills": 30,
    "Contact Information": 15,
    "Education": 15,
    "Projects": 15,
    "Experience": 10,
    "Certifications": 5,
    "Skills Section": 10
};

const maximum = maximums[category];

                const percentage =
                    (score / maximum) * 100;

                return `
                    
                    <div class="breakdown-item">

                        <div class="breakdown-header">

                            <span>${category}</span>

                            <strong>${score}/${maximum}</strong>

                        </div>

                        <div class="progress-bar">

                            <div
                                class="progress"
                                style="width: ${percentage}%"
                            ></div>

                        </div>

                    </div>

                `;

            })
            .join("")}

    </div>

</div>


<!-- JOB MATCH SCORE -->

<div class="analysis-section">

    <h3>Job Match Score</h3>

    <div
    class="job-score-circle"
    style="--score: ${data.job_match_score}"
>

    <div class="job-score-value">
        ${data.job_match_score}
    </div>

    <span>/100</span>

</div>

</div>


<!-- MATCHED KEYWORDS -->

<div class="analysis-section">

    <h3>Matched Keywords</h3>

    <div class="keyword-container">

        ${
            data.matched_keywords.length > 0
            ? data.matched_keywords
                .map(keyword => `
                    <span class="matched-tag">
                        ✓ ${keyword}
                    </span>
                `)
                .join("")
            : "<p>No matching keywords found.</p>"
        }

    </div>

</div>


<!-- MISSING KEYWORDS -->

<div class="analysis-section">

    <h3>Missing Keywords</h3>

    <div class="keyword-container">

        ${
            data.missing_keywords.length > 0
            ? data.missing_keywords
                .map(keyword => `
                    <span class="missing-tag">
                        ⚠ ${keyword}
                    </span>
                `)
                .join("")
            : "<p>No missing keywords detected.</p>"
        }

    </div>

</div>


                <!-- RESUME SECTIONS -->

                <div class="analysis-section">

                    <h3>Resume Sections</h3>

                    <div class="sections">
                        ${sectionsHTML}
                    </div>

                </div>


                <!-- CONTACT INFORMATION -->

                <!-- CONTACT INFORMATION -->

<div class="analysis-section">

    <h3>Contact Information</h3>

    <div class="contact-info">

        <div class="contact-item">

            <strong>Email</strong>

            <span>
                ${data.email || "Not detected"}
            </span>

        </div>


        <div class="contact-item">

            <strong>Phone</strong>

            <span>
                ${data.phone || "Not detected"}
            </span>

        </div>

    </div>

</div>


                <!-- SUGGESTIONS -->

<div class="analysis-section">

    <h3>Improvement Suggestions</h3>

    <ul class="suggestions">
        ${suggestionsHTML}
    </ul>

</div>


<!-- ANALYZE ANOTHER RESUME -->

<div class="another-resume">

    <button
        type="button"
        onclick="resetAnalyzer()"
    >
        ↻ Analyze Another Resume
    </button>

</div>


<!-- RESUME TEXT -->

<div class="analysis-section">

    <h3>Extracted Resume Text</h3>

    <div class="resume-text">
        ${data.text.replace(/\n/g, "<br>")}
    </div>

</div>

</div>
        `;

    }

    catch (error) {

        console.error(error);

        result.innerHTML = `
            <p class="error">
                Unable to connect to the backend.
            </p>
        `;
    }
}
function resetAnalyzer() {

    const fileInput =
        document.getElementById("resumeFile");

    const result =
        document.getElementById("result");

    fileInput.value = "";

    result.innerHTML = "";

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}