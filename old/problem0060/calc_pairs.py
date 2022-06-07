#!/usr/bin/env python

import prime_numbers
import sys


max_l = int(sys.argv[1])

possibles = prime_numbers.primes_less_than(10**max_l)
possibles = [str(n) for n in possibles if n > 2]

mates = {}

total = len(possibles)*(len(possibles) -1)//2
frac = total // 100

sys.stderr.write("%d things, '.' = %d\n"%(total,frac))
sys.stderr.flush()
total = 0
bound = frac
for i,n1 in enumerate(possibles):
    for n2 in possibles[i+1:]:
        total += 1
        if total > bound:
            bound += frac
            sys.stderr.write('.')
            sys.stderr.flush()
        if prime_numbers.is_prime(int(n1+n2)) and \
           prime_numbers.is_prime(int(n2+n1)):
            mates[(n1,n2)] = 1

print('\n')

for t in mates:
    print("%s %s"%t)

