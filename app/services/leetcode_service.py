import pandas as pd


class LeetCodeService:

    def __init__(self):
        self.df = pd.read_csv("data/leetcode_clean.csv")

        self.skill_mapping = {

            "Problem Solving": [
                "Array",
                "Hash Table",
                "Two Pointers",
                "Sorting"
            ],

            "Data Structures": [
                "Array",
                "Linked List",
                "Stack",
                "Queue",
                "Tree",
                "Graph"
            ],

            "Algorithms": [
                "Binary Search",
                "Greedy",
                "Dynamic Programming",
                "Backtracking"
            ],

            "Machine Learning": [
                "Heap",
                "Sorting"
            ],

            "Backend Development": [
                "Hash Table",
                "Graph",
                "Heap"
            ],

            "Database": [
                "Database"
            ],

            "SQL": [
                "Database"
            ],

            "System Design": [
                "Design"
            ],

            "REST API": [
                "Design"
            ],

            "Cloud Computing": [
                "Graph",
                "Heap"
            ],

            "Docker": [
                "Design"
            ],

            "FastAPI": [
                "Design"
            ]
        }

    def get_problems_by_topics(self, skills):

        topics = set()

        for skill in skills:

            if skill in self.skill_mapping:

                topics.update(
                    self.skill_mapping[skill]
                )

        if not topics:

            topics = {
                "Array",
                "Hash Table",
                "Dynamic Programming"
            }

        filtered = self.df[
            self.df["topics"].fillna("").apply(
                lambda x: any(
                    topic.lower() in x.lower()
                    for topic in topics
                )
            )
        ]

        return filtered