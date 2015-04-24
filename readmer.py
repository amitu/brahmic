import cmu

def main():
    readme = file("README.md").read().decode("utf-8")
    eng = readme.split("----")[0]
    hin = cmu.trans_text(eng)
    file("README.md", "w").write(("%s----\n\n%s" % (eng, hin)).encode("utf-8"))

if __name__ == "__main__":
    main()
