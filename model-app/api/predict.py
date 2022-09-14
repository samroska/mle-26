from fastapi import FastAPI, Request, Response, status
from data.objects import DataObject
from typing import List
from models.segmentation import get_prediction
import logging

app = FastAPI()


@app.post("/predict", summary="Send Data for Segmentation prediction")
async def predict(input: DataObject):
    """
    Create an DataObject with all the information:

    - data: json object

    example: {"data" : "{"x1":...}}
    """
    dataframe = get_prediction(input.data)
    return dataframe.to_json()


