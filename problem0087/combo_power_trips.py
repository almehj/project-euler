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

unique = []

for a in cubes:
    for b in quads:
        n = a+b
        if n < max_n:
            if n not in unique:
                unique.append(n)
        else:
            break

print(len(quads)*len(cubes))
print(len(unique))

unique.sort()

final = []
na = 0
for a in unique:
    na += 1
    if na%50 == 0:
        print('beep')
    for b in squares:
        n = a+b
        if n < max_n:
            if n not in final:
                final.append(n)
        else:
            break

print(len(final))
