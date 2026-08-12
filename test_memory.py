from conversation_memory import ConversationMemory

memory = ConversationMemory()

memory.add_message(
    "What is Python?",
    "Python is a programming language."
)

memory.add_message(
    "What is LangChain?",
    "LangChain helps build AI applications."
)

print(memory.get_history())