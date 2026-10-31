---
name: feedback-write-memories-before-session-ends
description: Persist durable notes to AIOS/memory and logs/log.md promptly — chat/session memory is not reliable
metadata:
  type: feedback
---

# Write memories before the session ends

**Why:** Ephemeral chat or agent-session memory can be deleted without warning. Only vault files under `AIOS/memory/` (indexed in `AIOS/memory-index.md`) and append-only `logs/log.md` survive across sessions.

**How to apply:**

- When something is worth remembering (a standing decision, a correction, a workflow preference, a fact that would otherwise be re-derived), write it to the vault in the same turn — do not wait for a later "wrap-up."
- If the user says to write memories now, or asks whether you can follow protocol, treat that as a cue to flush anything durable immediately.
- Durable → `AIOS/memory/` + a new index line. Session history → today's header in `logs/log.md`. Nothing meant to persist goes outside this vault folder.
