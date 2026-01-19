import requests

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

def ask_ollama(prompt: str) -> str:
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    res = requests.post(OLLAMA_URL, json=payload, timeout=120)
    res.raise_for_status()  # <-- quan trọng
    return res.json().get("response", "")
