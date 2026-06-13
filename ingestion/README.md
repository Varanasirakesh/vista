| Folder            | Purpose                     |
| ----------------- | --------------------------- |
| `data/raw/`       | Original PDFs               |
| `data/extracted/` | Extracted elements          |
| `data/processed/` | Chunked artifacts           |
| `data/qdrant/`    | Vector database persistence |

PDF
↓
Unstructured (hi_res)
↓
Raw Elements
↓
Metadata Enrichment
↓
Coordinate Preservation
↓
Chunking (future)
↓
Embeddings (future)
↓
Qdrant (future)