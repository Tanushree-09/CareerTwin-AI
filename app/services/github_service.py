import requests
import base64

class GitHubService:

    BASE_URL = "https://api.github.com"

    def get_user(self, username):

        response = requests.get(f"{self.BASE_URL}/users/{username}")
        response.raise_for_status()

        return response.json()


    def get_repositories(self, username):

        response = requests.get(f"{self.BASE_URL}/users/{username}/repos")
        response.raise_for_status()

        repos = response.json()

        repo_data = []

        for repo in repos:

            repo_data.append({
                "name": repo["name"],
                "description": repo["description"],
                "language": repo["language"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
                "topics": repo.get("topics", []),
                "url": repo["html_url"],
                "updated_at": repo["updated_at"],
                "default_branch": repo["default_branch"]
            })

        return repo_data
    def get_readme(self, username, repo_name):

        url = f"{self.BASE_URL}/repos/{username}/{repo_name}/readme"

        response = requests.get(url)

        if response.status_code != 200:
            return "No README available."

        data = response.json()

        content = base64.b64decode(data["content"]).decode("utf-8")
        return content
    def analyze_profile(self, username):

        repos = self.get_repositories(username)

        user = self.get_user(username)

        languages = {}

        total_stars = 0
        total_forks = 0
        readme_count = 0

        recent_projects = []

        for repo in repos:

            if repo["language"]:
                languages[repo["language"]] = (
                    languages.get(repo["language"], 0) + 1
                )

            total_stars += repo["stars"]
            total_forks += repo["forks"]

            if repo.get("readme"):
                readme_count += 1

            recent_projects.append({
                "name": repo["name"],
                "updated_at": repo["updated_at"]
            })

        return {

            "total_repositories": user["public_repos"],

            "languages": languages,

            "readme_coverage": f"{readme_count}/{len(repos)}",

            "total_stars": total_stars,

            "total_forks": total_forks,

            "recent_projects": recent_projects,

            "profile_url": user["html_url"]

        }
        