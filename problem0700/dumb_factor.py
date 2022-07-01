#!/usr/bin/env python


import sys
from math import sqrt


n = int(sys.argv[1])
f_max = sqrt(n) + 1
factors = []
with open("primes.txt") as infile:
    f = 0
    for line in infile:
        f = int(line)
        while n%f == 0:
            factors.append(f)
            n //= f
        if n <= 1 or f > f_max:
            if n > 1:
                factors.append(n)
            break

n = 1
for f in factors:
    n *= f

print(n,":"," ".join([str(n) for n in factors]))
