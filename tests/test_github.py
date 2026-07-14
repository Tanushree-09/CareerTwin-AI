from app.services.github_service import GitHubService

github = GitHubService()

username = input("GitHub Username: ")

user = github.get_user(username)

print("\n===== USER =====\n")

print(user["name"])
print(user["public_repos"])
print(user["followers"])

repos = github.get_repositories(username)

print("\n===== REPOSITORIES =====\n")

for repo in repos:

    print("=" * 60)

    print("Repository :", repo["name"])
    print("Description:", repo["description"])
    print("Language   :", repo["language"])
    print("Stars      :", repo["stars"])
    print("Forks      :", repo["forks"])
    print("Topics     :", repo["topics"])
    print("Updated    :", repo["updated_at"])
    print("URL        :", repo["url"])
    readme = github.get_readme(
        username,
        repo["name"]
    )

    print("\nREADME Preview\n")

    print(readme[:1000])     # first 1000 characters