import itertools
with open('filename.txt', "r", encoding='latin1') as ifile: #change encoding value according to your characters used in file
    for line in ifile:
        if line.startswith("TABLE"):
            print(line, end="")
            print(next(ifile, '').strip())
