---
name: reference-session-logging
description: The append-only session log convention — format, rules, and the rotation procedure for logs/log.md
metadata:
  type: reference
---

# Session logging convention

Session-by-session history lives in exactly one place: `logs/log.md`. This file spells out the convention so future sessions follow it rather than reinvent it.

**Format:**

- One dated header (`## YYYY-MM-DD`) per session, bullets underneath, newest at the bottom.
- One bullet per notable thing created, changed, or decided.
- Append-only, forever. Never edit or delete a past entry. If a past entry turns out to be wrong, add a new entry noting the correction — never rewrite history.
- Terse is the ideal, not a hard limit. Sessions doing real design work may produce detailed entries; that's fine, losing real information is not.

**Content/log separation:** Vault content pages document current state only — no date stamps, no "corrected by the user," no correction narratives. Citation-confidence flags ("extended, not attested") are facts about the claim and are allowed on content pages, terse and undated. History goes in the log. `AIOS/` (memory + site-map) is exempt — tracking change over time is its job.

**Rotation (only when the user asks — never roll unprompted):**

1. `cp logs/log.md logs/archive/log-NNN.md` — verbatim, zero-padded, next sequential number (first is `log-001.md`). The archive file is frozen forever; never edit it again.
2. Replace `logs/log.md` with just the header plus a pointer to the archive and `logs/index.md`.
3. Add an entry to `logs/index.md` (create it on first rotation) — one prose paragraph per archived file, oldest first, summarizing major threads by date-section, so the right archive can be found without opening each one.
4. Update `AIOS/site-map.md` if it lists the log files.
5. Update this memory file to record anything learned from the roll, since rotation is a permanent step in future rolls.

**Rotation history:** the first roll happened 2026-10-31 (`log-001.md`, covering 2026-09-26 to 2026-10-31; 385 lines). `logs/archive/` and `logs/index.md` now exist. The new `log.md` opens with a pointer line naming the archives, which should be extended with each later roll. Tip: before rolling, `grep -n '^##' logs/log.md` and skim each section's first bullets to write the index paragraph; later-dated entries may be nested under an older date's heading, so use the true dates.

**Why:** This convention comes from a sibling conlang/worldbuilding vault where it has run long-term. It exists because (a) sessions start cold and re-derive context without durable memory, and (b) letting history leak into content pages turns every page into a changelog — the two jobs must stay separate.

**How to apply:** Every session that changes vault content ends with a log entry under today's date header. When in doubt about whether a sentence belongs on a content page or in the log, ask: "does this describe how things are, or how they came to be?" The former goes on the page, the latter in the log.
