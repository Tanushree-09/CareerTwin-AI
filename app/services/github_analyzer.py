from collections import Counter


class GitHubAnalyzer:

    def analyze(self, repos):

        total_repos = len(repos)

        languages = []
        readme_count = 0
        stars = 0
        forks = 0

        recent_projects = []

        for repo in repos:

            if repo["language"]:
                languages.append(repo["language"])

            if repo["readme"] != "No README available.":
                readme_count += 1

            stars += repo["stars"]
            forks += repo["forks"]

            recent_projects.append({
                "name": repo["name"],
                "updated_at": repo["updated_at"]
            })

        language_count = Counter(languages)

        return {

            "total_repositories": total_repos,

            "languages": dict(language_count),

            "readme_coverage": f"{readme_count}/{total_repos}",

            "total_stars": stars,

            "total_forks": forks,

            "recent_projects": recent_projects

        }