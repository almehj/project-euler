#!/usr/bin/env python

import sys

max_n = int(sys.argv[1])

l = [1]*max_n

n = 2

while n < max_n:
    print(n)
    m = 1
    while m*n < max_n:
        l[m*n] = 0
        m += 1
    while n < max_n and l[n] == 0:
        n += 1
