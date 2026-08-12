# ==========================================================
# Project: Dynamic Knowledge Base Chatbot
# File: update_knowledge_base.py
# Author: Vijayalakshmi Narayanan
# Description:
# Automatically updates the knowledge base with new documents.
# ==========================================================

import os
import shutil

source_folder = "Project-2/new_documents"
destination_folder = "Project-2/knowledge_base"

files_added = 0
added_files = []

for filename in os.listdir(source_folder):

    if filename.endswith(".txt"):

        source = os.path.join(source_folder, filename)
        destination = os.path.join(destination_folder, filename)

        shutil.move(source, destination)

        print(f"Moved: {filename}")

        files_added += 1
        added_files.append(filename)

if files_added == 0:
    print("\nNo new documents found.")
    print("Knowledge Base is already up to date.")
else:
    print("\n===================================")
    print("Knowledge Base Updated Successfully!\n")

    print("Documents Added:")
    for file in added_files:
        print(f"• {file}")

    print(f"\nTotal Documents Added: {files_added}")
    print("Please restart AIRA to use the updated knowledge base.")
    print("===================================")