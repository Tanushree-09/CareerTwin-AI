import json

from app.core.llm import get_llm


class BaseAgent:

    def __init__(self):
        self.llm = get_llm()

    def invoke(self, prompt: str):

        response = self.llm.invoke(prompt)

        if isinstance(response.content, list):
            text = "".join(
                item.get("text", "")
                for item in response.content
                if isinstance(item, dict)
            )
        else:
            text = str(response.content)

        return json.loads(text)