# coding=utf-8
from __future__ import unicode_literals

CONSONENTS = [
    'ब',
    'भ',
    'ह',
    'ङ',
    'ग',
    'घ',
    'द',
    'ध',
    'ज',
    'झ',
    'ड',
    'ढ',
    'प',
    'फ',
    'र',
    'ऱ',
    'क',
    'ख',
    'त',
    'थ',
    'च',
    'छ',
    'ट',
    'ठ',
    'म',
    'ण',
    'न',
    'ऩ',
    'व',
    'ऴ',
    'ल',
    'ळ',
    'स',
    'श',
    'ष',
    'य',
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
    'ए',
    'ऐ',
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
    'ए': 'े',
    'ऐ': 'ै',
    'ओ': 'ो',
    'औ': 'ौ',
    'ऑ': 'ॉ',
}


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
