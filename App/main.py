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
    
# INFO:     Will watch for changes in these directories: ['C:\\Users\\G subhashini\\OneDrive\\Certificates.subha\\Projects\\Infosys-intern-5.0\\AI_infosys\\App']
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [50328] using WatchFiles
# INFO:     Started server process [49124]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.
