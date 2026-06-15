"Why didn't you use Conda?"

You can answer:

"For this project I chose standard Python virtual environments because they integrate seamlessly with Docker, CI/CD pipelines, and production deployments."

That's a very strong answer.

"Why Docker?"

A strong answer is:

"Docker ensures consistency between development, testing, and deployment environments while simplifying dependency management and onboarding."

Difference between Image and Container?

Answer:

Image:
    Blueprint/template.

Container:
    Running instance of an image.

Q: What is a Docker image?

Answer:

A Docker image is a read-only template containing the application code, dependencies, runtime, and configuration required to run a service.

If asked:

"How did you manage different deployment environments?"

You can say:

"I maintained separate Docker Compose configurations for infrastructure, development, and production environments to avoid configuration drift."Why Redis in AI systems?

Redis provides low-latency access patterns useful for caching, rate limiting, session management, and transient application state.

How did you implement evidence-backed citations?

Answer:

"I preserved coordinate metadata during ingestion and propagated it through retrieval, enabling the system to highlight the exact source regions that supported generated answers."

"How did you ensure maintainability of your ingestion pipeline?"

You can answer:

"I documented the pipeline stages and artifact lifecycle to simplify onboarding, debugging, and future enhancements."

Why did you separate extraction, chunking, and embeddings?

You can answer:

"To enable independent experimentation. I could modify embedding models or chunking strategies without repeatedly processing the source documents."

Why start with dense retrieval before hybrid retrieval?

Answer:

"I established a dense retrieval baseline first to understand its performance characteristics before introducing additional complexity through hybrid search."

Why did you choose element-aware chunking?

Answer:

"Element-aware chunking preserved document structure and layout metadata, enabling precise citations and region-level highlighting while minimizing semantic fragmentation.

How did you improve chunk quality?

Answer:

"I introduced an element-aware chunking strategy where different document structures followed different processing paths, reducing retrieval noise while preserving important contextual metadata."

Why BGE?

"BGE models provided strong retrieval performance while remaining lightweight enough for local experimentation."

Why normalize embeddings?

"Normalization ensured consistent cosine similarity behavior during retrieval."

Why do you prefer module execution (python -m)?

You can say:

"It ensures imports resolve relative to the project root and aligns with how applications are executed in packaged environments."

Why normalize embeddings?

You can answer:

"Normalization ensures cosine similarity behaves consistently during vector search."

Why didn't you start directly with hybrid retrieval?

Answer:

"I established a dense retrieval baseline first to understand its behavior. Once evaluated, I introduced BM25 and reciprocal rank fusion to improve recall while preserving a measurable improvement path."

How did you reduce hallucinations?

Answer:

"I used retrieval-augmented generation with strict prompting that constrained the LLM to answer only from retrieved evidence."

How did you evaluate your RAG system initially?

You can answer:

"I established a small manually curated evaluation set to validate retrieval quality, grounding behavior, and out-of-domain handling before introducing automated evaluation frameworks.