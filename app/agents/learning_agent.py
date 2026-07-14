from app.agents.base_agent import BaseAgent
from app.core.prompts import LEARNING_ROADMAP_PROMPT
from app.models.learning_roadmap import LearningRoadmap


class LearningAgent(BaseAgent):

    def generate(self, profile, skill_gap, timeline):

        prompt = f"""
{LEARNING_ROADMAP_PROMPT}

Student Name:
{profile.name}

Career Goal:
{profile.career_goal}

Timeline:
{timeline}

Current Skills:
{", ".join(profile.skills)}

Missing Skills:
{", ".join(skill_gap.missing_skills)}

Priority Skills:
{", ".join(skill_gap.priority_skills)}
"""

        data = self.invoke(prompt)

        return LearningRoadmap(**data)