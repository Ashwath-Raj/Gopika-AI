from faster_whisper import WhisperModel

model = WhisperModel(
    "base",
    device="cuda",
    compute_type="float16"
)

def transcribe(audio_path: str):
    segments, info = model.transcribe(
        audio_path,
        task="translate"   # Forces output in English
    )

    full_text = ""
    for segment in segments:
        full_text += segment.text

    return full_text.strip()
