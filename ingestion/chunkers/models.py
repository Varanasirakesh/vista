from pydantic import BaseModel
from typing import Optional

class Chunk(BaseModel):
    chunk_id: str
    text: str
    chunk_index: int
    document_id: str
    filename: str
    page_number: int
    element_type: str
    coordinates: Optional[dict] = None
    parent_section: Optional[str] = None