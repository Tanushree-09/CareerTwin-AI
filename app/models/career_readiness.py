from pydantic import BaseModel
from typing import List


class CareerReadiness(BaseModel):
    overall_score: int
    skill_score: int
    project_score: int
    learning_score: int
    summary: str
    next_steps: List[str]