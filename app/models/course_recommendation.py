from pydantic import BaseModel
from typing import List


class Course(BaseModel):
    skill: str
    title: str
    provider: str
    level: str
    duration: str
    reason: str
    link: str          # <-- Add this


class CourseRecommendation(BaseModel):
    recommendations: List[Course]