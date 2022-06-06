#!/usr/bin/env python

import sys
from math import sqrt
import prime_numbers

max_n = int(sys.argv[1])
max_f = int(sqrt(max_n))

l_primes = prime_numbers.primes_less_than(max_f)

squares = [n**2 for n in l_primes]
cubes = [n**3 for n in l_primes]
quads = [n**4 for n in l_primes]

squares = [n for n in squares if n < max_n]
cubes = [n for n in cubes if n < max_n]
quads = [n for n in quads if n < max_n]

print(len(squares),len(cubes),len(quads))
print(quads)

seen = []
for na in squares:
    for nb in cubes:
        base = na + nb
        if base < max_n:
            if base not in seen:
                seen.append(base)
        else:
            break

print("\n",len(seen),len(quads))
print("sorting")
seen.sort()
print("done sorting")

unique = []
for nc in quads:
    print(nc,len(unique))
    for base in seen:
        n = nc + base
        if n < max_n:
            if n not in unique:
                unique.append(n)
        else:
            break
unique.sort()
print("\n",len(unique))
