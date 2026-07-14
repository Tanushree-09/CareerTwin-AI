from app.agents.base_agent import BaseAgent
from app.core.prompts import CAREER_READINESS_PROMPT
from app.models.career_readiness import CareerReadiness


class ReadinessAgent(BaseAgent):

    def evaluate(self, profile, skill_gap, roadmap, project_analysis):

        prompt = f"""
{CAREER_READINESS_PROMPT}

Career Goal:
{profile.career_goal}

Current Skills:
{", ".join(profile.skills)}

Missing Skills:
{", ".join(skill_gap.missing_skills)}

Projects:
{", ".join(profile.projects)}

Project Analysis:
{project_analysis.model_dump_json(indent=2)}

Learning Roadmap:
{roadmap.model_dump_json(indent=2)}
"""

        data = self.invoke(prompt)

        return CareerReadiness(**data)