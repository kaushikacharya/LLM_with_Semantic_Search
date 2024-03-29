# Keyword Search

## Notebook

- [Jupyter Notebook](../code/L1-Keyword_Search.ipynb)
- We will connect to remote [Weaviate vector database](https://weaviate.io/developers/weaviate).
- Each row contains a passage in Wikipedia.
- Total records: 10 million
- Algorithm used: BM25
- Libraries used:
  - [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Cohere API keys](https://dashboard.cohere.com/api-keys)

## Search at a high level

- Components
  - Query
  - Search System
  - Document Archive
  - Results

- Search System stages:
  - 1st stage: Retrieval
    - Commonly uses BM25 algorithm to score the documents in the archive versus the query.
    - Utilizes inverted index
      - For each keyword, corresponding Document IDs are stored along with the word frequency in the document.
  - 2nd stage: Reranking
    - Often needed to involve or include additional signals rather than just text relevance.

- Limitation of keyword matching
  - No shared keywords
  - Language models can overcome this limitation because they're not comparing keywords simply. They look at the general meaning.

- Language models can improve both search stages.
