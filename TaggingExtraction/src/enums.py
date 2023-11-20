
from enum import Enum

class IntensityLevel(int, Enum):
    low = 1
    medium = 2
    high = 3

class SentimentValues(str, Enum):
    negative = "Negative"
    neutral = "Neutral"
    positive = "Positive"
