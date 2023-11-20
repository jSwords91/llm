from pydantic import BaseModel, Field
from enums import IntensityLevel, SentimentValues
from typing import Optional, List

class Person(BaseModel):
    """Information about a person."""
    name: str = Field(description="person's name")
    age: int = Field(description="The age of a person in years")
    profession: Optional[str] = Field(description="The profession or job of a person")


class Information(BaseModel):
    """Information to extract."""
    people: List[Person] = Field(description="List of information about people")


class KeyWord(BaseModel):
    word: str = Field(description="A keyword extracted from the text")


class Intensity(BaseModel):
    intensity: IntensityLevel = Field(description="The intensity level of the text.")


class Sentiment(BaseModel):
    sentiment: SentimentValues = Field(description="The sentiment of the text.")


class Overview(BaseModel):
    """Overview of a section of text."""

    summary: str = Field(description="A concise summary of the content.")
    sentiment: Sentiment = Field(description="The sentiment of the content.")
    keywords: List[KeyWord] = Field(description="Keywords related to the content.")
    people: List[Information] = Field(description="Information extracted about people in the text.")
    intensity: IntensityLevel = Field(description="The overall intensity of the text.")
