from retrievers.dense.dense_retriever import (
    DenseRetriever,
)

from retrievers.sparse.bm25_retriever import (
    BM25Retriever,
)

from retrievers.hybrid.rrf import (
    ReciprocalRankFusion,
)


class HybridRetriever:

    def __init__(
        self,
        top_k: int = 5,
    ):

        self.top_k = top_k

        self.dense_retriever = DenseRetriever(
            top_k=top_k,
        )

        self.sparse_retriever = BM25Retriever(
            top_k=top_k,
        )

        self.rrf = ReciprocalRankFusion()

    def retrieve(
        self,
        query: str,
    ):

        dense_results = (
            self.dense_retriever.retrieve(
                query
            )
        )

        sparse_results = (
            self.sparse_retriever.retrieve(
                query
            )
        )

        hybrid_results = self.rrf.fuse(
            dense_results,
            sparse_results,
        )

        return {
            "dense": dense_results,
            "sparse": sparse_results,
            "hybrid": hybrid_results,
        }