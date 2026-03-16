# enterprise-agent-learning

Self-learning middleware for enterprise AI agents. Agents that get better every week — not by retraining, but by studying their own work.

## Project structure
```
src/enterprise_agent_learning/
  __init__.py
  knowledge_store.py   # BM25+ with temporal decay (score = bm25 * e^(-λ*age))
  feedback_collector.py # Captures signals from SharePoint/Teams/CSAT
  study_loop.py        # Idle study: feedback_analysis, domain_deepening, task_simulation
tests/
examples/
  langgraph_basic.py   # Intended usage pattern (stub)
docs/
  design.md            # Full design document
```

## Always do
- `first run the tests` at session start: `pytest -q`
- `use red/green TDD` for all new code
- Run `ruff check src/ tests/` before committing
- Run `mypy src/ --ignore-missing-imports` before committing

## Rules (modular)
@rules/testing.md
@rules/coding-style.md
@rules/agents.md

## Subagents available
- `planner` — break down features before coding
- `tdd-guide` — test-first implementation
- `code-reviewer` — quality gate before commit
- `refactor-cleaner` — post-feature cleanup

## Key design decisions
- KnowledgeStore uses SQLite (local) or Azure Table Storage (enterprise)
- Temporal decay half-life: 30 days (configurable)
- Study loop runs every 30 min via APScheduler when idle
- All feedback signals are passive — no new UI required for enterprise deployment
- Framework-agnostic: wraps LangGraph/AutoGen/Semantic Kernel
