---
name: project-neo-sanskrit-decisions
description: Settled design decisions for Neo-Sanskrit (the Indo-Aryan UL) — boundary, breathy-consonant rule, nasal merger, vowels, phonotactics, Kaithi script
metadata:
  type: project
---

# Neo-Sanskrit decisions

**Why:** Neo-Sanskrit design choices are user-settled; don't re-derive or revert them.

**How to apply:**

- Boundary (user): Bengali is excluded from Neo-Sanskrit — it would break too many universals of the remaining group — and belongs with MSEAL instead. Zone is the Indo-Aryan subcontinent (Hindustani, Punjabi, Kashmiri, Garhwali, Rajasthani, Maithili, etc.); Dravidian stays with Dravindian.
- Phonology/orthography (user, 2026-10-24): the full Sanskrit 4×5 stop grid (voiceless/voiced/aspirated/breathy × labial/dental/retroflex/palatal/velar). **Breathy consonants are written with their own letters but no minimal pairs against the plain voiced series may exist.** Retroflex/palatal/velar nasals are one phoneme /ɳ~ɲ~ŋ/; in Kaithi ṇa 𑂝 = ña 𑂖 = ŋa 𑂑 are interchangeable. va /f~ʋ~w/ and ha /h~ɦ/ are marginal. Vowels: a e i o u ṛ (syllabic r survives), ā ī ū, ai au; no syllabic l (Sanskrit ḷ → li). Phonotactics: V/CV/CCV/CVC/CCVC/CVCC/CCVCC.
- Script: Kaithi (eventual). Romanization follows IAST habits. The abugida chart is on the Orthography page: independent vowels 𑂃–𑂌, diacritics 𑂰–𑂸, anusvara 𑂁, visarga 𑂂 (visarga only in Sanskrit words); the diacritic set is called kakahārā (𑂍𑂍𑂯𑂰𑂩𑂰). No flapped-retroflex letters (Kaithi 𑂚 dddha, 𑂜 rha are unused).
- Derivation rules (user, from old wiki notes): weak final schwa deletion; cluster reduction and simplification; keep syllabic ṛ, ḷ → li. "While many languages went through Prakritization, not all did — we make our own rules to get from Sanskrit to today." Zone branches: Central, Dardic, Northern, Northwestern, Southern, Western Indo-Aryan. Pronoun sketch: 1 meṃ/meme, 2 tam/tame, 2 formal ap/apne, 3 ti/te.
- Morphosyntax (user, from old wiki notes): word order SOV (confirmed 2026-10-24; the comparisons matrix already said SOV). Gender is purely formal — consonant-final = masculine, vowel-final = feminine, final -e forbidden on gendered words. Split ergativity by transitivity (not by tense/aspect): intransitive subject unmarked, transitive subject takes ergative ne 𑂢𑂵, transitive object takes accusative ma 𑂧. Postpositions: genitive sa 𑂮, dative na 𑂢, locative me 𑂧𑂵, elative the 𑂟𑂵, benefactive ya 𑂨, comitative soth 𑂮𑂷𑂟𑂹.
- Syllabic ṛ in Kaithi (settled 2026-10-24, user): the convention is borrowed from Tirhuta (which has a true vocalic-ṛ sign) but rendered with **U+0327 combining cedilla**, because Tirhuta codepoints don't render on the user's machine. Mechanics: cedilla under a consonant replaces the inherent a (kṛta = 𑂍̧𑂞); word-initial ṛ = ra + cedilla (ṛṣi = 𑂩̧𑂭𑂱). Romanization stays ṛ. Open: stress unsettled. Fixed while importing the user's chart: the d row had 𑂠𑂲 (dī) duplicated in the i column; correct di is 𑂠𑂱.
