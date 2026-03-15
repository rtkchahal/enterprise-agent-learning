# Enterprise Agent Learning — Design Doc

_Author: Ravi Chahal | Date: 2026-03-14 | Status: Draft v0.1_

---

## Problem

Enterprise AI agents plateau. They're deployed, they run, and six months later they make the same mistakes they made on day one. The frameworks (LangGraph, AutoGen, Semantic Kernel) handle orchestration beautifully — but none of them have a built-in mechanism for agents to improve from their own operational feedback.

Meanwhile, CashClaw (a crypto-native freelance agent) ships a self-learning loop that makes it measurably better over time. That pattern belongs in enterprise AI.

---

## The Pattern (stolen from CashClaw)

Three components working together:

### 1. Feedback Collection
Every agent task produces a quality signal:
- ✅ Approved / completed without revision
- 🔄 Revised (with revision reason)
- ❌ Rejected (with rejection reason)
- ⭐ Optional: manager rating (1-5) + free-text comment

No new UI needed. Wire into existing approval workflows:
- SharePoint approval flows → task ratings
- Teams message reactions → implicit signals
- Service desk resolution status → CSAT-equivalent

### 2. Knowledge Base (BM25+ with Temporal Decay)
```
Task completed → extract keywords → store as knowledge entry
{
  "id": "uuid",
  "topic": "solidity-audit",
  "content": "When auditing ERC-20 contracts, always check allowance overflow in transferFrom",
  "source": "feedback",
  "rating": 5,
  "tags": ["solidity", "audit", "erc20"],
  "created": "2026-03-14",
  "reinforced": "2026-03-14"
}
```

**Retrieval:** BM25+ search over knowledge base keyed to incoming task description.
**Temporal decay:** `score = bm25_score * e^(-lambda * age_days)`, half-life = 30 days.
**Injection:** Top 5 relevant entries injected into agent system prompt as `## Relevant Context`.

### 3. Idle Study Loop (3 Topics, Runs When No Active Tasks)
| Topic | Frequency | What it does |
|-------|-----------|--------------|
| Feedback analysis | When feedback exists | Find patterns: what scored well? what failed? Generate rules. |
| Domain deepening | Always | Research best practices for the agent's configured specialties |
| Task simulation | Always | Generate realistic task + work through approach. Practice run. |

Each session produces 1-3 knowledge entries stored in the knowledge base.

---

## Enterprise Architecture

```
┌─────────────────────────────────────────────────────────┐
│              Enterprise Agent Learning Layer             │
│                                                         │
│  Task Source          Agent Runtime        Learning      │
│  (SharePoint /   →   (LangGraph /    →    (BM25+        │
│   ServiceNow /        AutoGen /            Knowledge     │
│   Teams Bot)          Azure AI)            Base)         │
│                             ↑                  ↓         │
│                       Context Injection    Study Loop    │
│                       (top 5 relevant      (idle time)   │
│                        knowledge entries)               │
│                                                         │
│  Feedback Signal                                        │
│  (approval/rating) ─────────────────────→ Knowledge     │
│                                           Entry         │
└─────────────────────────────────────────────────────────┘
```

**Tech stack:**
- Knowledge store: SQLite (local) or Azure Table Storage (enterprise)
- BM25+ search: `rank-bm25` Python package (zero dependencies)
- Temporal decay: simple Python function
- LangGraph integration: custom node `KnowledgeInjectionNode`
- Azure OpenAI: existing client (no change)

---

## Minimal PoC — L'Oreal / Protective Life Agent

**Week 1 deliverable:** Add knowledge injection to existing agent
- [ ] Build knowledge store (SQLite, local)
- [ ] Build BM25+ retrieval function
- [ ] Add `KnowledgeInjectionNode` to existing LangGraph pipeline
- [ ] Wire manual rating (thumbs up/down in Teams) → knowledge entry

**Week 2 deliverable:** Add study loop
- [ ] Implement feedback analysis study session
- [ ] Implement domain deepening session (specialty = process defined in PDD)
- [ ] Schedule as cron (every 30 min idle)

**Week 3 deliverable:** Demo + write-up
- [ ] Before/after comparison: agent with vs without learning
- [ ] Internal case study (1 page)
- [ ] Open source the pattern as `enterprise-agent-learning` Python package
- [ ] LinkedIn post: "The self-improving enterprise agent"

---

## Differentiation vs. Current Market

| Capability | LangGraph | AutoGen | Semantic Kernel | This |
|-----------|-----------|---------|----------------|------|
| Orchestration | ✅ | ✅ | ✅ | ❌ (wraps them) |
| Observability | 🟡 | 🟡 | 🟡 | ✅ (via Opik) |
| Self-learning | ❌ | ❌ | ❌ | ✅ |
| Temporal decay | ❌ | ❌ | ❌ | ✅ |
| Idle study | ❌ | ❌ | ❌ | ✅ |
| Enterprise auth | ✅ | ✅ | ✅ | ✅ (inherits) |

**The pitch:** "We deploy agents that get better every week. Not because we retrain them. Because they study their own work."

---

## Capgemini Positioning

- Slides into any existing Azure AI / LangGraph engagement as an add-on module
- Differentiates Capgemini delivery from "we used the framework" to "we built compound intelligence"
- Reusable across clients — install once per engagement
- Measurable: show quality score trend over 30 days

**Client conversation:** "Your agent handled 200 tasks last month. Here's how it improved: week 1 avg score 3.2/5, week 4 avg score 4.6/5. Here's what it learned."

---

## Risks

| Risk | Mitigation |
|------|-----------|
| Knowledge base grows stale | Temporal decay handles it |
| Bad feedback poisons learning | Manual review UI on knowledge entries |
| Scope creep into framework territory | Stay thin — inject + study only, don't orchestrate |
| Client data in knowledge base | Use Azure Table Storage + tenant isolation |

---

## Open Source Strategy

Repo: `github.com/rtkchahal/enterprise-agent-learning`

- MIT license
- Python package: `pip install enterprise-agent-learning`
- LangGraph integration example
- Azure OpenAI example
- README with the operator playbook (train → supervised → autonomous)

**Why open source?** Builds credibility, drives LinkedIn content, positions Ravi as the person who brought CashClaw's pattern to enterprise. First mover advantage — no one has published this yet.

---

## Credits / Inspiration

- CashClaw by Moltlaunch (https://github.com/moltlaunch/cashclaw) — self-learning loop pattern
- ByteRover — semantic memory for OpenClaw agents
- Anthropic "Building Effective Agents" — evaluator-optimizer loop

---

_Next step: Ravi approves → build Week 1 PoC alongside L'Oreal or next available engagement._
