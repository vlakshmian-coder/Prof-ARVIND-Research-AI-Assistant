import re
from collections import Counter


def summarize_text(text, max_sentences=3):
    """
    Create a simple extractive summary from a research paper abstract.
    """

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    if len(sentences) <= max_sentences:
        return text.strip()

    summary = sentences[:max_sentences]

    return " ".join(summary)


def extract_keywords(text, top_n=8):
    """
    Extract the most frequent meaningful keywords from text.
    """

    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())

    stop_words = {
        "this", "that", "with", "from", "these", "those",
        "which", "their", "using", "into", "have", "been",
        "were", "than", "such", "also", "more", "they",
        "will", "about", "between", "through", "where"
    }

    keywords = [
        word for word in words
        if word not in stop_words
    ]

    return Counter(keywords).most_common(top_n)