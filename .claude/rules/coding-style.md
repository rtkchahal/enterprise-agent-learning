# Coding Style Rules

- All public functions must have type hints and docstrings
- No `print()` statements — use `logging` module
- No hardcoded credentials or API keys — use env vars or config objects
- No `eval()`, no `exec()`, no shell injection via subprocess
- Functions max 50 lines — split if longer (single responsibility)
- No commented-out code blocks — delete or keep, never comment
- Import order: stdlib → third-party → local (ruff enforces this)
- Run `ruff check src/ tests/` before every commit
- Run `mypy src/ --strict` — all type errors must be resolved
