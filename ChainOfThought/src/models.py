from pydantic import BaseModel, Field
from typing import List

from src.enums import Label

class MultiClassPrediction(BaseModel):
    predicted_labels: List[Label] = Field(description="The relevant labels assigned to the content. There may be multiple relevant labels to add.")
    chain_of_thought: str = Field(description="Think step-by-step in order to arrive at an answer.")