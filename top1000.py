import cmu, sys


def main():
    for line in file("0001-1000.txt"):
        _, word, _  = line.split(None, 2)
        mu = cmu.lookup(word.lower())
        hin = cmu.trans(mu)
        line = u"%s: %s => %s\n" % (word, mu, hin)
        sys.stdout.write(line.encode("utf-8"))
        # break

if __name__ == "__main__":
    main()
