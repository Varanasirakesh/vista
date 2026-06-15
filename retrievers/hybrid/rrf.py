""" Reciprocal Rank Fusion 
    the RRF algorithm takes the top k results from each retriever and combines them into a single ranked list of results
    the RRF algorithm is based on the idea that if a document is ranked highly by multiple retrievers, it is likely to be relevant to the query
    the RRF algorithm is a simple and effective way to combine the results of multiple retrievers
    
    RRF Approach:
        RRF(d)=∑r∈R​(1/k+r(d)1)​
        k = smoothing constant
        r(d) = rank of document d

    example: 
    DENSE: 
        A → Rank 1
        B → Rank 2
        C → Rank 3
    BM25:
        C → Rank 1
        A → Rank 2
        F → Rank 3
    scores:
    A = 1/61 + 1/62
    B = 1/62
    C = 1/63 + 1/61
    F = 1/63

    Thus final ranking is:
    A
    C
    B
    F
    """

from collections import defaultdict


class ReciprocalRankFusion:

    def __init__(
        self,
        k: int = 60,
    ):
        self.k = k

    def fuse(
        self,
        dense_results,
        sparse_results,
    ):
        scores = defaultdict(float)
        documents = {}

        # Dense retrieval results
        for rank, result in enumerate(
            dense_results,
            start=1,
        ):
            key = result.payload["chunk_id"]

            scores[key] += (
                1 / (self.k + rank)
            )

            documents[key] = result

        # Sparse retrieval results
        for rank, result in enumerate(
            sparse_results,
            start=1,
        ):
            key = result["chunk_id"]

            scores[key] += (
                1 / (self.k + rank)
            )

            # Preserve the first representation encountered
            documents.setdefault(key, result)

        fused = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            (documents[chunk_id], score)
            for chunk_id, score in fused
        ]