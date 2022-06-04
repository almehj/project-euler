#!/usr/bin/env python

import sys

seq = []
num_7 = 0
for a in sys.argv[1:]:
    n = int(a)
    if n == 7:
        num_7 += 1
    else:
        if num_7 > 0:
            seq.append("%dB"%(num_7))
            num_7 = 0
        if n == 25:
            seq.append('/')
            print(" ".join(seq))
            seq = []
        elif n == 33:
            seq.append('A')

print(" ".join(seq))

[
