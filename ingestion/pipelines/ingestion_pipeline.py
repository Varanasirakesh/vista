from pathlib import Path
import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from transformers import Chunk

from ingestion.extractors.pdf_extractor import extract_pdf
from ingestion.extractors.models import ExtractedElement

from ingestion.chunkers.recursive_chunker import RecursiveChunker
from ingestion.chunkers.models import Chunk

from ingestion.embeddings.embedding_service import EmbeddingService

client = QdrantClient(
    host="localhost",
    port=6333,
)
COLLECTION_NAME = "support_knowledge_base"

chunker = RecursiveChunker()
embedding_service = EmbeddingService()

# to ingest a PDF file and generate chunks
def ingest_pdf(pdf_path: Path) -> list[Chunk]:
    print(f"\nProcessing: {pdf_path.name}")
    elements = extract_pdf(str(pdf_path))
    print(f"Extracted {len(elements)} elements")
    all_chunks = []
    for element in elements:
        metadata = element.metadata.to_dict()
        extracted_element = ExtractedElement(
            document_id=pdf_path.stem,
            filename=pdf_path.name,
            page_number=metadata.get("page_number", -1),
            element_type=type(element).__name__,
            text=getattr(element, "text", ""),
            coordinates=metadata.get("coordinates"),
            parent_section=None,
        )
        chunks = chunker.chunk(extracted_element)
        all_chunks.extend(chunks)
    print(f"Generated {len(all_chunks)} chunks")
    return all_chunks

# to create points(vectors) from chunks
def build_points(chunks: list[Chunk]) -> list[PointStruct]:
    points = []
    for chunk in chunks:
        vector = embedding_service.embed(
            chunk.text
        )
        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "chunk_id": chunk.chunk_id,
                    "text": chunk.text,
                    "document_id": chunk.document_id,
                    "filename": chunk.filename,
                    "page_number": chunk.page_number,
                    "element_type": chunk.element_type,
                    "coordinates": chunk.coordinates,
                    "parent_section": chunk.parent_section,
                    "chunk_index": chunk.chunk_index,
                },
            )
        )
    print(f"Generated {len(points)} vectors")
    return points

# to insert points(vectors) into Qdrant
def upsert_points(points: list[PointStruct]):
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
    )
    print("Inserted into Qdrant")

if __name__ == "__main__":
    pdf_folder = Path("data/raw")
    pdfs = list(pdf_folder.glob("*.pdf"))
    print(f"Found {len(pdfs)} PDFs")
    total_points = 0
    for pdf in pdfs:
        chunks = ingest_pdf(pdf)
        points = build_points(chunks)
        upsert_points(points)
        total_points += len(points)
    print("\nIngestion completed")
    print(f"Total vectors inserted: {total_points}")

"""
to do all above actions in one function
"""
# def ingest_pdf(pdf_path: Path):
#     print(f"\nProcessing {pdf_path.name}")
#     elements = extract_pdf(str(pdf_path))
#     points = []

#     for idx, element in enumerate(elements):
#         metadata = element.metadata.to_dict()
#         extracted_element = ExtractedElement(
#             document_id=str(pdf_path.stem),
#             filename=pdf_path.name,
#             page_number=metadata.get("page_number", -1),
#             element_type=type(element).__name__,
#             text=getattr(element, "text", ""),
#             coordinates=metadata.get("coordinates"),
#             parent_section=None,
#         )

#         chunks = chunker.chunk(extracted_element)
#         for chunk in chunks:
#             vector = embedding_service.embed(
#                 chunk.text
#             )
#             point = PointStruct(
#                 id=str(uuid.uuid4()),
#                 vector=vector,
#                 payload={
#                     "chunk_id": chunk.chunk_id,
#                     "text": chunk.text,
#                     "document_id": chunk.document_id,
#                     "filename": chunk.filename,
#                     "page_number": chunk.page_number,
#                     "element_type": chunk.element_type,
#                     "coordinates": chunk.coordinates,
#                     "parent_section": chunk.parent_section,
#                     "chunk_index": chunk.chunk_index,
#                 },
#             )
#             points.append(point)
#     print(f"Generated {len(points)} vectors.")
#     client.upsert(
#         collection_name=COLLECTION_NAME,
#         points=points,
#     )
#     print("Inserted into Qdrant.")

# if __name__ == "__main__":
#     pdf_folder = Path("data/raw")
#     pdfs = list(pdf_folder.glob("*.pdf"))
#     print(f"Found {len(pdfs)} PDFs.")
#     for pdf in pdfs:
#         ingest_pdf(pdf)
#     print("\nIngestion completed.")