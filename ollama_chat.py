import ollama


def ask_ollama(question, conversation_history=None):

    messages = list(conversation_history or [])

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )

    return response["message"]["content"]