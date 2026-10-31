#!/usr/bin/env python3 -I
"""Print the WALS daughter-language table for one UL's Anthropology page.

Usage: python3 -I build_daughter_table.py WALS_CLDF_DIR UL_NAME
WALS_CLDF_DIR = the `cldf/` folder of github.com/cldf-datasets/wals.
Blank cells = not coded in WALS. UL column values come from the UL's own pages
(fall back to the Language Comparisons matrix); edit CONFIG below per UL.
"""
import csv, sys, os

ROWS = [('Word order (WALS 81A)', '81A'), ('Evidentiality (WALS 78)', '78A'), ('Cases', '49A'),
        ('Relative clause', '90A'), ('Gender', '30A'), ('Tone / pitch accent', '13A'),
        ('Definite article (WALS 37)', '37A'), ('Indefinite article (WALS 38)', '38A'),
        ('Clusivity', '39A'), ('Typology', '20A'), ('Perfective/imperfective affix', '65A'),
        ('Reduplication (WALS 27)', '27A'), ('Vowels', '2A'), ('Stress', '14A'),
        ('Morphosyntactic alignment', '98A'), ('T–V / politeness', '45A'),
        ('Polar question particle', '116A'), ('Future as verbal affix', '67A'), ('Negation', '112A')]

SHORT = {
    'Part of the tense system': 'Yes (tense system)', 'Grammatical marking': 'Yes',
    'No grammatical marking': 'No', 'Nominative - accusative (standard)': 'NA',
    'No inflectional future': 'No', 'Inflectional future exists': 'Yes', 'No tones': 'No',
    'Productive full and partial reduplication': 'Yes', 'Exclusively concatenative': 'Concat.',
    'Noun-Relative clause': 'post', 'Relative clause-Noun': 'ante', 'Question particle': 'Yes',
    'Interrogative intonation only': 'No (intonation)', 'No inclusive/exclusive': 'No',
    'None': '0', 'Two': '2', 'Three': '3', 'Binary politeness distinction': 'Yes',
    'No politeness distinction': 'No', 'Ultimate': 'R', 'Initial': 'L', 'No fixed stress': 'No fixed',
    'Negative affix': 'VA', 'Negative particle': 'particle', '[Neg-V]': 'Neg-V', 'NegV': 'Neg-V',
    'Average (5-6)': '5–6', 'Large (7-14)': '7+', 'Small (2-4)': '2–4',
    'No definite, but indefinite article': 'No', 'No definite or indefinite article': 'No',
    "Indefinite word distinct from 'one'": 'Yes', 'Definite affix': 'Yes (affix)',
    'Indefinite affix': 'Yes (affix)', 'Definite word distinct from demonstrative': 'Yes',
    'Demonstrative word used as definite article': 'Yes (demonstrative)',
    'Interrogative verb morphology': 'Verb morphology', 'No dominant order': 'No dominant',
    'No grammatical evidentials': 'No', 'Modal morpheme': 'Yes (modal)', 'Separate particle': 'Yes (particle)',
    'Mixed': 'Yes (mixed)', 'Simple tone system': 'Simple tone', "Indefinite word same as 'one'": 'Some',
    'No indefinite, but definite article': 'No', 'No productive reduplication': 'No',
    'Interrogative word order': 'No (word order)', 'Ergative - absolutive': 'Erg', 'Active-inactive': 'Active',
    'Four': '4', 'Variation between negative word and affix': 'varies',
    'Absence of declarative morphemes': 'No (decl. absent)', 'Five or more': '5+', "'We' the same as 'I'": 'No (we = I)',
    'Isolating/concatenative': 'Isol./concat.', 'Negative auxiliary verb': 'aux. verb', 'Correlative': 'correl.', 'Tripartite': 'Tri',
    'Mixture of previous two types': 'mixed', 'Inclusive/exclusive': 'Yes',
    'Pronouns avoided for politeness': 'Yes (avoidance)', 'Penultimate': 'Penult.', 'Complex tone system': 'Yes (complex)',
    'Tonal/isolating': 'Isolating', 'Exclusively isolating': 'Isolating',
    'Nominative - accusative (marked nominative)': 'NA (marked nom.)',
    'Negative word, unclear if verb or particle': 'word', 'Verbal affix or clitic': 'Yes (affix)',
    'Multiple politeness distinctions': 'Yes (multiple)', 'Full reduplication only': 'Yes (full only)',
}

CONFIG = {
    'Zens': dict(
        langs=[('prs', 'Persian'), ('taj', 'Tajik'), ('psh', 'Pashto'), ('krd', 'Kurdish (Central)'),
               ('kji', 'Kurmanji'), ('blc', 'Balochi'), ('oss', 'Ossetic'), ('wak', 'Wakhi'), ('zaz', 'Zazaki')],
        ul={'81A': 'SOV', '78A': 'Yes', '49A': '3 (ø, -ra, -(y)a)', '90A': 'post', '30A': '0', '13A': 'No',
            '37A': 'No', '38A': 'Some', '39A': 'No', '20A': 'A', '65A': 'Yes', '27A': 'Yes', '2A': '6',
            '14A': 'R', '98A': 'Tri', '45A': 'Yes', '116A': 'Yes', '67A': 'Yes', '112A': 'VA'}),
    'Folksprak': dict(
        langs=[('eng', 'English'), ('ger', 'German'), ('dut', 'Dutch'), ('afr', 'Afrikaans'),
               ('fri', 'Frisian'), ('swe', 'Swedish'), ('nor', 'Norwegian'), ('dsh', 'Danish'),
               ('ice', 'Icelandic')],
        ul={'81A': 'V2', '78A': 'No', '49A': 'pro', '90A': 'post', '30A': '0', '13A': 'No', '37A': 'Yes',
            '38A': 'Some', '39A': 'No', '20A': 'F', '27A': 'No', '2A': '7', '14A': 'L', '98A': 'NA',
            '116A': 'No (word order)', '67A': 'No', '112A': 'particle'}),
    'Dravindian': dict(
        langs=[('tml', 'Tamil'), ('tel', 'Telugu'), ('knd', 'Kannada'), ('mym', 'Malayalam'),
               ('tul', 'Tulu'), ('gon', 'Gondi')],
        ul={'81A': 'SOV', '78A': 'No', '49A': '8', '90A': 'post', '30A': '3', '13A': 'No', '37A': 'No',
            '38A': 'No', '39A': 'Yes', '20A': 'A', '65A': 'Yes', '27A': 'Yes', '2A': '5', '14A': 'R',
            '98A': 'NA', '45A': 'Yes', '116A': 'No (verb)', '67A': 'Yes', '112A': 'VA'}),
    'Balkan': dict(
        langs=[('grk', 'Greek'), ('tur', 'Turkish'), ('alb', 'Albanian'), ('scr', 'Serbo-Croatian'),
               ('bul', 'Bulgarian'), ('mcd', 'Macedonian'), ('rom', 'Romanian')],
        ul={'81A': 'SVO', '78A': 'No', '49A': '3', '90A': 'post', '30A': '3', '13A': 'No', '37A': 'Yes',
            '38A': 'Some', '39A': 'No', '20A': 'F', '65A': 'Yes', '27A': 'No', '2A': '6', '14A': 'R',
            '98A': 'NA', '45A': 'Yes', '116A': 'Yes', '67A': 'No', '112A': 'particle'}),
    'Guosa': dict(
        langs=[('yor', 'Yoruba'), ('igb', 'Igbo'), ('akn', 'Akan'), ('hau', 'Hausa'), ('wlf', 'Wolof')],
        ul={'81A': 'SVO', '78A': 'No', '49A': '0', '90A': 'post', '30A': '0', '13A': 'Yes', '39A': 'Yes',
            '20A': 'I', '27A': 'Yes', '2A': '5', '14A': 'weight', '98A': 'NA', '116A': 'Yes', '67A': 'Yes'}),
    'Interlingua': dict(
        langs=[('spa', 'Spanish'), ('fre', 'French'), ('por', 'Portuguese'), ('ita', 'Italian'),
               ('ctl', 'Catalan'), ('rom', 'Romanian')],
        ul={'81A': 'SVO', '78A': 'No', '49A': 'pro', '90A': 'post', '30A': '0 (pronouns 2)', '13A': 'No',
            '37A': 'Yes', '38A': 'Some', '39A': 'No', '20A': 'F', '65A': 'No', '27A': 'No', '2A': '5',
            '14A': 'R', '98A': 'NA', '45A': 'Yes', '116A': 'Yes', '67A': 'Yes', '112A': 'particle'}),
    'Indo-Malay': dict(
        langs=[('ind', 'Indonesian'), ('mly', 'Malay'), ('jav', 'Javanese'), ('sun', 'Sundanese'),
               ('bal', 'Balinese'), ('bug', 'Bugis'), ('mks', 'Makassar'), ('tag', 'Tagalog'),
               ('ceb', 'Cebuano'), ('ilo', 'Ilocano'), ('hil', 'Hiligaynon'), ('kpm', 'Kapampangan'),
               ('pnn', 'Pangasinan'), ('bkl', 'Bikol')],
        ul={'81A': 'SVO', '78A': 'No', '49A': '0', '90A': 'post', '13A': 'No', '38A': 'Some', '39A': 'Yes',
            '20A': 'A', '65A': 'No', '27A': 'Yes', '2A': '6', '14A': 'R', '98A': 'NA', '45A': 'Yes',
            '116A': 'Yes', '67A': 'No', '112A': 'particle'}),
    'Interslavic': dict(
        langs=[('rus', 'Russian'), ('pol', 'Polish'), ('cze', 'Czech'), ('svk', 'Slovak'), ('ukr', 'Ukrainian'),
               ('blr', 'Belarusian'), ('srb', 'Sorbian')],
        ul={'81A': 'SVO', '78A': 'No', '49A': '6', '90A': 'post', '30A': '3', '13A': 'No', '37A': 'No',
            '38A': 'No', '39A': 'No', '20A': 'F', '65A': 'Yes', '27A': 'No', '2A': '6', '14A': 'weight',
            '98A': 'NA', '45A': 'Yes', '116A': 'Yes', '67A': 'No', '112A': 'particle'}),
    'Neo-Sanskrit': dict(
        langs=[('hin', 'Hindi'), ('urd', 'Urdu'), ('pan', 'Panjabi'), ('mhi', 'Marathi'), ('guj', 'Gujarati'),
               ('nep', 'Nepali'), ('kas', 'Kashmiri'), ('sdh', 'Sindhi'), ('mai', 'Maithili'), ('snh', 'Sinhala')],
        ul={'81A': 'SOV', '78A': 'No', '49A': '4', '90A': 'correl.', '30A': '2', '13A': 'No', '37A': 'No',
            '38A': 'No', '39A': 'No', '20A': 'A', '65A': 'Yes', '27A': 'Yes', '2A': '7+', '14A': 'weight',
            '98A': 'Split', '45A': 'Yes (strong)', '116A': 'Yes', '67A': 'Yes', '112A': 'particle'}),
    'Middle Semitic': dict(
        langs=[('ams', 'Arabic (MSA)'), ('aeg', 'Arabic (Egyptian)'), ('asy', 'Arabic (Syrian)'),
               ('arg', 'Arabic (Gulf)'), ('arq', 'Arabic (Iraqi)'), ('amr', 'Arabic (Moroccan)'),
               ('heb', 'Hebrew'), ('naj', 'Neo-Aramaic (Arbel)')],
        ul={'81A': 'SVO', '78A': 'No', '49A': '0', '90A': 'post', '30A': '2', '13A': 'No', '37A': 'Yes',
            '38A': 'Some', '39A': 'No', '20A': 'F', '65A': 'No', '27A': 'No', '2A': '5', '14A': 'R',
            '98A': 'NA', '45A': 'Yes', '116A': 'Yes', '67A': 'No', '112A': 'particle'}),
    'SEDES': dict(
        langs=[('orh', 'Oromo (Harar)'), ('amh', 'Amharic'), ('som', 'Somali'), ('tig', 'Tigrinya'),
               ('tgr', 'Tigre'), ('wly', 'Wolaytta'), ('chh', 'Gurage (Chaha)')],
        ul={'81A': 'SOV', '78A': 'No', '49A': '2', '90A': 'ante', '30A': '2', '13A': 'No', '37A': 'Yes',
            '38A': 'No', '39A': 'No', '20A': 'A', '65A': 'No', '27A': 'Yes', '2A': '5', '14A': 'none',
            '98A': 'NA (marked nom.)', '45A': 'No', '116A': 'Yes', '67A': 'Yes', '112A': 'particle'}),
    'Ortatürk': dict(
        langs=[('tur', 'Turkish'), ('aze', 'Azerbaijani'), ('uzb', 'Uzbek'), ('kgz', 'Kyrgyz'), ('tvo', 'Tatar'),
               ('bsk', 'Bashkir'), ('tkm', 'Turkmen'), ('uyg', 'Uyghur'), ('kkp', 'Karakalpak'),
               ('chv', 'Chuvash'), ('ykt', 'Yakut')],
        ul={'81A': 'SOV', '78A': 'Yes (tense)', '49A': '7', '90A': 'ante', '30A': '0', '13A': 'No', '37A': 'Yes',
            '38A': 'Some', '39A': 'No', '20A': 'A', '65A': 'No', '27A': 'No', '2A': '7+', '14A': 'weight',
            '98A': 'NA', '45A': 'Yes', '116A': 'Yes', '67A': 'Yes', '112A': 'VA'}),
    'MSEAL': dict(
        langs=[('vie', 'Vietnamese'), ('tha', 'Thai'), ('lao', 'Lao'), ('khm', 'Khmer'), ('brm', 'Burmese'),
               ('cnt', 'Cantonese'), ('mnd', 'Mandarin'), ('hak', 'Hakka'), ('hok', 'Hokkien'),
               ('hmo', 'Hmong'), ('mie', 'Mien'), ('chw', 'Cham (Western)'), ('sha', 'Shan'), ('ben', 'Bengali')],
        ul={'81A': 'SVO', '78A': 'Yes (particle)', '49A': '0', '90A': 'post', '30A': '0', '13A': 'Yes',
            '37A': 'No', '38A': 'Some', '39A': 'Yes', '20A': 'I', '65A': 'No', '27A': 'Yes', '2A': '6',
            '14A': 'weight', '98A': 'NA', '45A': 'Yes', '116A': 'Yes', '67A': 'No', '112A': 'particle'}),
    'Kintu': dict(
        langs=[('swa', 'Swahili'), ('kik', 'Kikuyu'), ('kin', 'Kinyarwanda'), ('lda', 'Luganda'),
               ('lin', 'Lingala'), ('kon', 'Kongo'), ('cil', 'CiLuba'), ('bem', 'Bemba'), ('shn', 'Shona'),
               ('cic', 'Chichewa'), ('zul', 'Zulu'), ('xho', 'Xhosa'), ('ses', 'Sesotho'), ('umb', 'Umbundu')],
        ul={'81A': 'SVO', '78A': 'No', '49A': '0', '90A': 'post', '30A': '10 (classes)', '13A': 'Yes',
            '37A': 'Yes', '38A': 'No', '39A': 'No', '20A': 'A', '65A': 'Yes', '27A': 'Yes', '2A': '7+',
            '14A': 'weight', '98A': 'NA', '45A': 'No', '116A': 'Yes', '67A': 'Yes', '112A': 'VA'}),
    'Caucas': dict(
        langs=[('geo', 'Georgian'), ('chc', 'Chechen'), ('ava', 'Avar'), ('aze', 'Azerbaijani'),
               ('arm', 'Armenian'), ('rus', 'Russian'), ('kab', 'Kabardian'), ('abk', 'Abkhaz'),
               ('lez', 'Lezgian'), ('oss', 'Ossetic'), ('krc', 'Karachay-Balkar'), ('ing', 'Ingush'),
               ('lak', 'Lak')],
        ul={'81A': 'SOV', '78A': 'No', '49A': '10', '90A': 'ante', '30A': '0', '39A': 'No', '20A': 'A',
            '65A': 'Some', '2A': '6', '14A': 'weight', '98A': 'Erg', '45A': 'Yes', '116A': 'No (verb)',
            '67A': 'Yes', '112A': 'particle'}),
}


def main(wals, name):
    cfg = CONFIG[name]
    codes = {r['ID']: r['Name'] for r in csv.DictReader(open(os.path.join(wals, 'codes.csv')))}
    vals = {(r['Language_ID'], r['Parameter_ID']): codes.get(r['Code_ID'], r['Value'])
            for r in csv.DictReader(open(os.path.join(wals, 'values.csv')))}

    def cell(lang, p):
        v = vals.get((lang, p))
        if v is None:
            return ''
        if p == '49A':
            return '0' if v.startswith('No') else v.split()[0].replace('-', '–')
        if p == '90A' and v == 'Mixed':
            return 'mixed'
        return SHORT.get(v, v)

    langs = cfg['langs']
    print('| Feature | ' + ' | '.join(n for _, n in langs) + f' | **{name}** |')
    print('| ' + ' | '.join(['---'] * (len(langs) + 2)) + ' |')
    for label, p in ROWS:
        print(f'| {label} | ' + ' | '.join(cell(l, p) for l, _ in langs) + f' | {cfg["ul"].get(p, "")} |')


if __name__ == '__main__':
    main(*sys.argv[1:3])
