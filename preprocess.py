# ==========================================================
# Project: Dynamic Knowledge Base Chatbot
# File: preprocess.py
# Author: Vijayalakshmi Narayanan
# Description:
# Performs basic text preprocessing for NLP.
# ==========================================================

import string
import nltk
from nltk.corpus import stopwords

# Download stopwords (only needed the first time)
nltk.download('stopwords')

text = "Hello, Welcome to NLP! This is my first AI project."

print("Original Text:", text)

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Tokenization
words = text.split()

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

print("Processed Text:", text)
print("Words:", words)
print("Filtered Words:", filtered_words)