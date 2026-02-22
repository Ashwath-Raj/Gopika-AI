import subprocess
import uuid
from pathlib import Path

MODEL_PATH = "models/en_US-lessac-medium.onnx"

OUTPUT_DIR = Path("tts_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def synthesize(text: str):
    output_file = OUTPUT_DIR / f"{uuid.uuid4()}.wav"

    process = subprocess.Popen(
        [
            "piper",
            "--model", MODEL_PATH,
            "--output_file", str(output_file)
        ],
        stdin=subprocess.PIPE
    )

    process.communicate(input=text.encode("utf-8"))

    return str(output_file)
