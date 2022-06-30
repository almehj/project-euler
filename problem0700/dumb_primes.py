#!/usr/bin/env python


import sys

limit = 100000000

primes = {}
n = 2

while n <= limit:
    print(n)
    primes[n] = 1
    m = 2
    while m * n <= limit:
        if m % 100000 == 0:
            sys.stderr.write('.')
            sys.stderr.flush()
        primes[m * n] = 0
        m += 1
    if m > 100000:
        sys.stderr.write("\n")

    while n in primes:
        n += 1
