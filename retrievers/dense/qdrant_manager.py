""" 
This module manages the Qdrant collection for storing and retrieving vectors.
It provides functions to create a collection, insert dummy vectors, and manage the Qdrant client
"""
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
)
from ingestion.embeddings.embedding_service import EmbeddingService

COLLECTION_NAME = "support_knowledge_base"

client = QdrantClient(
    host="localhost",
    port=6333,
)

def create_collection():

    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE,
        ),
    )

    print("Collection ready.")
def insert_dummy_vector():
    embedding_service = EmbeddingService()
    text = "Restart OneDrive from the system tray."
    vector = embedding_service.embed(text)
    point = PointStruct(
        id=1,
        vector=vector,
        payload={
            "text": text,
            "filename": "dummy.pdf",
            "page_number": 1,
            "element_type": "ListItem",
        },
    )
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[point],
    )
    print("Dummy vector inserted.")

if __name__ == "__main__":
    create_collection()
    insert_dummy_vector()