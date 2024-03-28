# ReRank

- Dense Retireval is also not perfect.
- Solution: ReRank

- ReRank is trained on
  - Many queries with correct answers
  - Many queries with wrong answers

- Train a model to give
  - High scores to the good query response pairs
  - Low scores to the bad query response pairs

- Evaluating Search Models
  - Mean Average Precision (MAP)
  - Mean Reciprocal Rank (MRR)
  - Normalized Discounted Cumulative Gain (NDCG)

## Notebook

- [Jupyter Notebook](../code/L4-Rerank.ipynb)
- Cohere documentation
  - [rerank guide](https://docs.cohere.com/docs/rerank-guide)
  - [reranking](https://docs.cohere.com/docs/reranking)
- Observation:
  - `co.rerank` returns null document in my notebook unlike what is shown in the above documents.
