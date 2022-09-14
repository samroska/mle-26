from pydantic import BaseModel, Json, validator
from typing import Any, List

class DataObject(BaseModel):
    data: Json[Any]

    @validator('data')
    def check_data_field(cls, v, values):
        if v is not None and values['data'] is not None:
            raise ValueError('must not provide both data and error')
        if v is None and values.get('data') is None:
            raise ValueError('must provide data or error')
        return v
