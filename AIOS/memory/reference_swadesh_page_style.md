---
name: reference-swadesh-page-style
description: The standard Swadesh page layout for every UL — 13 fixed semantic sections (Interslavic style), target column last, lexicon-linked forms
metadata:
  type: reference
---

# Swadesh page style (vault-wide policy)

**Why:** The Swadesh pages had drifted into different layouts; the user asked for the Interslavic style everywhere, as a policy (2026-10-24).

**How to apply:** Every `<Language>/Swadesh.md` follows this shape:

- Header line: `> Parent: [[X]] · Lexicon/Cross-UL/Sounds/Script links as applicable`.
- Intro paragraph: what comparison languages appear, what **—** (uncoined) and blank (unrecorded) cells mean, † for rows with incomplete source data, and a "List source" line.
- The 207 items in the **standard 13 sections**, with these exact ranges and labels:

| Range | Label |
| --- | --- |
| 1–21 | Pronouns, deixis and quantifiers |
| 22–35 | Numerals and dimensions |
| 36–50 | People and animals |
| 51–71 | Plants and animal parts |
| 72–91 | Body |
| 92–107 | Body functions and senses |
| 108–125 | Life, conflict, motion and posture |
| 126–146 | Handling, speech and change |
| 147–159 | Sun, water and ground |
| 160–171 | Weather, fire and landscape |
| 172–181 | Colors, time and temperature |
| 182–200 | Qualities |
| 201–207 | Particles and name |

- One table per section, columns: № | English | comparison languages... | **target language last**. Target-language forms are wikilinks to their lexicon files (create the file when a form is coined — see the per-language lexicon convention memories).
- Supplementary material (extra numerals, extra interrogatives) goes in its own section **after** №207 (e.g. Folksprak "Further numerals", Middle Semitic "Supplementary").
- English glosses follow each language's own column conventions (Folksprak/SEDES use "thou", MS/Interlingua as imported); don't harmonize across pages without asking.
- Standard 207 numbering is assumed by the sections; if a source list deviates, renumber to the standard (precedent: the Interlingua paste's duplicate №110, hunt → 112).
