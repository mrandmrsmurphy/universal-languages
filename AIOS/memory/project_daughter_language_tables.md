---
name: project-daughter-language-tables
description: Plan for a WALS-based "Daughter languages" table in each UL's Anthropology page; Zens is the pilot
metadata:
  type: project
---

Each UL's `Anthropology.md` should get a "Daughter languages" section: a table of the source languages' WALS values, using the same rows as `Language Comparisons.md`, with the UL's own value as the last column.

- Pilot done on `Zens/Anthropology.md`. Roll out ONE UL at a time, only after the user reviews the pilot; never all at once.
- Pull values from the WALS CLDF release (github.com/cldf-datasets/wals, `values.csv`/`codes.csv`/`languages.csv`) by script; never type WALS values from memory. Blank = not coded in WALS.
- Reuse only matrix rows that have a WALS feature. Language-specific tables (consonants, vowels, etc.) stay in each UL's own pages and are not templated.
- Generate with `AIOS/scripts/build_daughter_table.py` (per-UL CONFIG dict). Done: Zens, Folksprak, Dravindian, Balkan, Guosa, Interlingua, Indo-Malay (new page), Interslavic, Neo-Sanskrit, Middle Semitic, SEDES, Ortatürk. MSEAL. Known matrix mismatches (Zens future affix + case count, Folksprak polar-question particle, Dravindian typology F vs agglutinative; Dravindian relative-clause "post" unverified; Balkan cases, definite article, vowels, stress; Guosa word order, clusivity, vowels; Interlingua gender, aspect) are logged, not yet fixed.
