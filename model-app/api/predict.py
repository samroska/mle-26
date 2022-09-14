from fastapi import FastAPI, Request, Response, status
from fastapi.encoders import jsonable_encoder
from data.objects import DataObject, DataList
from pydantic import ValidationError
from models.segmentation import get_prediction
import logging

app = FastAPI()


@app.post("/predict", summary="Send Data for Segmentation prediction")
async def predict(input: Request):
    req_body = await input.body()
    try:
        obj = DataObject (data=req_body)
        dataframe = get_prediction(obj)
        return Response(content=dataframe.to_json, media_type="application/json", status=status.HTTP_200_OK)
    except ValidationError as e:
        logging.error(e.errors)
        return status.HTTP_400_BAD_REQUEST

    

    
@app.post("/predict/batch", summary="Send Batch Data for Segmentation prediction")
async def predict(input: Request):
    req_body = await input.body()
    try:
        obj = DataObject (data=req_body)
        get_prediction(obj)
        return status.HTTP_200_OK
    except ValidationError as e:
        logging.error(e)
        return status.HTTP_400_BAD_REQUEST


