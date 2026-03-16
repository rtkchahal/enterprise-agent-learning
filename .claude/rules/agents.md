# Agent Delegation Rules

When to delegate to subagents:

- **planner** — before implementing any feature >2 hours. Get a plan first.
- **tdd-guide** — when writing tests for a new module or complex function
- **code-reviewer** — before every commit. Flag issues before they merge.
- **refactor-cleaner** — after a feature lands, clean up in a separate pass

## Subagent isolation rule
Subagents have NO shared memory. Pass ALL relevant context explicitly:
- Current module state (relevant existing code)
- What was already tried
- Specific acceptance criteria
- Test results if relevant

## Loop termination
Always check `stop_reason == "end_turn"`. Never use iteration caps or text parsing.
