---
name: project-folksprak-lexicon-conventions
description: Standing conventions for the Folksprak lexicon (Folksprak/Lexicon/) — one file per word, runic filenames, entry format, derivation habits
metadata:
  type: project
---

# Folksprak lexicon conventions

**Why:** The Folksprak lexicon is meant to move into its own vault someday, and each UL is meant to have its own Unicode area. The user (Aquatiki, the author of Folksprak; there is no separate committee) has set these rules in session; don't re-derive or revert them.

**How to apply:**

- One file per word in `Folksprak/Lexicon/`, never a big table. File name and title = runic spelling (not Latin). `Lexicon.md` holds the entry format and an index line per entry — add one for every new file.
- Entry rows (omit any that don't apply): Latin, IPA, Part of speech, Gloss, Composition, Proto-Germanic, Etymology (loanwords), Cognates, Swadesh №. Pronouns get a Forms table (case, runes, Latin, IPA) from `Folksprak/Morphosyntax`.
- No vowel-length marks in Latin forms; length is predictable (stressed + at most one following consonant = long). IPA is derived by me from `Phonology`/`Orthography` — flag it as derived. Proto-Germanic rows are always wanted: add standard reconstructions directly; only a genuinely uncertain source is left out and asked about. Cognates come from the Swadesh comparison columns where available.
- When a word has a Swadesh number, also fill its Folksprak cell in `Folksprak/Swadesh.md`.
- Letter facts the user has confirmed: ᚪ = /a/ (ᚨ is /o/, not used for a); ᛉ = /x/ (Latin x); ᛣ = /k/; ᚳ = /ʃ/ (Latin c — the settled rule: PGmc *sk → c before front vowels i/e/y, as in ficc; sk stays before back vowels, so culle became skulle); ᛟ = ø/œ (Latin ø, e.g. *bøm*); hi, vi are long; 9 = nyn.
- Sound correspondences are written into `Folksprak/Word formation guidelines` (þ→d, z→r, ai→e, eu→y, ō→ø, medial b→v, infinitive *-aną→-e, monosyllable gemination; sk→c is observed in ficc but not settled as general). Importing from upstream sources (folksprak.org draft, Munin, Parke): never verbatim — ü/uy→y, ö/oy→ø, check against vault /x/ and /ʃ/, vault form wins settled conflicts. **Before coining any word, pillage upstream first**: check the Munin dictionary (`http://folksprak.org/?target=dictionary` — entries are in the `var munin_data` JSON block in the page HTML, ~456 entries, keys word/type/translations with flk/eng/gem etc.), the wiki `concepts:*` pages, and Parke's dictionaries; if upstream has a form, prefer adapting it over coining fresh. Settled upstream divergences are recorded on `Folksprak/Divergences` (phonology, rune mapping, pronouns, grammar, lexicon) — add to that page whenever a new divergence is settled.
- The Linguifex Folksprak wiki has third-party errors; check wiki-sourced forms against `Orthography` and the user. Linguifex blocks scraping — get pasted wikitext.
