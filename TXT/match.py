import itertools
import re
def get_next_words(text, match, sep='.'):
    words = iter(text.split(sep))
    for word in words:
        if word == match:
            yield next(words)
with open('filename.txt', "r") as ifile:
    for line in ifile:
        print((line.split()[-1]).replace('files.','')) #modify according to your pattern of data
