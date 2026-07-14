from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
import tempfile
import os

from app.services.pdf_parser import PDFParser
from app.services.github_service import GitHubService
from app.services.skill_verifier import SkillVerifier

from app.agents.profile_agent import ProfileAgent
from app.agents.skill_gap_agent import SkillGapAgent
from app.agents.course_agent import CourseAgent
from app.agents.roadmap_agent import RoadmapAgent
from app.agents.project_analysis_agent import ProjectAnalysisAgent
from app.agents.resume_feedback_agent import ResumeFeedbackAgent
from app.agents.career_readiness_agent import CareerReadinessAgent

router = APIRouter()


@router.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    github: str = Form(...),
    career_goal: str = Form(...),
    timeline: str = Form(...)
):

    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:

        temp.write(await resume.read())

        pdf_path = temp.name

    # Extract resume text
    resume_text = PDFParser().extract_text(pdf_path)

    os.remove(pdf_path)

    # Profile Analysis
    profile = ProfileAgent().analyze_resume(resume_text)

    # Override career goal from UI
    profile.career_goal = career_goal

    # GitHub
    github_service = GitHubService()

    repos = github_service.get_repositories(github)

    summary = github_service.analyze_profile(github)

    # Skill Verification
    verification = SkillVerifier().verify(
        profile.skills,
        repos
    )

    # Skill Gap
    skill_gap = SkillGapAgent().analyze(profile)

    # Courses
    courses = CourseAgent().recommend(
        profile,
        skill_gap
    )

    # Roadmap
    roadmap = RoadmapAgent().generate(
        profile,
        skill_gap
    )

    # Projects
    project_analysis = ProjectAnalysisAgent().analyze(profile)

    # Resume Feedback
    resume_feedback = ResumeFeedbackAgent().review(profile)

    # Career Readiness
    career = CareerReadinessAgent().evaluate(
        profile,
        skill_gap,
        project_analysis
    )

    return JSONResponse({

        "profile": profile.model_dump(),

        "github": summary,

        "verification": verification,

        "skill_gap": skill_gap,

        "courses": courses,

        "roadmap": roadmap,

        "projects": project_analysis,

        "resume_feedback": resume_feedback,

        "career": career,

        "timeline": timeline

    })