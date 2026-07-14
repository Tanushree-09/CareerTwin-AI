from pydantic import BaseModel
from typing import List


class SkillGap(BaseModel):
    existing_skills: List[str]
    required_skills: List[str]
    missing_skills: List[str]
    priority_skills: List[str]
    explanation: str