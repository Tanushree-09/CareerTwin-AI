from app.agents.profile_agent import ProfileAgent
from app.agents.skill_gap_agent import SkillGapAgent
from app.agents.learning_agent import LearningAgent

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

profile = ProfileAgent().analyze_resume(resume)

skill_gap = SkillGapAgent().analyze(profile)

roadmap = LearningAgent().generate(profile, skill_gap)

print(roadmap.model_dump_json(indent=4))