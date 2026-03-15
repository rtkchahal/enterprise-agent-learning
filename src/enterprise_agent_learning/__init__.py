"""
enterprise-agent-learning
=========================

Self-learning middleware for enterprise AI agents.

Agents that get better every week — not by retraining, but by studying their own work.

Components
----------
KnowledgeStore
    BM25+ retrieval over a time-decayed knowledge base backed by SQLite
    (or Azure Table Storage for enterprise deployments).

FeedbackCollector
    Captures quality signals from completed agent tasks and converts them
    into structured knowledge entries.

StudyLoop
    Runs idle study sessions — feedback analysis, domain deepening, and
    task simulation — to continuously grow the knowledge base.

Quick start
-----------
>>> from enterprise_agent_learning import KnowledgeStore, FeedbackCollector, StudyLoop
>>> store = KnowledgeStore(db_path="agent_knowledge.db")
>>> collector = FeedbackCollector(store=store)
>>> loop = StudyLoop(store=store, collector=collector, specialties=["contract-review"])
"""

from enterprise_agent_learning.knowledge_store import KnowledgeStore
from enterprise_agent_learning.feedback_collector import FeedbackCollector
from enterprise_agent_learning.study_loop import StudyLoop

__all__ = ["KnowledgeStore", "FeedbackCollector", "StudyLoop"]
__version__ = "0.1.0"
