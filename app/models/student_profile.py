from pydantic import BaseModel
from typing import List


class StudentProfile(BaseModel):
    name: str

    education: str

    skills: List[str]

    projects: List[str]

    experience: List[str]

    certifications: List[str]

    career_goal: str

    strengths: List[str]

    weaknesses: List[str]