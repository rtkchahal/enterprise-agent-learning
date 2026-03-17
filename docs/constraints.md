# Constraints — What enterprise-agent-learning does NOT do

- Does NOT orchestrate agents (use LangGraph/AutoGen for that)
- Does NOT retrain or fine-tune models
- Does NOT replace existing feedback UI — captures signals passively from existing workflows
- Does NOT require changes to the underlying LLM or model provider
- Does NOT handle multi-tenant data isolation in v0.1 (planned for v0.2)
- Does NOT require internet access or external APIs in base mode
- Does NOT store PII — feedback entries are about agent behaviour patterns, not user data
