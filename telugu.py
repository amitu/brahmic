# coding=utf-8
from __future__ import unicode_literals

CONSONENTS = {
    'బ': 'ब',
    'భ': 'भ',
    '': 'ह',
    '': 'ङ',
    '': 'ग',
    '': 'घ',
    '': 'द',
    '': 'ध',
    '': 'ज',
    '': 'झ',
    '': 'ड',
    '': 'ढ',
    '': 'प',
    '': 'फ',
    '': 'र',
    '': 'ऱ',
    '': 'क',
    '': 'ख',
    '': 'त',
    '': 'थ',
    '': 'च',
    '': 'छ',
    '': 'ट',
    '': 'ठ',
    '': 'म',
    '': 'ण',
    '': 'न',
    '': 'ऩ',
    '': 'व',
    '': 'ऴ',
    '': 'ल',
    '': 'ळ',
    '': 'स',
    '': 'श',
    '': 'ष',
    '': 'य',
    '': 'य़',
}

HALF_CONSONENTS = dict(t + '్' for t in CONSONENTS)
VOWELS = {}

mapping = CONSONENTS
mapping.update()
reverse_mapping = {}


def create_reverse_mapping():
    for k, v in mapping.items():
        reverse_mapping[v] = k


def to_devnagri(text):
    pass


def from_devnagri(text):
    pass


create_reverse_mapping()
