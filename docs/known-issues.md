# Known Issues

## KI-001: KnowledgeStore not yet implemented
**Status:** In progress (Week 1)  
**Impact:** Core functionality unavailable — stubs only  
**Workaround:** None  
**Owner:** Week 1 coding session

## KI-002: Temporal decay not validated against real data
**Status:** Design only  
**Impact:** Half-life of 30 days is a reasonable assumption but untested  
**Plan:** Validate with synthetic feedback data in Week 2 testing

## KI-003: No concurrency protection on SQLite writes
**Status:** Known limitation  
**Impact:** Multi-threaded agent writes may cause SQLite locking errors  
**Workaround:** Use single-threaded StudyLoop (acceptable for v0.1)  
**Plan:** Add write queue or WAL mode in v0.2
