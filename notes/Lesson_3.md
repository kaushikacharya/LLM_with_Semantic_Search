# Dense Retrieval

- This lesson contains the following two parts:
  - Vector search using the embeddings
  - Build a vector index from scratch
    - Build a vector search database

- Two main ways of doing semantic search
  - Using properties of similarity and distance into search
  - Re-rankers

## ANN vector search vs Vector databases

- Approximate Nearest-Neighbor Vector search libraries
  - Annoy (from Spotify)
  - FAISS (from Facebook)
  - ScaNN (from Google)

- Vector Databases
  - Weaviate
  - PostgreSQL (extensions support vector database)
  - Qdrant
  - Vespa
  - Pinecone
  - Chroma

- ANN vector search library features
  - Easy to set up
  - Store vectors only

- Vector databases features
  - Store vectors and text
  - Easier to update (add new vectors)
    - ANN vector search library would require to reindex the vectors
  - Allow filtering and more advanced queries
    - Example: filtering by language as shown in the notebook

## Hybrid Search: Keyword + Vector

- Combines
  - Keyword search
  - Vector search
    - `co.embed()`
  - Other signals
    - Example: Google's PageRank algorithm assigns an authority score to various web pages and websites based on how many other pages link to them.
    - Search engines have tens, hundreds and sometimes thousands of signals that feed into the decision of how they order the search results.

- Next lesson:
  - Text Relevance Reranker
    - `co.rerank()`

## Learn more

- [Pretrained Transformers for Text Ranking: BERT and Beyond](https://direct.mit.edu/coli/article/49/1/253/113643/Pretrained-Transformers-for-Text-Ranking-BERT-and)
  - This textbook and paper describes the development of dense retrieval over the last few years.

## Notebook

- [Jupyter Notebook](../code/L3-Dense_Retrieval.ipynb)
- In a cleaner text like the one used here, splitting of sentences can be done using `.`. But in real-world scenarios it might require complicated approach.
- [Annoy Python APIs](https://github.com/spotify/annoy#full-python-api)
