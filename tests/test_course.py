from app.agents.profile_agent import ProfileAgent
from app.agents.skill_gap_agent import SkillGapAgent
from app.agents.course_agent import CourseAgent

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

courses = CourseAgent().recommend(profile, gap)

print(courses.model_dump_json(indent=4))