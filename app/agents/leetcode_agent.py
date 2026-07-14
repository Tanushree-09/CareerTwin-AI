from app.services.leetcode_service import LeetCodeService


class LeetCodeAgent:

    def __init__(self):
        self.service = LeetCodeService()

    def recommend(self, skill_gap):

        problems = self.service.get_problems_by_topics(
            skill_gap.priority_skills
        )

        recommendations = []

        for _, row in problems.head(10).iterrows():

            recommendations.append({

                "title": row["title"],
                "difficulty": row["difficulty"],
                "topic": row["topics"],
                "problem_link": row["url"],
                "solution_link": row["solution_code_url"]
                if row["solution_code_url"] else None

            })

        return recommendations