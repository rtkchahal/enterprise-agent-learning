"""
knowledge_store.py — BM25+ Knowledge Store with Temporal Decay
===============================================================

The KnowledgeStore is the persistence and retrieval backbone of the
enterprise-agent-learning library.

Design
------
Every agent task interaction can produce a *knowledge entry* — a small,
structured record capturing a lesson, a best practice, or a corrected
mistake. Entries are indexed using BM25+ (via the `rank-bm25` package)
for fast, dependency-light full-text retrieval.

Temporal decay
~~~~~~~~~~~~~~
Knowledge has a shelf life. An entry created six months ago about a
deprecated API pattern should carry less weight than one created last
week. Retrieval scores are multiplied by an exponential decay factor:

    score = bm25_score × e^(−λ × age_days)

The default half-life is 30 days (λ ≈ 0.0231), making entries roughly
half as influential after a month and negligible after ~4 months. The
half-life is configurable per store instance.

Storage backends
~~~~~~~~~~~~~~~~
- **Local:** SQLite (zero-config, ideal for development and single-agent
  deployments)
- **Enterprise:** Azure Table Storage (planned — enables multi-agent,
  multi-tenant deployments with tenant isolation)

Retrieval contract
~~~~~~~~~~~~~~~~~~
`KnowledgeStore.retrieve(query, top_k=5)` returns the top-k entries most
relevant to the query string, already sorted by decayed BM25+ score
descending. Callers can inject the results directly into an agent system
prompt as ``## Relevant Context``.

Knowledge entry schema
~~~~~~~~~~~~~~~~~~~~~~
Each entry is a dict with the following keys:

    {
        "id":         str,    # UUID
        "topic":      str,    # e.g. "contract-review"
        "content":    str,    # the lesson text
        "source":     str,    # "feedback" | "study" | "manual"
        "rating":     float,  # 1.0–5.0 (None if not rated)
        "tags":       list,   # keyword tags
        "created":    str,    # ISO-8601 date
        "reinforced": str,    # ISO-8601 date (updated on re-use)
    }
"""


class KnowledgeStore:
    """BM25+ knowledge store with temporal decay for enterprise AI agents.

    Parameters
    ----------
    db_path : str
        Path to the SQLite database file. Will be created if it does not
        exist. Use ``:memory:`` for an ephemeral in-process store.
    half_life_days : float, optional
        Half-life for temporal decay in days. Defaults to 30. Increase
        for domains where knowledge stays relevant longer (e.g. legal),
        decrease for fast-moving domains (e.g. market data).
    """

    pass
