#!/usr/bin/env python3
import re, sys

UL = "/Users/robertmarshallmurphy/Documents/UL"
DY = "/Users/robertmarshallmurphy/Documents/danayo/lexipedia/Swadesh.md"
MS = "/Users/robertmarshallmurphy/Documents/middle-semitic/Swadesh.md"

def split_row(line):
    # split on unescaped pipes
    parts = re.split(r'(?<!\\)\|', line.strip())
    # drop leading/trailing empties from the outer pipes
    if parts and parts[0] == '': parts = parts[1:]
    if parts and parts[-1] == '': parts = parts[:-1]
    return [p.strip() for p in parts]

def parse_ul_page(path):
    """Return (glosses {num: english}, forms {num: cell}). Only rows inside the
    standard numbered '## N–M' sections count — supplementary tables reuse numbers."""
    glosses, forms = {}, {}
    in_standard = False
    for line in open(path, encoding='utf-8'):
        if line.startswith('##'):
            in_standard = bool(re.match(r'##\s*\d+\s*–\s*\d+', line))
            continue
        if not in_standard or not line.startswith('|'): continue
        cells = split_row(line)
        if len(cells) < 3: continue
        num = cells[0]
        m = re.match(r'(\d+)', num)
        if not m: continue
        n = int(m.group(1))
        if not (1 <= n <= 207): continue
        glosses[n] = cells[1]
        forms[n] = cells[-1]  # target column last, everywhere
    return glosses, forms

def parse_danayo(path):
    glosses, forms = {}, {}
    for line in open(path, encoding='utf-8'):
        if not line.startswith('|'): continue
        cells = split_row(line)
        if len(cells) < 9: continue
        num = cells[0]
        if not num.isdigit(): continue
        n = int(num)
        if not (1 <= n <= 207): continue
        glosses[n] = cells[1]
        cell = cells[8]
        # <ruby>[[我]]<rt>ㄚ</rt></ruby> or <ruby>[彼](../words/彼.md)<rt>ㄅㄜ</rt></ruby>
        m = re.search(r'\[\[([^\]]+)\]\]', cell)
        if not m:
            m = re.search(r'\[([^\]]+)\]\([^)]*\)', cell)
        rt = re.search(r'<rt>(.*?)</rt>', cell)
        if m:
            forms[n] = (f"<ruby>{m.group(1)}<rt>{rt.group(1)}</rt></ruby>" if rt
                        else m.group(1))
        else:
            forms[n] = ''
    return glosses, forms

pages = {
    "Folksprak":       f"{UL}/Folksprak/Swadesh.md",
    "Interlingua":     f"{UL}/Interlingua/Swadesh.md",
    "Interslavic":     f"{UL}/Interslavic/Swadesh.md",
    "Middle Semitic":  MS,  # external: the middle-semitic vault
    "SEDES":           f"{UL}/SEDES/Swadesh.md",
    "Kintu":           f"{UL}/Kintu/Swadesh.md",
}

data = {}
gloss_src = {}
for lang, p in pages.items():
    g, f = parse_ul_page(p)
    data[lang] = f
    gloss_src[lang] = g
dy_g, dy_f = parse_danayo(DY)
data["Dan'a'yo"] = dy_f
gloss_src["Dan'a'yo"] = dy_g

# canonical English: Folksprak first, then Interlingua, MS, SEDES, Interslavic, Dan'a'yo
glosses = {}
for n in range(1, 208):
    for lang in ["Folksprak", "Interlingua", "Middle Semitic", "SEDES", "Interslavic", "Dan'a'yo"]:
        if n in gloss_src[lang]:
            glosses[n] = gloss_src[lang][n]
            break

# diagnostics
for lang in data:
    missing = [n for n in range(1,208) if n not in data[lang]]
    if missing:
        print(f"{lang}: missing rows {missing[:10]}{'...' if len(missing)>10 else ''}", file=sys.stderr)
miss_g = [n for n in range(1,208) if n not in glosses]
if miss_g: print(f"MISSING GLOSSES: {miss_g}", file=sys.stderr)

def cell(lang, n):
    c = data[lang].get(n, '').strip()
    if c in ('', '—', '-', '**—**'): return '—'
    if lang == "Middle Semitic":
        c = c.replace('[[', '').replace(']]', '')  # links would be dead here; the lexicon is in the other vault
    return c

ORDER = ["Dan'a'yo", "Interlingua", "Folksprak", "Interslavic", "Middle Semitic", "SEDES", "Kintu"]

SECTIONS = [
    (1, 21, "Pronouns, deixis and quantifiers"),
    (22, 35, "Numerals and dimensions"),
    (36, 50, "People and animals"),
    (51, 71, "Plants and animal parts"),
    (72, 91, "Body"),
    (92, 107, "Body functions and senses"),
    (108, 125, "Life, conflict, motion and posture"),
    (126, 146, "Handling, speech and change"),
    (147, 159, "Sun, water and ground"),
    (160, 171, "Weather, fire and landscape"),
    (172, 181, "Colors, time and temperature"),
    (182, 200, "Qualities"),
    (201, 207, "Particles and name"),
]

out = []
out.append("# Swadesh\n")
out.append("> Cross-UL basic vocabulary. Hub: [[Universal Languages]] · Compare: [[Language Comparisons]]\n")
out.append("The comparative Swadesh 207 list is the vault's standard core-vocabulary benchmark — filling it is milestone 5 on the [[Development Roadmap]]. Every language's own Swadesh page uses the same layout (Interslavic style): the 207 items in the 13 fixed sets, comparison-language columns first and the target language last, with target forms linked to their lexicon files.\n")
out.append("Below, the seven ULs with any coined forms are shown side by side, one table per set. **—** marks an item not yet coined in that language. Folksprak, Interslavic, Interlingua, SEDES and Kintu forms are live links to their in-vault lexicon pages. Dan'a'yo forms carry their Bopomofo reading in ruby annotation (renders stacked in Reading view) and are unlinked — its completed comparative list lives in its own vault at `lexipedia/Swadesh.md`; Middle Semitic forms are likewise unlinked — its lexicon lives in its own vault at `../middle-semitic`.\n")
out.append("## Where each language stands\n")
out.append("| UL | Page | Status |")
out.append("| --- | --- | --- |")
ms_filled = sum(1 for n in range(1, 208) if cell("Middle Semitic", n) != '—')
out.append("| [[Dan'a'yo]] | `lexipedia/Swadesh.md` in the danayo vault | **Complete** comparative list |")
out.append("| [[Folksprak]] | [[Folksprak/Swadesh]] | №1–143 coined and lexicon-linked; numerals 1–12 done |")
out.append("| [[Interslavic]] | [[Interslavic/Swadesh]] | Comparative page; lexicon links begun |")
out.append(f"| [[Middle Semitic]] | `Swadesh.md` in the middle-semitic vault | Full comparative table (MSA, Hebrew, Syriac, Egyptian, Palestinian); {ms_filled} of 207 Middle Semitic cells filled |")
out.append("| [[Interlingua]] | [[Interlingua/Swadesh]] | Full comparative table (Latin, Portuguese, Spanish, French, Italian, Interlingua) |")
out.append("| [[SEDES]] | [[SEDES/Swadesh]] | Comparative table (Amharic, Somali, Oromo, Beja); SEDES column begun |")
out.append("| [[Kintu]] | [[Kintu/Swadesh]] | Comparative table (Proto-Bantu, Swahili, Kinyarwanda, Lingala, Zulu, Shona, Umbundu); №1–125 coined (34–35, 53, 58 open) |")
out.append("| [[Neo-Sanskrit]] · [[MSEAL]] · [[Indo-Malay]] · [[Guosa]] · [[Ortatürk]] · [[Zens]] · [[Balkan]] · [[Dravindian]] | — | Not started |\n")
out.append("## The 207 in 13 sets\n")

for lo, hi, label in SECTIONS:
    out.append(f"### {lo}–{hi} {label}\n")
    out.append("| № | English | " + " | ".join(ORDER) + " |")
    out.append("| --- | --- | " + " | ".join(["---"]*len(ORDER)) + " |")
    for n in range(lo, hi+1):
        row = [str(n), glosses.get(n, '?')] + [cell(l, n) for l in ORDER]
        out.append("| " + " | ".join(row) + " |")
    out.append("")

with open(f"{UL}/Swadesh.md", "w", encoding='utf-8') as fh:
    fh.write("\n".join(out))
print("written", len(out), "lines")
