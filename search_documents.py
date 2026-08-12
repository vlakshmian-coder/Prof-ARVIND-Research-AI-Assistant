# ==========================================================
# Project: Dynamic Knowledge Base Chatbot
# File: search_documents.py
# Author: Vijayalakshmi Narayanan
# Description:
# Searches the knowledge base using TF-IDF and cosine
# similarity to find the most relevant document.
# ==========================================================


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from load_medquad import load_medquad

# Load MedQuAD dataset
medical_data = load_medquad()

questions = []
answers = []
sources = []

for item in medical_data:
    questions.append(item["question"])
    answers.append(item["answer"])
    sources.append(item["source"])

print(f"\nLoaded {len(questions)} medical questions.\n")

vectorizer = TfidfVectorizer(
    stop_words="english",
    lowercase=True
)

question_vectors = vectorizer.fit_transform(questions)

# Function to search the knowledge base
def search_knowledge_base(query):

    query_vector = vectorizer.transform([query])

    similarity = cosine_similarity(query_vector, question_vectors)

    best_match = similarity.argmax()

    best_score = similarity[0][best_match]

    print(f"\nBest Match: {questions[best_match]}")
    print(f"Best Score: {best_score:.4f}")

    # Minimum similarity required
    if best_score < 0.20:
        return (
            "No matching document",
            "Sorry, I couldn't find an answer in my knowledge base.\n"
            "Please try asking about AI, Python, Machine Learning, "
            "Deep Learning, or another topic available in the knowledge base.",
            best_score
        )

    return (
        sources[best_match],
        answers[best_match],
        best_score
)


