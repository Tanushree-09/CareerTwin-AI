from pydantic import BaseModel
from typing import List


class RoadmapStep(BaseModel):
    week: int
    topic: str
    objective: str


class LearningRoadmap(BaseModel):
    roadmap: List[RoadmapStep]
    final_goal: str