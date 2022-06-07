#!/usr/bin/env python

import prime_numbers
import sys


max_l = int(sys.argv[1])

possibles = prime_numbers.primes_less_than(10**max_l)
possibles = [n for n in possibles if n > 2]
print(possibles[:5])
def working_parts(n):
    answer = []
    n = str(n)
    for i in range(1,len(n)):
        # proposed partition
        n1,n2 = n[:i],n[i:]

        # Find reasons to reject
        if n2[0] == '0':
            continue
        backward = int(n2+n1)
        if not prime_numbers.is_prime(backward):
            continue
        
        n1,n2 = int(n1),int(n2)
        if prime_numbers.is_prime(n1) and \
           prime_numbers.is_prime(n2) and \
           n1 > 2 and n2 > 2:
            answer.append((n1,n2))
            
    return answer

mates = {}
frac = len(possibles)//10
nvals = 1
bound = frac
for n in possibles:
    l = working_parts(n)
    if len(l) > 0:        
        for n1,n2 in l:
            if n1 not in mates:
                mates[n1] = []
            if n2 not in mates:
                mates[n2] = []
            mates[n1].append(n)
            mates[n2].append(n)
    nvals += 1

    if nvals > bound:
        bound += frac
        print('.')

for n in mates:
    print (n,":",mates[n])
