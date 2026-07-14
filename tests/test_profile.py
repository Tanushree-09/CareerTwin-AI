from app.agents.profile_agent import ProfileAgent

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

agent = ProfileAgent()

profile = agent.analyze_resume(resume)

print(profile.model_dump_json(indent=4))