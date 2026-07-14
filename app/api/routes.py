from app.agents.profile_agent import ProfileAgent
from app.agents.skill_gap_agent import SkillGapAgent
from app.agents.course_agent import CourseAgent
from app.agents.learning_agent import LearningAgent
from app.agents.project_agent import ProjectAgent
from app.agents.readiness_agent import ReadinessAgent
from app.agents.resume_agent import ResumeAgent
from app.agents.leetcode_agent import LeetCodeAgent

from app.services.github_service import GitHubService
from app.services.skill_verifier import SkillVerifier
from app.services.pdf_service import PDFService
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
import tempfile
import os
router = APIRouter()
@router.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    github: str = Form(...),
    career_goal: str = Form(...),
    timeline: str = Form(...)
):

    # -----------------------------
    # Save uploaded PDF
    # -----------------------------

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:

        temp.write(await resume.read())

        pdf_path = temp.name

    # -----------------------------
    # Resume Parsing
    # -----------------------------

    resume_text = PDFService().extract_text(pdf_path)

    os.remove(pdf_path)

    # -----------------------------
    # Profile Analysis
    # -----------------------------

    profile = ProfileAgent().analyze_resume(resume_text)

    # Override career goal selected in UI
    profile.career_goal = career_goal

    # -----------------------------
    # GitHub Analysis
    # -----------------------------

    github_service = GitHubService()

    repos = github_service.get_repositories(github)

    github_summary = github_service.analyze_profile(github)

    # -----------------------------
    # Skill Verification
    # -----------------------------

    verification = SkillVerifier().verify(
        profile,
        repos
    )

    # -----------------------------
    # Skill Gap
    # -----------------------------

    skill_gap = SkillGapAgent().analyze(profile)

    # -----------------------------
    # LeetCode Recommendation
    # -----------------------------

    leetcode = LeetCodeAgent().recommend(skill_gap)
    print(leetcode)
    # -----------------------------
    # Course Recommendation
    # -----------------------------

    courses = CourseAgent().recommend(
        profile,
        skill_gap
    )

    # -----------------------------
    # Learning Roadmap
    # -----------------------------

    roadmap = LearningAgent().generate(
        profile,
        skill_gap, timeline
    )

    # -----------------------------
    # Project Analysis
    # -----------------------------

    repos = github_service.get_repositories(github)

    project_analysis = ProjectAgent().analyze(
        profile,
        repos
    )

    # -----------------------------
    # Career Readiness
    # -----------------------------

    readiness = ReadinessAgent().evaluate(
        profile,
        skill_gap,
        roadmap,
        project_analysis
    )

    # -----------------------------
    # Resume Feedback
    # -----------------------------

    resume_feedback = ResumeAgent().review(
        profile,
        project_analysis,
        readiness
    )

    # -----------------------------
    # Final Response
    # -----------------------------

    return JSONResponse({

        "profile": profile.model_dump(),

        "github": github_summary,

        "verification": verification,

        "skill_gap": skill_gap.model_dump(),

        "leetcode": leetcode,

        "courses": courses.model_dump(),

        "roadmap": roadmap.model_dump(),

        "projects": project_analysis.model_dump(),

        "career": readiness.model_dump(),

        "resume_feedback": resume_feedback.model_dump(),

        "timeline": timeline

    })