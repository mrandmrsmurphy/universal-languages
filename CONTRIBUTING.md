# Contributing

Corrections, sources and design discussion for the Universal Languages vault are welcome. This repository is the parent of the project: it holds the shared pages and the thirteen language subtrees still incubating here. Two languages have their own repositories, and contributions to them go there:

- **Dan'a'yo**: https://github.com/mrandmrsmurphy/danayo
- **Middle Semitic**: https://github.com/mrandmrsmurphy/middle-semitic

## How it works

1. **Propose through a pull request** (or an issue, for a question or suggestion). Describe what you changed and why.
2. **The maintainer reviews all contributions.** Nothing is merged unseen. A design decision may already be settled (see [AIOS/memory](AIOS/memory/) for the standing decisions per language) or may be one the maintainer wants to make.
3. **Vetted contributors can be given direct access** once their work has been reviewed and found careful.

## Where help is most useful

- **Source checks.** Cognates, correspondences, population figures and boundary claims, each with a citation.
- **Native-reader checks.** Source-language forms in the Swadesh tables.
- **Gaps in the Swadesh list and lexicons.** See [Swadesh](Swadesh.md) and each language's Lexicon.
- **Maps and flags.** Freely licensed replacements for any image listed as unverified in [ATTRIBUTION](ATTRIBUTION.md).
- **Errors.** A wrong form, a broken table, a link that does not resolve.

## Standards

- **Content pages describe the current state only.** No dates, no "decided by", no correction narratives. History goes in [`logs/log.md`](logs/log.md), which is append-only.
- **Cite evidence.** Do not invent a cognate to fill a gap. If a form is only supposed, say so tersely on the page.
- **Follow the conventions of the language's subtree**: lexicon entry format, Swadesh page layout, filenames (runic for Folksprak, Cyrillic for Interslavic). Look at an existing page first.
- **Accessible charts and maps.** Use colour-blind-safe palettes.
- **Escape pipes** inside table embeds (`![[file\|60]]`).
- **Keep `CLAUDE.md` and `AGENTS.md` byte-identical** if you change either.
- **Say if AI helped.** Note it in the pull request, and check what the assistant gave you.

## Licence

By contributing you agree that your contribution is licensed under [CC BY-SA 4.0](LICENSE), like the rest of the repository. Do not contribute images or text you do not have the right to share under that license.
