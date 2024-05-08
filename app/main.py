import io

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from app.friend import get_response
from app.friend import get_voice


app = FastAPI()

@app.get("/")
def index():
    return {"Status": "Healthy"}

@app.get("/message")
def send_message(human_input: str):
    message = get_response(human_input)
    voice = get_voice(message)
    return StreamingResponse(io.BytesIO(voice), media_type="audio/mpeg")