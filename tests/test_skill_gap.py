from app.agents.profile_agent import ProfileAgent
from app.agents.skill_gap_agent import SkillGapAgent

resume = """
Name: Tiny

Education:
B.E Computer Science

Skills:
Python
SQL
Machine Learning

Projects:
Food Waste Management
CareerTwin AI

Career Goal:
AI Engineer
"""

profile_agent = ProfileAgent()
profile = profile_agent.analyze_resume(resume)

skill_agent = SkillGapAgent()
gap = skill_agent.analyze(profile)

print(gap.model_dump_json(indent=4))