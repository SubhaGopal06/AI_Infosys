from typing import Union

from fastapi import FastAPI #type: ignore

app=FastAPI()

@app.get("/")
async def root():
    return {"API endpoints" : "Sentiment, Responses"}

@app.get("/get_sentiment")
async def read_root():
    return {"sentiment": "Positive"}

@app.get("/get_response")
async def read_item(item_id: int, q: Union[str, None]=None):
    return {"response": "Your query is resolved"}
