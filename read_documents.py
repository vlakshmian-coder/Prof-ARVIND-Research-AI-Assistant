# ==========================================================
# Project: Dynamic Knowledge Base Chatbot
# File: read_documents.py
# Author: Vijayalakshmi Narayanan
# Description:
# Reads all text documents from the knowledge base.
# ==========================================================

import os

current_folder = os.getcwd()
print(current_folder)

folder_path = os.path.join(current_folder, "knowledge_base")

# Path to the knowledge_base folder
folder_path = "Project-1/knowledge_base"

# Read every text file
for filename in os.listdir(folder_path):

    if filename.endswith(".txt"):

        file_path = os.path.join(folder_path, filename)

        print("=" * 40)
        print("Reading:", filename)
        print("=" * 40)

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        print(content)
        print("\n")