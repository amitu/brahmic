# coding=utf-8
from __future__ import unicode_literals

CONSONENTS = [
    'क',
    'ख',
    'ग',
    'घ',
    'ङ',
    'च',
    'छ',
    'ज',
    'झ',
    'ञ',
    'ट',
    'ठ',
    'ड',
    'ढ',
    'ण',
    'त',
    'थ',
    'द',
    'ध',
    'न',
    'प',
    'फ',
    'ब',
    'भ',
    'म',
    'य',
    'र',
    'ल',
    'व',
    'श',
    'ष',
    'स',
    'ह',
    'ळ',
    'ऱ',
    'ऩ',
    'ऴ',
    'य़',
]

HALF_CONSONENTS = [c + '्' for c in CONSONENTS]

VOWELS = [
    'अ',
    'आ',
    'इ',
    'ई',
    'उ',
    'ऊ',
    'ऋ',
    'ऎ',
    'ए',
    'ऐ',
    'ऒ',
    'ओ',
    'औ',
    'ऑ',
]

VOWELS_MATRA = {
    'अ': '',
    'आ': 'ा',
    'इ': 'ि',
    'ई': 'ी',
    'उ': 'ु',
    'ऊ': 'ू',
    'ऋ': 'ृ',
    'ऎ': 'ॆ',
    'ए': 'े',
    'ऐ': 'ै',
    'ऒ': 'ॊ',
    'ओ': 'ो',
    'औ': 'ौ',
    'ऑ': 'ॉ',
    'अं': 'ं',
    'अः': 'ः',
}

DIGITS = '०१२३४५६७८९'


def is_vowel(l):
    # print l, l in VOWELS
    return l in VOWELS


def is_consonent(l):
    # print l, l in CONSONENTS, l in HALF_CONSONENTS
    return l in CONSONENTS or l in HALF_CONSONENTS


def add_vowel(c, v):
    # print "add_vowel", c, v
    if c in HALF_CONSONENTS:
        c = c[:-1]
    # print "add_vowel", c, v, c+VOWELS_MATRA.get(v, v)
    return c+VOWELS_MATRA.get(v, v)
