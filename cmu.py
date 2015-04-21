# coding=utf-8
from __future__ import unicode_literals

cmu_dict = {}


def populate_cmu():
    for line in file("./cmudict/cmudict.dict"):
        if line[0] == ";":
            continue
        try:
            parts = line.split(u" ", 1)
        except UnicodeDecodeError:
            print "skipping", line
        else:
            cmu_dict[parts[0].lower()] = parts[1][:-1]


def lookup(word):
    if not cmu_dict:
        populate_cmu()
    return cmu_dict.get(word, "unknown")


hin_dict = """
AA  odd     AA D      | ऑ
AE  at  AE T          | ऐ
AH  hut HH AH T       | ऽ
AH0  hut HH AH T      | ए
AH1  hut HH AH T      | आ
AO  ought   AO T      | आ
AW  cow K AW          | आव
AY  hide    HH AY D   | आय
B   be  B IY          | ब
CH  cheese  CH IY Z   | च
D   dee D IY          | ड
DH  thee    DH IY     | द
EH  Ed  EH D          | ए
ER  hurt    HH ER T   | र
EY  ate EY T          | एऽ
F   fee F IY          | फ
G   green   G R IY N  | ग
HH  he  HH IY         | ह
IH  it  IH T          | इ
IY  eat IY T          | ई
JH  gee JH IY         | ज
K   key K IY          | क
L   lee L IY          | ल
M   me  M IY          | म
N   knee    N IY      | न
NG  ping    P IH NG   | गं
OW  oat OW T          | ओ
OY  toy T OY          | ऑय
P   pee P IY          | प
R   read    R IY D    | र
S   sea S IY          | स
SH  she SH IY         | श
T   tea T IY          | ट
TH  theta   TH EY T AH| थ
UH  hood    HH UH D   | उ
UH  hood    HH UH D   | ऊ
UW  two T UW          | उ
UW1  two T UW         | ऊ
V   vee V IY          | व
W   we  W IY          | व
Y   yield   Y IY L D  | य
Z   zee Z IY          | ज़
"""

hin_dict = dict(
    (line.split()[0], line.split()[-1])
    for line in hin_dict.splitlines() if line.strip()
)


def trans_lookup(phoneme):
    return hin_dict.get(phoneme, hin_dict.get(phoneme[:-1], phoneme))


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
    # print "add_vowel", c, v
    return c+VOWELS_MATRA.get(v, v)


def trans(cmu):
    cmu = "".join(trans_lookup(m) for m in cmu.split())
    hi = []
    for i in range(len(cmu)):
        l = trans_lookup(cmu[i])
        if i > 0 and is_vowel(l) and is_consonent(hi[-1]):
            hi[-1] = add_vowel(hi[-1], l)
        else:
            hi.append(l)
    return "".join(hi)


# while True:
#     word = raw_input("word: ")
#     cmu = lookup(word.lower())
#     hin = trans(cmu)
#     print "%s: %s => %s" % (word, cmu, hin)

def main():
    import sys
    words = sys.argv[1:]

    output = file("out.txt", "w")

    for word in words:
        cmu = lookup(word.lower())
        hin = trans(cmu)
        line = u"%s: %s => %s\n" % (word, cmu, hin)
        output.write(line.encode("utf-8"))

if __name__ == "__main__":
    main()
