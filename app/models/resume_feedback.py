from pydantic import BaseModel
from typing import List


class ResumeFeedback(BaseModel):
    overall_score: int
    strengths: List[str]
    weaknesses: List[str]
    missing_sections: List[str]
    improvements: List[str]
    rewritten_points: List[str]