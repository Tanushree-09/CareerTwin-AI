from app.services.pdf_service import PDFService

from app.agents.profile_agent import ProfileAgent
from app.agents.skill_gap_agent import SkillGapAgent
from app.agents.learning_agent import LearningAgent
from app.agents.course_agent import CourseAgent
from app.agents.project_agent import ProjectAgent
from app.agents.readiness_agent import ReadinessAgent
from app.agents.resume_agent import ResumeAgent


# STEP 1
pdf = PDFService()

resume_text = pdf.extract_text("resume.pdf")      # Change filename


# STEP 2
profile = ProfileAgent().analyze_resume(resume_text)

print("\n========== PROFILE ==========\n")
print(profile.model_dump_json(indent=4))


# STEP 3
skill_gap = SkillGapAgent().analyze(profile)

print("\n========== SKILL GAP ==========\n")
print(skill_gap.model_dump_json(indent=4))


# STEP 4
learning_plan = LearningAgent().generate(
    profile,
    skill_gap
)

print("\n========== LEARNING PLAN ==========\n")
print(learning_plan.model_dump_json(indent=4))


# STEP 5
courses = CourseAgent().recommend(profile,skill_gap)

print("\n========== COURSES ==========\n")
print(courses.model_dump_json(indent=4))


# STEP 6
projects = ProjectAgent().analyze(profile)

print("\n========== PROJECTS ==========\n")
print(projects.model_dump_json(indent=4))


# STEP 7
readiness = ReadinessAgent().evaluate(
    profile,
    skill_gap,
    learning_plan,
    projects
)

print("\n========== READINESS ==========\n")
print(readiness.model_dump_json(indent=4))


# STEP 8
resume_feedback = ResumeAgent().review(
    profile,
    projects,
    readiness
)

print("\n========== RESUME ==========\n")
print(resume_feedback.model_dump_json(indent=4))