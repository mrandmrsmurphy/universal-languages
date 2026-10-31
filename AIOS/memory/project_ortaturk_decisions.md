# Ortatürk decisions

The Turkic-zone UL. On 2026-10-25 the user switched this slot from **Jalpi** (the vault's planned revival of Gaspirali's historical pan-Turkic project) to **Ortatürk**, an extant project by others (Kärimov & Mutalov 1992 → 2005 → VATN simplified 2008 → Mireev's *Öztürk Tili* 2023, 16,000-word dictionary; Glosbe `mis_ort`; VK community "Öztürkçe"). Same adoption pattern as Interlingua / Interslavic / Guosa: document, don't reform.

## Settled

- The page is `Ortatürk.md` (root stub for now); all vault references renamed from Jalpi (hub table, UL Map, Roadmap, Comparisons, Credits, map colour #9970ab).
- Foundation: statistical average of Turkic languages ("double majority": by speakers and by number of languages), 25 languages / ~160M speakers in the 2008 VATN version.
- Script: ARMENIAN long-term (carried over from the Jalpi plan); Latin accepted only temporarily (per the user's every-UL-its-own-script principle). Armenian orthography settled 2026-10-25 (user's draft + one fix): consonants մ ն նկ(ŋ) · պ տ ճ կ ք · բ դ ջ գ · ֆ ս շ խ հ · վ զ ժ ղ · լ ռ յ; vowels ա a · է ä(æ) · ե e · ի i · ը ı(ɯ) · օ o · ո ö(ø) · ու u · և ü(y). Upstream h ([x~h]) = խ; հ reserved for loans with true [h]. և also = Armenian 'and' — context disambiguates. Hub sample: Օրտատևրկ; native name Ոզտևրկ տիլի / Ոզտևրկճե. Historical precedent: Armeno-Kipchak was Turkic in Armenian letters for centuries (scored 8% in Ortatürk's own similarity survey; Crimean Tatar tops it at 34%).
- Upstream phonology facts (ru.wiki): 9 vowels incl. ä/æ — the user's draft missed ä, fixed by է=ä, ո=ö (user choice). Upstream k/g are palatalized (soft); q/ğ (ğ = Ukrainian-style ɣ) are the back counterparts. Upstream merges x/h as one letter h. v absent from upstream phonetics list but w occurs in examples (kähwe). Pronunciation variability explicitly allowed upstream.
- Upstream grammar facts captured from ru.wiki for the future Morphosyntax page: infinitive -maq/-mek or -ırğa/-irge/.../-rge; deverbal nouns -ma/-me or -uw/-üw/-w; 4 voices (reflexive, passive, reciprocal, causative) + basic; tenses: present indefinite, past categorical, past subjective/evidential, present-future (requests, proverbs: 'Ne ekseñ, şunu orursıñ'), future categorical, present-of-the-moment, past continuous (-a/-e/-y + edi), pluperfect (-ğan/-mış + edi); converbs -ıp/-ip/-up/-üp, -a/-e/-y, -araq/-erek; adjectives inflect only for comparison.
- Gaspirali's "Jalpi Türk" is recorded on the page as the historical predecessor — the name Jalpi is retired for the language itself.
- Known coverage caveat: the 1992 proposal omitted Oghuric (Chuvash), Siberian, and Argu (Khalaj); CORRECTION 2026-10-25 — the VATN/GitHub languages.json includes those branches WITH speaker counts (Chuvash 1.3M, Sakha 0.5M, Khalaj 2k, …) plus ~15 historical languages (Old Turkic, Chagatai, Armeno-Kipchak, Kashgari's Middle Turkic…) at zero speaker weight. Hub wording updated.
- The averaging algorithm (from GitHub selector.js and the TurkLang-2023 proceedings paper): per-character-position vote across cognate rows; each candidate's score = % of languages + % of speakers ('double majority'); a vowel-harmony pass pairs hard aouıqğ vs soft â(ä)öüikg(+e). Paper formulas: variant weight X = 1 − (i−1)/2s; word score F = Σ (1 + Kα/K̄)·Xα. Proceedings PDF (TurkLang 2023, buxdu.uz) scraped to /tmp during the session — the Karimov & Mutalov paper is at its pp. 513–521; turklang.net's own 2018 PDF was unreachable (connection refused).
- Watch out for name clutter: "Öztürkçe" also = Turkish purism reform; "Ortak Türk Tili" (Turkey-backed) is a different, criticized reformed-Turkish project. Our line is Kärimov/Mutalov → VATN → Mireev.
- Roadmap score set to 8 (extant grammar + 16k dictionary + translations; vault adoption pending).

## Open

- Morphosyntax page built 2026-10-25 from the ru.wiki grammar summary. Remaining gap: nominal morphology (cases, plural, possessives) not yet documented — ru.wiki's summary doesn't cover it; Mireev 2023 would.
- No Swadesh or Lexicon pages yet: needs source-gathering from Mireev 2023 and Glosbe.
- Armenian orthography has no texts yet beyond the name samples and the proverb on Morphosyntax.

## Sources harvested (2026-10-25)

- **Karimov & Mutalov 1992, «Ўртатурк тили»** (Tashkent, Mehnat, ~20 pp., print run 10,000) — the foundational pamphlet: the averaging method with a worked example (gapirmoq 'to speak' synonym rows across 5 languages), alphabet policy (one alphabet or several in parallel by agreement), and an English summary ("Ortaturk — the averaged Turkic language"). DOWNLOADED: `files/ortaturk_karimov_mutalov_1992.pdf` + OCR text `files/ortaturk_karimov_mutalov_1992_ocr.txt` (OCR quality mediocre, Uzbek Cyrillic).
- **GitHub AmbientLighter/Ortaturk** (GPL-3.0) — a React app implementing the median-word algorithm: `src/selector.js` is the algorithm, `src/languages.json` the 25-language list. NO lexicon data in the repo.
- **Glosbe `mis_ort`** — VATN word base uploaded Dec 2022; live but JS-rendered; the old gapi endpoint is dead, so no bulk harvest — browser use only.
- **Mireev 2023 *Öztürk Tili*** (Shymkent, 300 pp., ISBN 978-601-7678-55-5; grammar + 16,000-word dictionary + translations) — available on twirpx.com, but behind registration/points; not directly fetchable.
- **ru.wikipedia Среднетюркский язык** — phonetics (captured on Ortatürk/Phonology), grammar summary (captured above), similarity survey (Crimean Tatar closest at 34%, Turkish 28%, Chuvash 3%, Khalaj and Orkhon 1%).
