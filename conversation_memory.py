# ==========================================================
# Project: Multi-Modal AI Assistant
# File: conversation_memory.py
# Description:
# Stores conversation history.
# ==========================================================

class ConversationMemory:

    def __init__(self):
        self.history = []

    def add_message(self, user, assistant):
        self.history.append({
            "user": user,
            "assistant": assistant
        })

    def get_history(self):

        text = ""

        for item in self.history:

            text += (
                f"User: {item['user']}\n"
                f"AIRA: {item['assistant']}\n\n"
            )

        return text