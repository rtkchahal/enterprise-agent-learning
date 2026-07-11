# Pending Decisions — Session Miner

Proposed decisions extracted nightly. Review in morning, approve/reject.

---

## 2026-03-17

**brandonwise/humanizer chosen over blader** — Installed globally as CLI + skill. 29 patterns vs 24, statistical scoring (0-100), batch scan + autofix support. Scoped to public repos + client-facing docs only (skip internal notes, CLAUDE.md/AGENTS.md). Wired into code-reviewer subagent to flag scores > 45 on public READMEs. → Approve/Reject?

**ivangdavila/self-improving evaluated and skipped** — HOT/WARM/COLD tiered memory system with decay rules. Already have self-improving-agent skill + FEEDBACK-LOG.md. Third parallel memory system = more overhead, not value at current scale. Pattern stolen: 3x repetition before promoting to permanent rule (validate corrections recur before treating as rules). → Approve/Reject?

## 2026-03-20

**Google Stitch MCP integrated for UI design pipeline** — Wired into Claude Code via HTTP endpoint (`https://stitch.googleapis.com/mcp`). Text → UI designs → HTML export → Next.js site. Used for ravichahal.com personal platform (newsletter-first + subscriber-gated Lab). Created skill `stitch-design` to capture full design pipeline (Stitch → UI/UX Pro Max → Claude Code build). 350 generations/month free tier. → Approve/Reject?

**ravichahal.com personal content platform launched** — Dark OLED design (Space Grotesk + DM Sans), newsletter-first landing with email signup, two pillars (Agentic AI cyan + Bitcoin gold), subscriber-gated Lab section for experiments. Built with Next.js 15 + Tailwind v4 from Stitch HTML + DESIGN.md. LinkedIn → site → email funnel. Code at `~/projects/ravichahal-site/`. Photo: `public/images/ravi.png` with grayscale → color hover. → Approve/Reject?

**Tailwind v4 + Next.js 15 config fix documented** — `postcss.config.ts` → `.mjs` (TS config breaks Tailwind plugin registry). Added `@source "../**/*.{tsx,ts,jsx,js}"` to globals.css for v4 content scanning. Delete `.next/` after config rename to clear webpack cache. Stitch skill notes capture this gotcha. → Approve/Reject?

## 2026-03-27

**Codex CLI ACP integration completed with Azure backend** — Installed `@openai/codex` v0.117.0 globally. Uses Azure OpenAI endpoint (`pmi-foundry-ai.services.ai.azure.com`) with `gpt-5.3-codex` model. OPENAI_API_KEY set in `~/.zshrc`, model_provider configured as `azure` in `~/.codex/config.toml`. Codex confirmed working non-interactively (`codex exec`). Binding to Telegram forum topic still pending thread ID fix (topic:1 not topic:3). → Approve/Reject?

## 2026-04-03

**brain/wiki compiled as LLM knowledge base** — Spawned Sonnet 4.6 sub-agent to scan 60+ files across brain/, memory/, agentic-reference/ and compile 25 wiki articles. Entry point: brain/wiki/index.md. Validated Karpathy pattern: LLM as knowledge compiler, not just code generator. Bitcoin thesis contradiction flagged and corrected ($126K ATH was Oct 2025, currently in correction phase). → Approve/Reject?

**Weekly wiki recompilation cron proposed** — Run Sundays, Sonnet 4.6, ~$2/run. Scans brain/, memory/, agentic-reference/ for changes since last compile. Keeps wiki fresh + catches stale contradictions. Outputs wiki refresh to brain/wiki/ with date stamp. → Approve/Reject?

**steipete/aiedge OpenClaw audit rules applied** — Read 50+ tips doc. Key captures: intentional under-prompting for coding agents (vs over-specifying), plan mode first for complex multi-file work, MCP config audit (outlook-graph only = clean). Documented principles in CODING-AGENT-PRINCIPLES.md. → Approve/Reject?
