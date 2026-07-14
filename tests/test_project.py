from app.agents.profile_agent import ProfileAgent
from app.agents.project_agent import ProjectAgent

resume = """
Name: Tiny

Education:
B.E Computer Science

Skills:
Python
SQL
Machine Learning
FastAPI

Projects:
Food Waste Management
CareerTwin AI

Career Goal:
AI Engineer
"""

profile = ProfileAgent().analyze_resume(resume)

analysis = ProjectAgent().analyze(profile)

print(analysis.model_dump_json(indent=4))