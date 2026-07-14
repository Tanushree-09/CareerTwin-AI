from app.services.github_service import GitHubService
from app.services.github_analyzer import GitHubAnalyzer
from app.services.skill_verifier import SkillVerifier

from app.agents.profile_agent import ProfileAgent
from app.services.pdf_service import PDFService

import json

username = input("GitHub Username: ")

pdf = PDFService()

resume = pdf.extract_text("resume.pdf")

profile = ProfileAgent().analyze_resume(resume)

github = GitHubService()

repos = github.get_repositories(username)

for repo in repos:
    repo["readme"] = github.get_readme(
        username,
        repo["name"]
    )[:3000]

analysis = GitHubAnalyzer().analyze(repos)

result = SkillVerifier().verify(
    profile,
    repos
)

print(json.dumps(result, indent=4))