from pydantic import BaseModel
from typing import List


class ProjectEvaluation(BaseModel):
    project_name: str
    score: float
    strengths: List[str]
    weaknesses: List[str]
    missing_features: List[str]
    recommendations: List[str]
    resume_ready: bool


class ProjectAnalysis(BaseModel):
    projects: List[ProjectEvaluation]