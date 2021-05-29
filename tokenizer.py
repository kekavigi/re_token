"""
Tokenisasi dengan Regular Expression.
Merujuk pada PUEBI, dengan beberapa perluasan.
"""

import re

PARAGRAPH_SEPARATOR = '\n\n' # atau '\n'


# TODO: https://stackoverflow.com/questions/42742810/speed-up-millions-of-regex-replacements-in-python-3/42789508#42789508
with open('abbrwords.txt', 'r') as f:
    tmp = set(f.read().split('\n')) - {''}
ABBREV = r'\b(?:%s)' % r'|'.join(tmp)
ABBREV = ABBREV.replace(r'.', r'\.')

with open('affwords.txt', 'r') as f:
    tmp = set(f.read().split('\n')) - {''}
AFFIX = r'\b(?:%s)\b' % r'|'.join(tmp)


#
# TODO: phonenum, normalize singkatan umum (bulan, 'yg.'),

# https://www.geeksforgeeks.org/python-check-url-string/
# dimodifikasi agar hanya menampilkan group pertama
URLS = r"(?i)\b(?:(?:https?:\/\/|www\d{0,3}[.]|[a-z0-9.\-]+" +\
    r"[.][a-z]{2,4}""\/)(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\(" +\
    r"?:[^\s()<>]+\)))*\))+(?:\((?:[^\s()<>]+|(?:\([^\s()<>" +\
    r"] +\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

def tokenize(text):
    ''' Memroses tokenisasi terkait bentuk-bentuk umum. '''

    regexes = [
        URLS,
        # Format email
        r'[\w.+-]+@[\w-]+\.(?:[\w-]\.?)+[\w-]',
        # Format jam, III.A.3.
        r'\d{2}\.\d{2}\.\d{2}',
        # Format tanda hubung: III.E.2., III.E.3., III.E.4., III.E.5. III.E.6.
        r'(?:[a-zA-Z]+(?:-[a-zA-Z]+)+)',
        # Format bilangan ribuan, III.A.5.
        # ditambah kemungkinan desimal, cth: 213.126,56
        # kemungkinan simbol positif dan negatif tidak diurus
        #   karena tanda kurang sama dengan tanda hubung, cth 2013-2014
        #   secara tidak langsung mengurus format penggunaan tanda
        #   hubung sebagai saltik dari tanda pisah, III.F.3.
        # ditambah bentuk umum \d+
        r'(?:\d{4,}|(?:\d{1,3}(?:\.\d{3})*))(?:\,\d*)?',
        # urus kemungkinan kasus II.H.3., II.H.4. II.H.1.
        ABBREV, r'\b[A-Z]\.',
        # Format III.E.7.
        AFFIX,
        # Format III.G.2., III.I.1., III.I.2.
        #   simbol -- sebagai subtitusi tanda pisah
        #   simbol-simbol lainnya sebagai token
        #   TODO: respect word boundaries
        r'(?:%s)' % r'|'.join(r'''\(\?\) \.{3} -- \n \. \, ; : \! " ' \? \( \) [ ] / —'''.split(' ')),
        #karakter non-spasi yang tersisa sebagai token
        r'(?:[a-zA-Z]+)', r'(?:\S)',
    ]

    patterns = re.compile(r'(%s)' % '|'.join(regexes), re.VERBOSE)

    #text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(“|”|")', r'"', text)
    text = re.sub(r'\(\s*\?\s*\)', '(?)', text)

    tokens = patterns.findall(text)
    return tokens
