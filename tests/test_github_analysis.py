from app.services.github_service import GitHubService
from app.services.github_analyzer import GitHubAnalyzer
import json

github = GitHubService()
analyzer = GitHubAnalyzer()

username = input("GitHub Username: ")

repos = github.get_repositories(username)

for repo in repos:
    repo["readme"] = github.get_readme(
        username,
        repo["name"]
    )[:3000]

analysis = analyzer.analyze(repos)

print(json.dumps(analysis, indent=4))