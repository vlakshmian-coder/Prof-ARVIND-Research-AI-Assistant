import os
import json
import urllib.request
import urllib.error
import streamlit as st


OPENROUTER_MODEL = "nvidia/nemotron-3.5-lightning:free"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def ask_ollama(question, conversation_history=None):
    """Keep the existing function name so app.py does not need to change."""

    api_key = None

    try:
        api_key = st.secrets["OPENROUTER_API_KEY"]
    except Exception:
        api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        return "OpenRouter API key is not configured."

    messages = [
        {
            "role": "system",
            "content": (
                "You are Professor Arvind, an AI research assistant. "
                "Give clear, accurate explanations in simple language. "
                "Return only the final answer. Do not reveal internal reasoning "
                "or a step-by-step thinking process."
            ),
        }
    ]

    messages.extend(conversation_history or [])

    messages.append({"role": "user", "content": question})

    payload = json.dumps({
        "model": OPENROUTER_MODEL,
        "messages": messages,
    }).encode("utf-8")

    request = urllib.request.Request(
        OPENROUTER_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://prof-arvind-research-ai-assistant.streamlit.app",
            "X-Title": "Professor Arvind AI Research Assistant",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))

        return result["choices"][0]["message"]["content"]

    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        return f"OpenRouter returned HTTP {e.code}.\n{error_body}"

    except Exception as e:
        return f"OpenRouter connection error: {e}"
