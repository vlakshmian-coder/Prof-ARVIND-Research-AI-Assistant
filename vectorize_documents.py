# ==========================================================
# Project: Dynamic Knowledge Base Chatbot
# File: vectorize_documents.py
# Author: Vijayalakshmi Narayanan
# Description:
# Converts the knowledge base into TF-IDF vectors.
# ==========================================================

import os
from sklearn.feature_extraction.text import TfidfVectorizer

# Folder containing documents
folder_path = "Project-2/knowledge_base"

documents = []
filenames = []

# Read all text files
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            documents.append(file.read())
            filenames.append(filename)

# Convert to TF-IDF vectors
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(documents)

print("Documents Loaded:")
print(filenames)

print("\nVocabulary:")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(X.toarray())