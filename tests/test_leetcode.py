from app.services.leetcode_service import LeetCodeService

service = LeetCodeService()

skills = [
    "Array",
    "Dynamic Programming",
    "Graph"
]

problems = service.get_problems_by_topics(skills)

print(problems[["title", "difficulty", "topics"]].head(10))