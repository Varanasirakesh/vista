from pydantic import BaseModel
from typing import Optional


class ExtractedElement(BaseModel):
    document_id: str
    filename: str
    page_number: int
    element_type: str
    text: str
    coordinates: Optional[dict] = None
    parent_section: Optional[str] = None