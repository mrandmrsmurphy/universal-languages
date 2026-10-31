# UL Vault Instructions

This file and `AGENTS.md` are duplicates — always keep them byte-identical; edit both (or edit one and copy it over the other) whenever instructions change.

This vault is an Obsidian vault documenting the **Universal Languages** conlang/auxlang project: fifteen regional auxiliary languages (Folksprak, Middle Semitic, Interlingua, etc.), each derived from a proto-language or sprachbund, plus a cross-UL comparison matrix.

## Memory system (read first)

- Read `AIOS/memory-index.md` first, every session, before touching anything. It points to every durable memory (project identity, standing decisions, workflow feedback from past sessions). Do not skip it and re-derive things from scratch.
- Durability warning: never write anything meant to persist to `~/.claude/projects/.../memory/` or anywhere outside this vault folder. Everything meant to survive across sessions goes in `AIOS/memory/`, indexed in `AIOS/memory-index.md`. Session-by-session history of what was created/changed/decided goes in `logs/log.md` (append-only).
- See `AIOS/site-map.md` for the current page hierarchy and status of each section.

## Content pages vs. log — the rule that matters most

- Content pages (the language pages, `Language Comparisons.md`, the `Folksprak/` subtree and the other in-vault language subtrees, etc.) document **current state only**. No date stamps, no "decided by the user on X," no correction narratives. If a decision changes, update the page's fact in place, written as if it had been right from the start.
- All history — what was decided when, what got corrected, who caught what — belongs exclusively in `logs/log.md` (append-only, never edit past entries). If you catch yourself writing history on a content page, move it to today's log entry instead.
- Citation-confidence / evidentiary-weight flags ("plausible extension, not directly attested") are facts about the claim itself and are fine on content pages — terse and undated, no session references or names.
- `AIOS/site-map.md` and everything in `AIOS/memory/` are exempt from this rule — tracking what changed and when is their actual job. Dates and "New (date)" markers belong there.
