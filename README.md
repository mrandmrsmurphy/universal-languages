# Universal Languages

An [Obsidian](https://obsidian.md) vault documenting the **Universal Languages** project: fifteen regional auxiliary languages (conlangs/auxlangs), each derived from a proto-language or a sprachbund, plus cross-language comparison material.

Rather than one world language, the idea is one modest, easy-to-learn bridge language per region. Each unifies a group of related or neighbouring peoples, eases learning of the region's natural languages, and clarifies regional identity. The full pitch is in [`Universal Languages.md`](Universal%20Languages.md).

## The fifteen

| Language | Foundation | Where |
| --- | --- | --- |
| Dan'a'yo | Classical Chinese | East Asia (own vault, see below) |
| Neo-Sanskrit | Sanskrit | Indo-Aryan |
| Interlingua | Proto-Romance | Romance |
| Folksprak | Proto-Germanic | Germanic |
| Kintu | Proto-Bantu | Bantu |
| Indo-Malay | Proto-Malayo-Polynesian | Maritime Southeast Asia |
| Guosa | Proto-Niger-Congo | West Africa |
| Interslavic | Proto-Slavic | Slavic |
| Middle Semitic | Proto-Semitic | Semitic (own vault, see below) |
| MSEAL | Sprachbund | Mainland Southeast Asia |
| Dravindian | Proto-Dravidian | Dravidian |
| Zens | Proto-Iranian | Iranian |
| Ortatürk | Turkic (statistical average) | Turkic |
| SEDES | Sprachbund | Horn of Africa |
| Balkan | Sprachbund | Balkans |

Interlingua, Interslavic, Guosa and Ortatürk are existing external projects that the vault adopts and documents; the rest are designed here. Smaller sketches outside the core fifteen: Samboka, Caucas, Qinghai.

## Getting started

1. Clone the repo and open the folder as a vault in Obsidian (**Open folder as vault**).
2. Start at [`Universal Languages.md`](Universal%20Languages.md), then browse [`Language Comparisons.md`](Language%20Comparisons.md), [`UL Map.md`](UL%20Map.md), [`Swadesh.md`](Swadesh.md) and [`Development Roadmap.md`](Development%20Roadmap.md).
3. Each language has a folder with a hub page of the same name (e.g. `Folksprak/Folksprak.md`) and, as far as it has progressed, Anthropology, Phonology, Orthography, Morphosyntax, Swadesh and Lexicon pages.

The vault uses `[[wikilinks]]` and embedded images, so it reads best in Obsidian; on GitHub the Markdown is readable but links and embeds will not resolve.

## Layout

```
Universal Languages.md   hub page
Language Comparisons.md  cross-UL feature matrix
Swadesh.md               cross-UL Swadesh tables
<Language>/              one subtree per language
files/                   flags, maps, images, reference sources
AIOS/                    project memory, site map, build scripts
logs/log.md              append-only history of changes and decisions
```

- Content pages describe **current state only**; history lives in `logs/log.md`.
- `AIOS/site-map.md` tracks the status of every section.
- `AIOS/scripts/` holds the Python scripts that generate the Swadesh and daughter-language tables.
- `CLAUDE.md` and `AGENTS.md` are identical instruction files for AI coding agents working in the vault.

## Related vaults

Two languages have outgrown this vault and live in their own repositories, which this vault's hub pages point to:

- **Dan'a'yo**: the flagship, furthest-along language.
- **Middle Semitic**: lexicon, root pages, grammar and Swadesh.

Their hub pages here (`Dan'a'yo.md`, `Middle Semitic.md`) are summaries only.

## Contributing

Corrections, sources and design discussion are welcome via issues and pull requests. Please keep content pages free of dates and decision narratives (see above), and cite sources for linguistic claims.

## License and credits

Original text and design: [CC BY-SA 4.0](LICENSE).

Flags, maps and other third-party images keep their own licenses and authorship; see [`ATTRIBUTION.md`](ATTRIBUTION.md) and [`files/maps/Credits.md`](files/maps/Credits.md). Some reference files are not redistributed and are excluded via `.gitignore`.
