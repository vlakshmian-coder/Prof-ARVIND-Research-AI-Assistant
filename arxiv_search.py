import json
from pathlib import Path


# arXiv dataset stored outside the GitHub project
ARXIV_PATH = Path(
    r"C:\AI_Datasets\arXiv\archive\arxiv-metadata-oai-snapshot.json"
)


def search_arxiv(query, max_results=5):
    """
    Search arXiv metadata for papers matching a query
    in the title, abstract, or categories.
    """

    query = query.lower().strip()
    results = []

    if not query:
        return results

    with open(ARXIV_PATH, "r", encoding="utf-8") as file:

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

            if query in searchable_text:

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