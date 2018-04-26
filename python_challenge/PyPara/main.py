import re
import os
from collections import Counter
import string

para = os.path.join('para.txt')

words = 0
parawords = 0

with open(para, 'r' ) as f:
    for line in f:
        #Split Paragraph on basis of '.' or ? or !.
        sen = re.split(r"\.|\?|\!", line)
        len(sen)
        print(sen)
        #Split line into list using space.
        words = sen.split(" ")
        numwords = len(words)
        print(numwords)
