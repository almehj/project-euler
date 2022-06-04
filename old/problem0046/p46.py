#!/usr/bin/env python

import sys
import prime_numbers
from math import sqrt


max_val = int(sys.argv[1])
max_n = int(sqrt(max_val/2)) + 1
dsq = [2*n*n for n in range(max_val+1)]

n = 9

while n < max_val:
    if (n+1)%1000 == 0:
        sys.stdout.write('.')
        sys.stdout.flush()
        
    if not prime_numbers.is_prime(n):
        can_do = False
        m = 1
        while dsq[m] < n:
            if prime_numbers.is_prime(n-dsq[m]):
                can_do = True
                break
            m += 1
        if not can_do:
            print("CANNOT DO",n)
            sys.exit(0)
    
    n += 2

print(" ")
