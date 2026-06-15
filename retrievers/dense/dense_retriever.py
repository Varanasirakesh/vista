from qdrant_client import QdrantClient

from ingestion.embeddings.embedding_service import EmbeddingService


class DenseRetriever:
    def __init__(
        self,
        collection_name: str = "support_knowledge_base",
        top_k: int = 5,
    ):
        self.client = QdrantClient(
            host="localhost",
            port=6333,
        )
        self.embedding_service = EmbeddingService()
        self.collection_name = collection_name
        self.top_k = top_k

    def retrieve(
        self,
        query: str,
    ):
        query_vector = self.embedding_service.embed(query)
        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=self.top_k,
        )
        return results.points