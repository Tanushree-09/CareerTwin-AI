from app.agents.base_agent import BaseAgent
from app.core.prompts import PROJECT_ANALYSIS_PROMPT
from app.models.project_analysis import ProjectAnalysis


class ProjectAgent(BaseAgent):

    def analyze(self, profile, repositories):

        repo_text = ""

        for repo in repositories:

            repo_text += f"""
Repository Name: {repo['name']}
Description: {repo['description']}
Language: {repo['language']}
Stars: {repo['stars']}
Forks: {repo['forks']}
Topics: {", ".join(repo['topics'])}
Repository URL: {repo['url']}
Last Updated: {repo['updated_at']}
"""

        prompt = f"""
{PROJECT_ANALYSIS_PROMPT}

Student Name:
{profile.name}

Career Goal:
{profile.career_goal}

Skills:
{", ".join(profile.skills)}

GitHub Repositories:

{repo_text}
"""

        data = self.invoke(prompt)

        return ProjectAnalysis(**data)