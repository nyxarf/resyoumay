from .groq_client import generate_text


def generate_resume(data: dict) -> str:
    prompt = f"""
Create a professional resume using this information:

Name: {data['name']}
Education: {data['education']}
Skills: {data['skills']}
Projects: {data['projects']}
Experience: {data['experience']}
Achievements: {data['achievements']}

Make it clean, ATS-friendly, and concise.
"""
    return generate_text(prompt)


def generate_cover_letter(data: dict) -> str:
    prompt = f"""
Write a professional cover letter for a student with:

Name: {data['name']}
Skills: {data['skills']}
Projects: {data['projects']}
Role applying for: {data['target_role']}
"""
    return generate_text(prompt)


def generate_portfolio_summary(data: dict) -> str:
    prompt = f"""
Create a professional, ATS-optimized resume.

- Use bullet points.
- Quantify achievements (%, numbers, impact).
- Avoid placeholders.
- Do NOT use 20XX.
- Use strong action verbs.
- Make it tailored for a {data['target_role']} role.
...
"""
    return generate_text(prompt)