from tokenize import Double
from pydantic import BaseModel, Json
from typing import Any

class DataObject(BaseModel):
    data: Json[Any]


class OutputObject(BaseModel):
    probability: Double
    
