from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util
from fastapi.middleware.cors import CORSMiddleware

from .schemas import ResumeRequest
from .resume_generator import (
    generate_resume,
    generate_cover_letter,
    generate_portfolio_summary
)
from .keyword_extractor import extract_keywords


# --------------------------------------------------
# App Initialization
# --------------------------------------------------

app = FastAPI(title="AI Resume Builder API")

# Load embedding model once (for job matching)
model = SentenceTransformer("all-MiniLM-L6-v2")


# --------------------------------------------------
# CORS (keep near top for clarity)
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Root
# --------------------------------------------------

@app.get("/")
def root():
    return {"message": "AI Resume Builder Backend Running 🚀"}


# --------------------------------------------------
# GENERATE ENDPOINT
# --------------------------------------------------

@app.post("/generate")
def generate_all(data: ResumeRequest):

    resume = generate_resume(data.dict())
    cover_letter = generate_cover_letter(data.dict())
    portfolio = generate_portfolio_summary(data.dict())

    keywords = extract_keywords(resume)

    return {
        "resume": resume,
        "cover_letter": cover_letter,
        "portfolio_summary": portfolio,
        "ats_keywords": keywords
    }


# --------------------------------------------------
# ATS SCORE MODULE
# --------------------------------------------------

class ATSRequest(BaseModel):
    resume_text: str
    skills: list[str]
    target_role: str


def calculate_ats_score(resume_text: str, skills: list[str], target_role: str):
    score = 0
    text = resume_text.lower()

    # Length feature
    word_count = len(resume_text.split())
    if word_count > 300:
        score += 20
    elif word_count > 150:
        score += 10

    # Skills feature
    score += min(len(skills) * 5, 30)

    # Role keyword feature
    if target_role.lower() in text:
        score += 20

    # Action verbs feature
    verbs = ["developed", "implemented", "designed", "built", "led"]
    score += sum(v in text for v in verbs) * 2

    return min(score, 100)


@app.post("/ats-score")
def ats_score(data: ATSRequest):
    score = calculate_ats_score(
        data.resume_text,
        data.skills,
        data.target_role
    )

    return {
        "ats_score": score,
        "verdict": "Strong" if score > 70 else "Moderate" if score > 40 else "Weak"
    }


# --------------------------------------------------
# JOB MATCH MODULE (Semantic Similarity)
# --------------------------------------------------

class MatchRequest(BaseModel):
    resume_text: str
    job_description: str


def calculate_job_match(resume_text: str, job_description: str):
    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(job_description, convert_to_tensor=True)

    similarity = util.cos_sim(emb1, emb2).item()
    return round(similarity * 100, 2)


@app.post("/job-match")
def job_match(data: MatchRequest):
    score = calculate_job_match(
        data.resume_text,
        data.job_description
    )

    return {
        "job_match_score": score,
        "recommendation": "Good alignment"
        if score > 70
        else "Needs improvement"
    }