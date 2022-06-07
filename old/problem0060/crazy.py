#!/usr/bin/env python

import sys
import prime_numbers

def commons(l1,l2):
    answer = []
    for a in l1:
        if a in l2:
            answer.append(a)
    return answer


max_len = int(sys.argv[1])
max_val = 10**max_len

primes = prime_numbers.primes_less_than(max_val)
primes = [str(n) for n in primes if n > 2]
hash_primes = {}
for n in primes:
    hash_primes[n] = 1

befores = {}
afters = {}
follows = {}
for a in primes:
    len_a = len(a)
    befores[a] = []
    afters[a] = []
    for b in primes:
        len_b = len(b)
        if len_b > len_a:
            changed = False
            
            front = b[:len_a]
            if front == a:
                if b[len_a:] in hash_primes:
                    afters[a].append(b[len_a:])
                    changed = True
            back = b[-len_a:]
            if back == a:
                if b[:-len_a] in hash_primes:
                    befores[a].append(b[:-len_a])
                    changed = True

    f = commons(befores[a],afters[a])
    if len(f) > 0:
        follows[a] = f
        for c in f:
            print(a,c)
        sys.stdout.flush()

print("done")

    
