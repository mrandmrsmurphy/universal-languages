#!/usr/bin/env python3
"""Regenerate AIOS/facts.yaml (reportage protocol: outside agents read it instead of prose counts).
Run from anywhere: python3 AIOS/scripts/build_facts.py
Counts come from `git ls-files -z` (tracked files only; handles non-ASCII names)."""
import subprocess, datetime, pathlib

root = pathlib.Path(__file__).resolve().parents[2]
files = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True, check=True).stdout.decode().split("\0")
files = [f for f in files if f]
md = [f for f in files if f.endswith(".md")]

# Language subtrees = top-level folders holding a hub page of the same name
langs = sorted({f.split("/")[0] for f in md if "/" in f and f.split("/")[1] == f.split("/")[0] + ".md"})
lex = {l: sum(1 for f in md if f.startswith(f"{l}/Lexicon/") and f.count("/") == 2 and not f.endswith("Lexicon.md")) for l in langs}

out = ["# Machine-readable vault facts for outside agents. Regenerate: AIOS/scripts/build_facts.py",
       "vault: UL", "project: Universal Languages", "hub: Universal Languages.md", "counts:",
       f"  markdown_pages: {len(md)}",
       f"  languages_with_subtree: {len(langs)}",
       "lexicon_entries_in_vault:"]
out += [f"  {l}: {n}" for l, n in lex.items() if n]
out += ["sibling_vaults:",
        "  danayo: https://github.com/mrandmrsmurphy/danayo",
        "  middle-semitic: https://github.com/mrandmrsmurphy/middle-semitic",
        "key_pages:",
        "  hub: Universal Languages.md", "  comparison: Language Comparisons.md", "  swadesh: Swadesh.md",
        "  roadmap: Development Roadmap.md", "  design_philosophy: Design Philosophy.md",
        "  site_map: AIOS/site-map.md", "  memory_index: AIOS/memory-index.md",
        "source_record: none",
        f"generated: {datetime.date.today().isoformat()}"]
(root / "AIOS" / "facts.yaml").write_text("\n".join(out) + "\n")
