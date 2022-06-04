#!/usr/bin/env python

import sys

normal = [485,196,289,196,289,196,485]
n_normal = len(normal)
s_normal = sum(normal)
part_s_normal = [sum(normal[:n]) for n in range(n_normal)]

min_occur = 30
min_p = 7953

# find the power of the nth opccurance where 2^n starts with 123
def delta_p(n):

    p = 7953
    n -= 30

    n_sums = n // n_normal
    stop = n % n_normal

    p += n_sums*s_normal
    p += part_s_normal[stop]

    return p


for n in [int(s) for s in sys.argv[1:]]:
    print(n,delta_p(n))
    
