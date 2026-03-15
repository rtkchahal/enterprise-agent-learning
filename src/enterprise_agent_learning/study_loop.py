"""
study_loop.py — Idle Study Loop
================================

The StudyLoop runs autonomous study sessions whenever the agent has no
active tasks. Each session produces 1–3 new knowledge entries that are
written to the KnowledgeStore, compounding the agent's expertise over time.

Design
------
The StudyLoop implements three distinct study modes, each targeting a
different source of learning:

1. Feedback Analysis (runs when unprocessed feedback exists)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Reads recent feedback entries from the KnowledgeStore, identifies patterns
— what task types score consistently high? what failure modes recur? —
and generates generalised rules or heuristics. These are stored as
``source="study"`` knowledge entries with a topic of ``"feedback-pattern"``.

Example output:
    "Contract review tasks that include a risk summary section consistently
    score 4.5+ (n=12). Always include a structured risk summary."

2. Domain Deepening (always eligible)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Uses the agent's configured ``specialties`` list to identify knowledge gaps
and research best practices. In the initial implementation this is driven
by an LLM call with a structured prompt; later versions may pull from
curated domain corpora.

Example output (specialty = "solidity-audit"):
    "ERC-4626 vault contracts require checking share-to-asset ratio
    rounding direction. Favour rounding down on deposit, up on redeem."

3. Task Simulation (always eligible)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Generates a realistic synthetic task matching one of the agent's
specialties, works through it step-by-step using the agent's configured
LLM, and extracts the key decision points as knowledge entries. Serves as
a practice run — the agent rehearses approaches before encountering real
tasks.

Scheduling
~~~~~~~~~~
``StudyLoop`` is designed to be invoked by a scheduler (e.g. APScheduler,
a cron job, or an Azure Function Timer trigger). The recommended frequency
is every 30 minutes when the agent's task queue is empty. The loop is
idempotent — running it on an already-studied corpus is safe but
produces no new entries.

Session result schema
~~~~~~~~~~~~~~~~~~~~~
    {
        "session_id":     str,   # UUID
        "mode":           str,   # "feedback_analysis" | "domain_deepening"
                                 #   | "task_simulation"
        "entries_added":  int,
        "duration_s":     float,
        "timestamp":      str,   # ISO-8601
    }
"""


class StudyLoop:
    """Runs autonomous idle study sessions to grow the agent's knowledge base.

    Parameters
    ----------
    store : KnowledgeStore
        The knowledge store that study-produced entries will be written to.
    collector : FeedbackCollector
        Used to access and mark processed feedback signals during feedback
        analysis sessions.
    specialties : list[str]
        List of domain specialty strings that guide domain deepening and
        task simulation sessions. Examples: ``["contract-review",
        "risk-analysis", "solidity-audit"]``.
    llm_client : object, optional
        LLM client used for domain deepening and task simulation prompts.
        Expected to expose an ``invoke(prompt: str) -> str`` interface.
        Defaults to None (sessions requiring LLM calls will be skipped
        until a client is provided).
    """

    pass
