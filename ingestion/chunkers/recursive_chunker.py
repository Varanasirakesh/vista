"""
Converts ExtractedElements into RAG chunks while preserving metadata.

NarrativeText elements are recursively chunked.
Titles, ListItems, and Tables are preserved as single chunks.
Headers, Footers, and Images are excluded from retrieval.
"""

import uuid
from langchain_text_splitters import RecursiveCharacterTextSplitter
from ingestion.chunkers.models import Chunk
from ingestion.extractors.models import ExtractedElement

SUPPORTED_FOR_RAG = {
    "NarrativeText",
    "Title",
    "ListItem",
    "Table",
}

SKIP_FOR_RAG = {
    "Header",
    "Footer",
}

FUTURE_MULTIMODAL = {
    "Image",
}

class RecursiveChunker:

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def chunk(
        self,
        element: ExtractedElement,
    ) -> list[Chunk]:
        chunks = []
        if not element.text or not element.text.strip():
            return []
        
        if element.element_type not in SUPPORTED_FOR_RAG:
            return []

        if element.element_type in {"Title", "ListItem", "Table"}:
            texts = [element.text]

        else:
            texts = self.splitter.split_text(element.text)
        for idx, text in enumerate(texts):

            chunks.append(
                Chunk(
                    chunk_id=str(uuid.uuid4()),
                    text=text,
                    chunk_index=idx,
                    document_id=element.document_id,
                    filename=element.filename,
                    page_number=element.page_number,
                    element_type=element.element_type,
                    coordinates=element.coordinates,
                    parent_section=element.parent_section,
                )
            )
        return chunks