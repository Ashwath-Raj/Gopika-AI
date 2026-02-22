import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:8b-instruct-q4_K_M"



def stream_llm_response(prompt: str):
    with requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": True
        },
        stream=True,
    ) as r:

        for line in r.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                chunk = data.get("response", "")
                yield chunk



def generate_full_response(prompt: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": f"You are GOPIKA, a helpful multilingual farm assistant. Speak warmly and clearly.\nUser: {prompt}\nAssistant:",
            "stream": False
        }
    )

    data = response.json()
    return data.get("response", "").strip()
