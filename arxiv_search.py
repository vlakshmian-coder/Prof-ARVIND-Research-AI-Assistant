import json
import gzip
from pathlib import Path    


# arXiv dataset stored outside the GitHub project
ARXIV_PATH = Path(__file__).parent / "data" / "arxiv_cs_deployment.json.gz"


def search_arxiv(query, max_results=5):
    """
    Search arXiv metadata for papers matching a query
    in the title, abstract, or categories.
    """

    query = query.lower().strip()
    results = []

    if not query:
        return results

    # Use the important words from a natural-language question
    # instead of requiring the complete sentence to appear in a paper.
    stop_words = {
        "what", "is", "are", "the", "a", "an", "of", "in", "on",
        "to", "for", "and", "or", "can", "you", "explain", "tell",
        "me", "about", "how", "does", "do", "why", "please"
    }

    query_words = [
        word.strip(".,?!:;()[]{}")
        for word in query.split()
        if word.strip(".,?!:;()[]{}") not in stop_words
    ]

    if not query_words:
        query_words = query.split()

    with gzip.open(ARXIV_PATH, "rt", encoding="utf-8") as file:

        for line in file:

            if not line.strip():
                continue

            paper = json.loads(line)

            title = paper.get("title", "")
            abstract = paper.get("abstract", "")
            categories = paper.get("categories", "")

            if not any(category.startswith("cs.") for category in categories.split()):
                continue

            searchable_text = (
                title + " " + abstract + " " + categories
            ).lower()

            if all(word in searchable_text for word in query_words):

                results.append(
                    {
                        "id": paper.get("id", ""),
                        "title": " ".join(title.split()),
                        "authors": paper.get("authors", ""),
                        "categories": categories,
                        "abstract": " ".join(abstract.split()),
                    }
                )

                if len(results) >= max_results:
                    break

    return results