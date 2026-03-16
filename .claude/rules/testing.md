# Testing Rules

- Always use red/green TDD: write failing test first, then implement
- 80% coverage minimum before any PR
- Use pytest fixtures for shared setup — no repeated boilerplate
- In-memory SQLite for KnowledgeStore tests (never hit disk in tests)
- Assert exact values — no `assert result is not None`
- Test edge cases: empty store, None inputs, boundary values for temporal decay
- Run `pytest --tb=short -q` before every commit
