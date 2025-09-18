import glob

pths = glob.glob(r"./*.md")

for pth in pths:
    info = ""
    with open(pth, 'r', encoding='utf-8') as f:
        for line in f:
            info += line
    info = info.replace("Wei-Nan", "Weinan")
    with open(pth, 'w', encoding='utf-8') as f:
        f.write(info)


