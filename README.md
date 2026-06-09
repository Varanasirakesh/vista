# Enterprise AI Support Copilot

Production-grade AI Support Assistant built using open-source models and modern AI engineering practices.

---

## Overview

Enterprise AI Support Copilot is an end-to-end Retrieval-Augmented Generation (RAG) platform designed to assist support engineers in troubleshooting issues using organizational knowledge bases.

The system ingests support documentation, retrieves relevant information using advanced retrieval techniques, generates evidence-backed responses using open-source LLMs, and provides explainability through highlighted source documents.

The primary goals of this project are:

* Learn and demonstrate production-grade AI engineering concepts.
* Prepare for AI Engineer interviews through practical implementation.
* Explore modern LLM application architectures.
* Build a potentially deployable and extensible support assistant platform.

---

## Key Objectives

* Build a production-grade RAG system.
* Use only open-source models where possible.
* Support local development using Ollama and Docker.
* Implement enterprise-level retrieval strategies.
* Introduce AI observability and evaluation.
* Provide explainability through PDF evidence highlighting.
* Explore agentic workflows using LangGraph and MCP.
* Prepare the system for future cloud deployment.

---

## Core Features

### Document Processing

* PDF ingestion pipeline.
* Extraction using Unstructured.
* High-resolution parsing for coordinate extraction.
* Metadata preservation.
* Document lifecycle management.

---

### Retrieval Pipeline

* Semantic chunking.
* Dense retrieval.
* BM25 retrieval.
* Hybrid retrieval.
* Parent-child retrieval.
* Cross-encoder reranking.

---

### Generation Pipeline

* Prompt engineering.
* Context compression.
* Source attribution.
* Evidence-based answering.
* Confidence-aware responses.

---

### Explainability

* Page-level citations.
* Region-level PDF highlighting.
* Coordinate preservation.
* Retrieval trace visualization.

---

### Guardrails

Input guardrails:

* Prompt injection detection.
* Jailbreak prevention.
* Toxicity filtering.
* PII detection.

Retrieval guardrails:

* Low-confidence detection.
* Empty retrieval handling.

Output guardrails:

* Hallucination checks.
* Unsupported claim detection.
* Safety filtering.

---

### Agentic Capabilities

* LangGraph orchestration.
* Tool creation.
* Tool calling.
* Multi-step reasoning.
* MCP client integration.
* MCP server implementation.

---

### Evaluation

* RAGAS-based evaluation.
* Faithfulness measurement.
* Answer relevancy scoring.
* Context precision.
* Context recall.
* Benchmark dataset creation.

---

### Observability

* LangSmith tracing.
* OpenTelemetry instrumentation.
* Retrieval diagnostics.
* Latency tracking.
* User feedback collection.
* Failure analysis dashboards.

---

### Infrastructure

* FastAPI backend.
* Streamlit frontend.
* PostgreSQL.
* Redis.
* Qdrant.
* Docker and Docker Compose.
* GitHub-based development workflow.

---

### Deployment

Future phases include:

* AWS deployment.
* Reverse proxy configuration.
* CI/CD pipelines.
* Monitoring integration.
* Multi-tenant support.

---

## High-Level Architecture

User Query

↓

Semantic Cache (Redis)

↓

Hybrid Retrieval

├── Dense Retrieval (Qdrant)

└── Sparse Retrieval (BM25)

↓

Reranker

↓

Guardrails

↓

LangGraph Agent

↓

MCP Client Layer

↓

MCP Servers / Tools

↓

Open-Source LLM (Ollama)

↓

Response Generation

↓

Source Attribution + PDF Highlighting

↓

Feedback Collection

↓

Evaluation + Observability

---

## Technology Stack

### LLMs

* Ollama
* Hugging Face Models

Examples:

* Llama 3.x
* Qwen
* DeepSeek
* BGE models

---

### Embeddings

* BAAI/bge-large-en-v1.5
* intfloat/e5-large-v2

---

### Rerankers

* BAAI/bge-reranker-large
* cross-encoder/ms-marco-MiniLM-L-6-v2

---

### Vector Database

* Qdrant

---

### Backend

* FastAPI

---

### Frontend

* Streamlit

---

### Databases

* PostgreSQL
* Redis

---

### Agent Framework

* LangGraph

---

### Evaluation

* RAGAS

---

### Observability

* LangSmith
* OpenTelemetry

---

### PDF Processing

* Unstructured
* PyMuPDF

---

### Containerization

* Docker
* Docker Compose

---

### Version Control

* Git
* GitHub

---

## Planned Milestones

### Phase 0

Project blueprint and repository setup.

---

### Phase 1

GitHub initialization and development environment setup.

---

### Phase 2

Docker fundamentals and infrastructure setup.

---

### Phase 3

FastAPI, PostgreSQL, Redis, and Qdrant integration.

---

### Phase 4

PDF ingestion and extraction pipeline.

---

### Phase 5

Baseline RAG implementation.

---

### Phase 6

Hybrid retrieval.

---

### Phase 7

Reranking.

---

### Phase 8

Evidence highlighting and explainability.

---

### Phase 9

Guardrails.

---

### Phase 10

Evaluation using RAGAS.

---

### Phase 11

Observability using LangSmith and OpenTelemetry.

---

### Phase 12

LangGraph agents.

---

### Phase 13

MCP client and server implementation.

---

### Phase 14

Streamlit interface.

---

### Phase 15

Production hardening.

---

### Phase 16

AWS deployment.

---

## Repository Structure

support-copilot/

├── backend/

├── frontend/

├── ingestion/

├── retrievers/

├── rerankers/

├── agents/

├── mcp/

├── evaluations/

├── observability/

├── dashboards/

├── docker/

├── tests/

├── docs/

└── .github/

---

## Project Vision

This project aims to bridge the gap between experimental RAG applications and production-ready AI systems.

By combining retrieval engineering, agentic workflows, evaluation, observability, and deployment practices, the system will serve as both:

* a learning platform for mastering AI engineering concepts, and
* a showcase project demonstrating readiness for real-world AI Engineer roles.

---

## Status

Current Phase:

Phase 0 — Project Blueprint and Repository Design

---

## Disclaimer

This project is being developed iteratively with a strong emphasis on learning, explainability, and production best practices. Architectural decisions may evolve as new capabilities are introduced.
