from enum import Enum

class Label(str, Enum):
    BILLING = "billing"
    OPERATIONS = "operations"
    SALES = "sales"
    COMPLAINTS = "complaint"
    GENERAL_QUERY = "general_query"
