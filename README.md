# enterprise-agent-learning

> **Self-learning for enterprise AI agents. Agents that get better every week — not by retraining, but by studying their own work.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyPI - Coming Soon](https://img.shields.io/badge/PyPI-coming%20soon-lightgrey)](https://pypi.org/)

---

## The Problem

Enterprise AI agents plateau.

They're deployed, they run, and six months later they make the same mistakes they made on day one. The frameworks — LangGraph, AutoGen, Semantic Kernel — handle orchestration beautifully. But none of them have a built-in mechanism for agents to **improve from their own operational feedback**.

Your agents handle hundreds of tasks a month. That's hundreds of learning opportunities, discarded.

---

## How It Works

Three components work together to close the loop:

### 1. Feedback Collector
Captures quality signals from every completed task — approvals, revisions, rejections, and ratings — without requiring new UI. Wires into existing workflows: SharePoint approval flows, Teams reactions, service desk resolution status.

### 2. BM25+ Knowledge Store with Temporal Decay
Every task interaction produces a knowledge entry. Retrieval uses BM25+ search keyed to incoming task descriptions. Stale knowledge decays automatically:

```
score = bm25_score × e^(−λ × age_days)   [half-life = 30 days]
```

Top-5 relevant entries are injected into the agent system prompt as `## Relevant Context` before each task — no retraining, no fine-tuning.

### 3. Idle Study Loop
When no active tasks are running, the agent studies:
- **Feedback analysis** — finds patterns in what scored well and what failed
- **Domain deepening** — researches best practices for its configured specialties
- **Task simulation** — generates realistic tasks and works through them as practice

Each session produces 1–3 new knowledge entries.

---

## Installation

```bash
pip install enterprise-agent-learning
```

> ⚠️ Coming soon — not yet published to PyPI. Clone and install locally for now:
> ```bash
> git clone https://github.com/rtkchahal/enterprise-agent-learning.git
> cd enterprise-agent-learning
> pip install -e .
> ```

---

## Quick Start

```python
from enterprise_agent_learning import KnowledgeStore, FeedbackCollector, StudyLoop

store = KnowledgeStore(db_path="agent_knowledge.db")
collector = FeedbackCollector(store=store)
loop = StudyLoop(store=store, collector=collector, specialties=["contract-review", "risk-analysis"])
```

Wrap your existing LangGraph or AutoGen agent — no changes to your orchestration logic required.

---

## Framework Compatibility

Designed for **LangGraph** and **AutoGen**. Slots in as a middleware layer — you keep your existing agent graph unchanged.

- `KnowledgeInjectionNode` for LangGraph pipelines
- `LearningMiddleware` adapter for AutoGen agents
- Works with Azure OpenAI out of the box

See working examples in [`examples/`](examples/).

---

## Roadmap

| Week | Deliverable |
|------|-------------|
| **Week 1** | `KnowledgeStore` — SQLite backend, BM25+ retrieval, temporal decay |
| **Week 2** | `StudyLoop` — feedback analysis, domain deepening, task simulation sessions |
| **Week 3** | LangGraph + AutoGen examples, before/after benchmark, PyPI publish |

---

## Why Not Just Fine-Tune?

Fine-tuning is expensive, slow, and requires labelled datasets your ops team doesn't have time to build. This library takes a different bet: **retrieval-augmented learning** from live operational feedback. No GPU. No MLOps pipeline. Just a SQLite file and a cron job.

---

## Credits

- Inspired by the self-learning loop in [CashClaw](https://github.com/moltlaunch/cashclaw) by Moltlaunch — the pattern that proved this works
- [ByteRover](https://github.com/moltlaunch/byterover) — semantic memory for OpenClaw agents
- Anthropic "Building Effective Agents" — evaluator-optimizer loop design

Built to bring the CashClaw pattern into enterprise AI delivery by [Ravi Chahal](https://github.com/rtkchahal).

---

## License

MIT © 2026 Ravi Chahal
