import numpy as np
from qdrant_client import QdrantClient
from rank_bm25 import BM25Okapi

class BM25Retriever:

    def __init__(
        self,
        collection_name: str = "support_knowledge_base",
        top_k: int = 5,
    ):
        self.collection_name = collection_name
        self.top_k = top_k
        self.client = QdrantClient(
            host="localhost",
            port=6333,
        )
        self.documents = []
        self.tokenized_documents = []
        self.bm25 = None
        self.build_index()

    def build_index(self):
        response, _ = self.client.scroll(
            collection_name=self.collection_name,
            limit=10000,
            with_payload=True,
            with_vectors=False,
        )
        self.documents = []
        self.tokenized_documents = []
        for point in response:
            payload = point.payload
            text = payload.get("text", "")
            if not text:
                continue
            self.documents.append(payload)
            self.tokenized_documents.append(
                text.lower().split()
            )
        self.bm25 = BM25Okapi(
            self.tokenized_documents
        )
        print(
            f"BM25 index built with "
            f"{len(self.documents)} documents."
        )

    def retrieve(
        self,
        query: str,
    ):
        query_tokens = query.lower().split()
        scores = self.bm25.get_scores(
            query_tokens
        )
        # batch_scores = self.bm25.get_batch_scores(
        #     query_tokens,
        #     list(range(len(self.documents)))
        # )
        top_indices = np.argsort(scores)[::-1][
            : self.top_k
        ]
        results = []
        for idx in top_indices:
            payload = self.documents[idx]
            results.append(
                {
                    "text": payload["text"],
                    "filename": payload.get("filename"),
                    "page_number": payload.get("page_number"),
                    "coordinates": payload.get("coordinates"),
                    "score": float(scores[idx]),
                    # "batch_score": float(batch_scores[idx]),
                    "chunk_id": payload.get("chunk_id"),
                }
            )

        return results