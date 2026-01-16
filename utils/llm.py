import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile"


def call_llm(prompt, temperature=0.8):
    if not GROQ_API_KEY:
        raise RuntimeError("❌ GROQ_API_KEY missing in .env")

    response = requests.post(
        GROQ_URL,
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a savage Indian stand-up comedian. Roast but keep it funny."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": temperature,
        },
        timeout=60
    )

    data = response.json()

    # 🔥 ERROR HANDLING (THIS FIXES YOUR CRASH)
    if "error" in data:
        raise RuntimeError(f"GROQ ERROR: {data['error']['message']}")

    if "choices" not in data:
        raise RuntimeError(f"Unexpected response: {data}")

    return data["choices"][0]["message"]["content"]
