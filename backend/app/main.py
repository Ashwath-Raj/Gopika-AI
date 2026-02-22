from app.services.llm_service import generate_full_response
from app.services.tts_service import synthesize
from fastapi import UploadFile, File
from app.services.stt_service import transcribe
import tempfile
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from app.services.llm_service import stream_llm_response

app = FastAPI()
app.mount("/tts_outputs", StaticFiles(directory="tts_outputs"), name="tts_outputs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp_path = tmp.name

    text = transcribe(tmp_path)
    return {"text": text}

@app.post("/speak")
def speak(request: ChatRequest):
    audio_path = synthesize(request.prompt)
    return {"audio": audio_path}
@app.post("/voice-chat")
async def voice_chat(file: UploadFile = File(...)):
    # Save uploaded audio temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp_path = tmp.name

    # 1. Transcribe
    user_text = transcribe(tmp_path)

    # 2. Generate LLM response
    ai_text = generate_full_response(user_text)

    # 3. Convert to speech
    audio_path = synthesize(ai_text)

    return {
        "transcription": user_text,
        "response_text": ai_text,
        "response_audio": audio_path
    }
