#!/usr/bin/env python

import sys


def digsum(n):
    return sum([int(d) for d in list(str(n))])


max_sum = 0
for a in range(1,101):
    for b in range(1,101):
        n = a**b
        s = digsum(n)
        if s > max_sum:
            max_sum = s

print(max_sum)
        
