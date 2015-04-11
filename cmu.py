# coding=utf-8
from __future__ import unicode_literals

cmu_dict = {}


def populate_cmu():
    for line in file("cmudict-0.7b.txt"):
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
AO  ought   AO T      | आ
AW  cow K AW          | आव
AY  hide    HH AY D   | आय
B   be  B IY          | ब
CH  cheese  CH IY Z   | च
D   dee D IY          | ड
DH  thee    DH IY     | ढ
EH  Ed  EH D          | ए
ER  hurt    HH ER T   | अ
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
UW  two T UW          | वू
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
    if phoneme[-1].isdigit():
        phoneme = phoneme[:-1]
    return hin_dict.get(phoneme, phoneme)


def trans(cmu):
    return "".join(trans_lookup(word) for word in cmu.split())


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
