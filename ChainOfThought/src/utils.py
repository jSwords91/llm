from typing import TypeVar

import instructor
from openai import OpenAI

T = TypeVar("T")

client = instructor.patch(OpenAI())

def model_query(
    pydantic_class: T, system_prompt: str, query: str, model="gpt-3.5-turbo"
) -> T:
    return client.chat.completions.create(
        model=model,
        response_model=pydantic_class,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {"role": "user", "content": query},
        ],
    )
