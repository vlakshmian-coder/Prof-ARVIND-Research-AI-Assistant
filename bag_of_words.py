# ==========================================================
# Project: Dynamic Knowledge Base Chatbot
# File: bag_of_words.py
# Author: Vijayalakshmi Narayanan
# Description:
# Demonstrates the Bag of Words text representation.
# ==========================================================

from sklearn.feature_extraction.text import CountVectorizer

# Sample sentences
sentences = [
    "I love Python",
    "Python is easy",
    "I love AI"
]

# Create the vectorizer
vectorizer = CountVectorizer()

# Learn the vocabulary and create the matrix
X = vectorizer.fit_transform(sentences)

# Print the vocabulary
print("Vocabulary:")
print(vectorizer.get_feature_names_out())

# Print the Bag of Words matrix
print("\nBag of Words Matrix:")
print(X.toarray())