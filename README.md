# Resyoumay — AI Resume Builder

Resyoumay is an AI-powered resume builder that generates professional, ATS-optimized resumes from structured user input. It helps users quickly create high-quality resumes with intelligent content suggestions and clean formatting.

>  **Capstone Project**
> This project was developed as a capstone project for the **Edunet Foundation AICTE Internship Program**, conducted in association with **IBM SkillsBuild**.

---

##  Features

*  AI-generated resume content from user details
*  Clean, professional resume formatting
*  Intelligent keyword extraction for ATS optimization
*  Downloadable output (PDF / document formats)
*  Simple, user-friendly web interface
*  Fast generation with modern frontend stack
*  Modular backend for future enhancements

---

##  AI & Machine Learning Integrations

Resyoumay integrates modern AI tools and NLP techniques to enhance resume quality.

###  Large Language Model (LLM)

* Uses **Groq-accelerated LLM inference** for generating resume content
* Produces professional summaries, experience descriptions, and bullet points
* Tailors output based on user input data

###  Keyword Extraction (NLP)

* Uses **KeyBERT** for extracting relevant keywords from job descriptions or user data
* Helps optimize resumes for Applicant Tracking Systems (ATS)
* Improves visibility during automated screening

###  ML-Driven Enhancements

* Context-aware text generation
* Structured content transformation
* Natural language processing for summarization and rewriting

---

##  Tech Stack

### Frontend

* React (Vite)
* JavaScript (ES6+)
* HTML5 & CSS3

### Backend

* Python
* FastAPI (or equivalent API framework)
* RESTful API architecture

### AI / NLP Libraries

* Groq API (LLM inference)
* KeyBERT (keyword extraction)
* Transformer-based NLP models

---

##  Project Structure

```
resyoumay/
│
├── app/                # Backend application logic
├── frontend/           # React frontend
├── demo/               # Sample input data
├── requirements.txt    # Python dependencies
├── page.html           # Standalone demo page
└── README.md
```

---

##  How to Run Locally

###  Clone the Repository

```
git clone https://github.com/yourusername/resyoumay.git
cd resyoumay
```

---

###  Backend Setup

Create a virtual environment and install dependencies:

```
pip install -r requirements.txt
```

Set your API key as an environment variable:

```
GROQ_API_KEY=your_api_key_here
```

Run the backend server:

```
python app/main.py
```

---

###  Frontend Setup

```
cd frontend
npm install
npm run dev
```

Open the local development URL shown in the terminal.

---

##  Use Cases

* Students and fresh graduates creating their first resume
* Professionals updating resumes quickly
* Generating ATS-friendly resumes for job applications
* Rapid resume drafting for multiple roles

---

##  Future Improvements

* Multiple resume templates
* Job-description matching
* Cover letter generation
* Cloud deployment
* User accounts & resume storage
* Multilingual support

---

##  Author
Arfa Ahmed Ansari
Developed as part of the **Edunet Foundation AICTE Internship Program (IBM SkillsBuild)** capstone project.

---

##  License

This project is for educational and demonstration purposes.
