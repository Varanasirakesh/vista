# Docker Setup

## Infrastructure Services

| Service | Purpose | Port |
|----------|----------|-------|
| PostgreSQL | Persistent application data | 5432 |
| Redis | Caching and transient state | 6379 |
| Qdrant | Vector database | 6333 / 6334 |

---

## Starting Infrastructure

```powershell
.\docker\scripts\infra-up.ps1

## Compose Files

- docker-compose.infrastructure.yml → Local infrastructure services
- docker-compose.dev.yml → Development environment (future)
- docker-compose.prod.yml → Production environment (future)

## Services

- PostgreSQL
- Redis
- Qdrant