from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.services.llm_service import stream_llm_response

app = FastAPI()


class ChatRequest(BaseModel):
    prompt: str


@app.get("/")
def root():
    return {"status": "GOPIKA backend running"}


@app.post("/chat")
def chat(request: ChatRequest):
    return StreamingResponse(
        stream_llm_response(request.prompt),
        media_type="text/plain"
    )
