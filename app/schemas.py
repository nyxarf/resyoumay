from pydantic import BaseModel
from typing import List


class ResumeRequest(BaseModel):
    name: str
    education: str
    skills: List[str]
    projects: List[str]
    experience: str
    achievements: str
    target_role: str