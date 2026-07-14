import re


class SkillVerifier:

    def verify(self, profile, repos):

        resume_skills = set(skill.lower() for skill in profile.skills)

        evidence = {}

        all_text = ""

        github_languages = set()

        for repo in repos:

            if repo["language"]:
                github_languages.add(repo["language"].lower())

            all_text += " "
            all_text += repo.get("name", "")
            all_text += " "
            all_text += repo.get("description") or ""
            all_text += " "
            all_text += " ".join(repo.get("topics", []))
            all_text += " "
            all_text += repo.get("readme", "")

        all_text = all_text.lower()

        verified = []
        unverified = []

        for skill in resume_skills:

            found = False

            # Language Match
            if skill in github_languages:
                found = True

            # README / Description / Topics Match
            elif re.search(rf"\b{re.escape(skill)}\b", all_text):
                found = True

            if found:
                verified.append(skill.title())
            else:
                unverified.append(skill.title())

        additional = []

        technology_keywords = [
            "python",
            "java",
            "javascript",
            "typescript",
            "php",
            "c",
            "c++",
            "c#",
            "sql",
            "mysql",
            "mongodb",
            "postgresql",
            "tensorflow",
            "pytorch",
            "keras",
            "scikit-learn",
            "opencv",
            "flask",
            "django",
            "fastapi",
            "react",
            "node",
            "express",
            "docker",
            "kubernetes",
            "aws",
            "azure",
            "gcp",
            "firebase",
            "git",
            "github",
            "linux",
            "numpy",
            "pandas",
            "matplotlib",
            "seaborn",
            "langchain",
            "langgraph",
            "gemini"
        ]

        for tech in technology_keywords:

            if re.search(rf"\b{re.escape(tech)}\b", all_text):

                if tech not in resume_skills:

                    additional.append(tech.title())

        return {

            "verified_skills": sorted(verified),

            "unverified_skills": sorted(unverified),

            "additional_detected_skills": sorted(list(set(additional)))

        }