"""
feedback_collector.py — Feedback Signal Capture
================================================

The FeedbackCollector is responsible for capturing quality signals from
completed agent tasks and converting them into structured knowledge entries
that are written to the KnowledgeStore.

Design
------
Enterprise agents already live inside approval workflows. The
FeedbackCollector is a thin adapter that translates those existing signals
into learning material — no new UI, no new process for the end user.

Supported signal types
~~~~~~~~~~~~~~~~~~~~~~
- **Approved** — task completed and accepted without revision. Positive
  reinforcement: the approach that produced this outcome is stored as a
  high-confidence knowledge entry.
- **Revised** — task output was accepted after modification, along with a
  revision reason. The delta between original and revised output is
  captured as a corrective entry.
- **Rejected** — task output was rejected outright. The rejection reason is
  stored as a cautionary knowledge entry with a low rating.
- **Rated** — an optional 1–5 manager rating plus free-text comment. Used to
  weight entries in the KnowledgeStore and to surface high-quality examples
  during study sessions.

Integration points
~~~~~~~~~~~~~~~~~~
The FeedbackCollector exposes a simple ``record(signal)`` method. Callers
are responsible for wiring it into their feedback source. Planned adapters:

- ``SharePointAdapter`` — polls SharePoint approval list items
- ``TeamsReactionAdapter`` — maps Teams message reactions to signals
- ``ServiceDeskAdapter`` — maps CSAT / resolution status from ServiceNow /
  Jira Service Management

Each adapter produces a normalised ``FeedbackSignal`` dict that
``FeedbackCollector.record()`` ingests.

Signal schema
~~~~~~~~~~~~~
    {
        "task_id":     str,   # identifier of the originating task
        "task_desc":   str,   # natural-language description of the task
        "outcome":     str,   # "approved" | "revised" | "rejected"
        "reason":      str,   # revision/rejection reason (may be empty)
        "rating":      float, # 1.0–5.0 or None
        "comment":     str,   # free-text manager comment (may be empty)
        "timestamp":   str,   # ISO-8601
    }
"""


class FeedbackCollector:
    """Captures task feedback signals and writes knowledge entries to the store.

    Parameters
    ----------
    store : KnowledgeStore
        The knowledge store that entries will be written to.
    min_rating_to_store : float, optional
        Minimum rating required to store an approved or revised entry.
        Entries with a rating below this threshold are discarded. Defaults
        to 1.0 (store everything). Set higher (e.g. 3.0) to keep the
        knowledge base signal-rich.
    """

    pass
