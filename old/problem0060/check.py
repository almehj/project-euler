#!/usr/bin/env python

import sys
from prime_numbers import is_prime

base = sys.argv[1:]

print(base)
for n1 in base:
    for n2 in base:
        if n1 != n2:
            print(n1+n2,is_prime(int(n1+n2)))
