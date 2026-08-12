def detect_sentiment(text):

    text = text.lower()

    positive_words = [
        "happy",
        "good",
        "great",
        "excellent",
        "awesome",
        "love",
        "thanks",
        "thank you",
        "wonderful"
    ]

    negative_words = [
        "sad",
        "bad",
        "angry",
        "frustrated",
        "upset",
        "hate",
        "terrible",
        "worst",
        "problem"
    ]

    for word in positive_words:
        if word in text:
            return "Positive"

    for word in negative_words:
        if word in text:
            return "Negative"

    return "Neutral"