from langchain.prompts import ChatPromptTemplate

from typing import Dict

class Chain:
    def __init__(self, chain) -> None:
        self.chain = chain

    def run(self, input: str) -> Dict:
        return (
            self.chain.invoke({"input": input})
        )

def build_prompt(template: str) -> ChatPromptTemplate:
    return (
        ChatPromptTemplate.from_messages([("system", template), ("human", "{input}")])
    )