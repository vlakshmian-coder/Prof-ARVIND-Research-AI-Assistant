# ==========================================================
# Project: Dynamic Knowledge Base Chatbot
# File: tfidf.py
# Author: Vijayalakshmi Narayanan
# Description:
# Demonstrates TF-IDF vectorization of text documents.
# ==========================================================

from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I love Python programming",
    "Python is easy to learn",
    "AI uses Python",
    "Machine learning uses AI"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(documents)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(X.toarray())