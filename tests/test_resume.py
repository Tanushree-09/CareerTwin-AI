from app.agents.profile_agent import ProfileAgent
from app.agents.skill_gap_agent import SkillGapAgent
from app.agents.learning_agent import LearningAgent
from app.agents.project_agent import ProjectAgent
from app.agents.readiness_agent import ReadinessAgent
from app.agents.resume_agent import ResumeAgent

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

gap = SkillGapAgent().analyze(profile)

roadmap = LearningAgent().generate(profile, gap)

projects = ProjectAgent().analyze(profile)

readiness = ReadinessAgent().evaluate(
    profile,
    gap,
    roadmap,
    projects
)

feedback = ResumeAgent().review(
    profile,
    projects,
    readiness
)

print(feedback.model_dump_json(indent=4))