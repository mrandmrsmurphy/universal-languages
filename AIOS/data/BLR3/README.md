# BLR3 — local reference copy

Local copy of **Bantu Lexical Reconstructions 3** (Bastin, Coupez, Mumba & Schadeberg, eds., 2002, Royal Museum for Central Africa, Tervuren), downloaded from the [AfricaMuseum site](https://www.africamuseum.be/en/research/discover/human_sciences/culture_society/blr) (database last updated 2005-11-06). Used as the Proto-Bantu source for Kintu coinage.

The `.USR` files are FileMaker 5 data and are **gitignored** (not ours to redistribute); the strings dumps exist for grepping. Cite the editors, not this copy. If this folder is missing, re-download `BLR3.zip` from the museum page and re-run: `strings -n 4 Reconst.USR > Reconst.strings.txt` (same for MGRefl).

## Files

- `Reconst.USR` / `Reconst.strings.txt` — the ~10,000 Proto-Bantu reconstructions (roots and derived stems)
- `MGRefl.USR` / `MGRefl.strings.txt` — daughter-language reflexes, for the recognition check
- `ReadMe.txt` — the editors' original readme

## Reading the dump

The app displayed text in a custom font (BantuPhon), so the raw bytes use an ASCII stand-in encoding:

- `I` = ɪ, `U` = ʊ (the second-degree vowels), `E` = ɛ
- `C` = c (the palatal stop; Kintu s), `J` = the palatal voiced stop (Guthrie's j)
- doubled vowels = PB length
- glosses are in **French**; `voir fiche N` = cross-reference to record N
- **tone does not survive** strings extraction (it lived in the font) — verify a root's H/L on the website before coining its acute

Protoform lines are root families: `bond` = *-bònd-, with `bonId` applicative, `bonIk` potential, `bondUk` reversive-intransitive, etc.
