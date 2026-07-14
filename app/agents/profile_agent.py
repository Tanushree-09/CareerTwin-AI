from app.agents.base_agent import BaseAgent
from app.core.prompts import PROFILE_AGENT_PROMPT
from app.models.student_profile import StudentProfile


class ProfileAgent(BaseAgent):

    def analyze_resume(self, resume_text: str):

        prompt = f"""
{PROFILE_AGENT_PROMPT}

Resume:

{resume_text}
"""

        data = self.invoke(prompt)

        return StudentProfile(**data)