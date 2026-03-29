import os
import httpx
import json

from collections.abc import Generator

OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

def call_ollama(prompt: str) -> Generator[str, None, None]:
    with httpx.stream(
        "POST",
        f"{OLLAMA_URL}/api/generate",
        json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": True},
        timeout=httpx.Timeout(connect=30.0, read=None, write=None, pool=None),
    ) as response:
        response.raise_for_status()

        for line in response.iter_lines():
            if not line:
                continue

            chunk = json.loads(line)
            yield chunk.get("response", "")

            if chunk.get("done"):
                break