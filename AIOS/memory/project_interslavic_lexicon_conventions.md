---
name: project-interslavic-lexicon-conventions
description: Standing conventions for the Interslavic lexicon (Interslavic/Lexicon/) and Swadesh page — modeled on Folksprak's, with Cyrillic filenames
metadata:
  type: project
---

# Interslavic lexicon conventions and standing decisions

**Why:** The user wants every UL to eventually mirror Folksprak's sub-page set. Interslavic's lexicon follows the same one-file-per-word pattern; set up 2026-10-21 with the first entry `я.md`.

**How to apply:**

- One file per word in `Interslavic/Lexicon/`, named and titled by the Cyrillic spelling; `Lexicon.md` holds the entry format and an index line per entry — add one for every new file. Model: [[project-folksprak-lexicon-conventions]].
- Entry rows (omit any that don't apply): Latin, IPA, Part of speech, Gloss, Proto-Slavic (with PIE source if given), Compare (Eastern / Western / Southern), Swadesh №. Inflected words get a Forms table taken from `Interslavic/Morphology`.
- Every coined Interslavic form in `Interslavic/Swadesh.md` is a `[[word]]` link to its lexicon file; coin a word → create the file.
- The user supplies etymology and IPA from the Interslavic wiki (wikitext pasted); don't invent Proto-Slavic sources. Drop wiki templates (`{{ConSwad}}`, categories).
- The Swadesh page keeps six columns (OCS, Czech, Polish, Upper Sorbian, Russian, Interslavic); Belarusian, Rusyn, Ukrainian, Slovak and Lower Sorbian were cut by the user. Source rows 100, 106, 126, 137, 145, 181, 196 were incomplete (marked †).
- All Interslavic words are lowercase everywhere (filenames, titles, Swadesh cells, links, Morphology tables). The source wiki capitalizes some entries (Тутой, Что, Един...) — normalize on conversion.
- Standing decisions (user, 2026-10-21): long-term script is Cyrillic, Latin is an interim aid for Czechs/Poles etc.; j is й (not ј); South Slavic is a non-voting audience (votes in Balkan); keep the ~300 million population figure; instant intelligibility outranks ease of learning; foundation Proto-Slavic and "continuation of Old Church Slavonic" are compatible; the defunct projects merged in 2011 need not be named; cite ISO 639-3 `isv` (adopted April 2024). Orthography (user, 2026-10-21): Е = /ɛ/ (Latin e), Є = /jɛ/ (je), Э not used; Я, Ю, Є are the ligatures (ja, ju, je); Њ = ñ /ɲ/ and Љ = /ʎ/ are letters; /dz/ exists (ДЗ); only one /r/; /x~h/ and tilde variants (incl. retroflex) are accepted pronunciations; mid-vowel IPA is loose (/e/ /o/ fine).
- Noun morphology (user, 2026-10-21): lives in `Interslavic/Morphology` (not Morphosyntax). Four declensions with a hard/soft and animate split; vocative shown but not a case; consonantal declensions (kamen, imę, mati) labeled antiquarian. Latin is plain: no ų ę ě ȯ ŕ (written u e e o r); Cyrillic is the final orthography; ų → у, ę → е, ě → е (plain e; only Є is je), ȯ → о; Е = e, Є/Я/Ю are the jV ligatures. Too many diacritics: ť ď ň ř ľ ś only show softness and resolve to t d n r l s. Interslavic words never use є for ě (кде, не, дете, человек). No soft sign: hardness/softness and animacy are lexical. Gen. pl. -ø after hard stems, -ej after soft; soft feminines keep j (zemjam). Locative sg. M/N: -ě (-i, -u). Old project names (Slovianski etc.) are the same language now.
- Source conflicts (user, 2026-10-21): the various Interslavic wikis disagree; take the clear, pan-Slavic, obvious answer. Latin text pasted from a wiki is already unambiguous — don't re-derive it; Cyrillic is derived from it by the Orthography rules (jego -> єго; n- forms use њ: njego -> њего). Pronoun tables on `Interslavic/Morphology` are Latin + Cyrillic with short forms in parentheses.
