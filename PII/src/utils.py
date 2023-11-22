from typing import TypeVar

import instructor
from openai import OpenAI

from PyPDF2 import PdfReader

T = TypeVar("T")

client = instructor.patch(OpenAI())


def read_pdf(filepath: str) -> str:
    """Takes a filepath to a PDF and returns a string of the PDF's contents"""
    reader = PdfReader(filepath)
    pdf_text = ""
    page_number = 0
    for page in reader.pages:
        page_number += 1
        pdf_text += page.extract_text() + f"\nPage Number: {page_number}"
    return pdf_text


def model_query(
    pydantic_class: T, system_prompt: str, query: str, model="gpt-3.5-turbo"
) -> T:
    queries = client.chat.completions.create(
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
    return queries