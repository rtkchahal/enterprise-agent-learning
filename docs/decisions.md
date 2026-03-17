# Architecture Decision Records

## ADR-001: SQLite as default knowledge store backend
**Date:** 2026-03-16  
**Status:** Accepted  
**Decision:** Use SQLite for local/dev, Azure Table Storage for enterprise  
**Reason:** Zero infra setup for devs; Azure Table Storage is standard in enterprise Capgemini deployments  
**Trade-off:** SQLite not suitable for multi-process writes (acceptable for single-agent use case)

## ADR-002: BM25+ over vector embeddings for retrieval
**Date:** 2026-03-16  
**Status:** Accepted  
**Decision:** Use `rank-bm25` (BM25Okapi) not semantic embeddings  
**Reason:** No embedding model dependency, faster, deterministic, works offline  
**Trade-off:** Misses semantic similarity (e.g. "error" vs "exception") — acceptable for structured domain knowledge  
**Future:** Add optional embedding layer as `search_mode="semantic"` parameter

## ADR-003: 30-day temporal decay half-life
**Date:** 2026-03-16  
**Status:** Accepted  
**Decision:** Default half-life = 30 days, configurable  
**Reason:** Enterprise process rules change quarterly; 30 days keeps recent feedback dominant  
**Formula:** `score = bm25_score * exp(-ln(2)/30 * age_days)`

## ADR-004: APScheduler for idle study loop
**Date:** 2026-03-16  
**Status:** Proposed  
**Decision:** Use APScheduler (BackgroundScheduler) for 30-min idle study cycle  
**Reason:** Lightweight, no external dependencies, works in any Python app  
**Trade-off:** Not suitable for distributed multi-instance deployments (acceptable for v0.1)
