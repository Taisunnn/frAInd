from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from app.friend import get_response
from app.friend import get_voice


app = FastAPI()

@app.get("/")
def index():
    return {"Status": "Healthy"}

@app.get("/get_response")
def send_message(human_input: str):
    message = get_response(human_input)
    return message