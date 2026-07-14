from app.agents.base_agent import BaseAgent
from app.core.prompts import COURSE_RECOMMENDATION_PROMPT
from app.models.course_recommendation import CourseRecommendation


class CourseAgent(BaseAgent):

    def recommend(self, profile, skill_gap):

        prompt = f"""
{COURSE_RECOMMENDATION_PROMPT}

Career Goal:
{profile.career_goal}

Missing Skills:
{", ".join(skill_gap.missing_skills)}

Priority Skills:
{", ".join(skill_gap.priority_skills)}
"""

        data = self.invoke(prompt)

        return CourseRecommendation(**data)