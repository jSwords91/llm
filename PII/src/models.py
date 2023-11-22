from pydantic import BaseModel, Field
from typing import List

class Data(BaseModel):
    index: int
    data_type: str = Field(description="The type of the PII value found")
    pii_value: str = Field(description="The PII value found")


class PIIData(BaseModel):
    """
    Extracted PII data from a document, all data_type values should try to have consistent property names
    """

    pii_data: List[Data] = Field(
        description="A list of the PII data found in the document"
    )

    def scrub_data(self, content: str):
        """
        Iterates over the private data and replaces the value with a placeholder in the form of
        <{data_type}_{i}>
        """

        for i, data in enumerate(self.pii_data):
            content = content.replace(data.pii_value, f"<{data.data_type}_{i}>")

        return content