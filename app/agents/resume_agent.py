from app.agents.base_agent import BaseAgent
from app.core.prompts import RESUME_FEEDBACK_PROMPT
from app.models.resume_feedback import ResumeFeedback


class ResumeAgent(BaseAgent):

    def review(self, profile, project_analysis, readiness):

        prompt = f"""
{RESUME_FEEDBACK_PROMPT}

Career Goal:
{profile.career_goal}

Skills:
{", ".join(profile.skills)}

Projects:
{project_analysis.model_dump_json(indent=2)}

Career Readiness:
{readiness.model_dump_json(indent=2)}
"""

        data = self.invoke(prompt)

        return ResumeFeedback(**data)