from app.agents.base_agent import BaseAgent
from app.core.prompts import SKILL_GAP_PROMPT
from app.models.skill_gap import SkillGap


class SkillGapAgent(BaseAgent):

    def analyze(self, profile):

        prompt = f"""
{SKILL_GAP_PROMPT}

Student Profile:

Name: {profile.name}

Education:
{profile.education}

Current Skills:
{", ".join(profile.skills)}

Projects:
{", ".join(profile.projects)}

Career Goal:
{profile.career_goal}
"""

        data = self.invoke(prompt)

        return SkillGap(**data)