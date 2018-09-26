# coding: utf-8

"""
@author: 武明辉 
@time: 18-9-12 上午9:48
"""

import sys
import re
import collections

WORD_RE = re.compile('\w+')

index = {}

# normal
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurences = index.get(word, [])
            occurences.append(location)
            index[word] = occurences

for word in sorted(index, key=str.upper):
    print(word, index[word])

# setdefault method
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])


# defaultdict
index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)  # bug index[xxx] still return None because it call __getattribute__

for word in sorted(index, key=str.upper):
    print(word, index[word])


if __name__ == '__main__':
    pass
