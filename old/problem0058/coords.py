#!/usr/bin/env python

import sys
import prime_numbers

n = 3
total = 0
max_rat = 1.0
while n < int(sys.argv[1]):


    coords = [n**2 - (n-1)*i for i in range(1,4)]
    for m in coords:
        n_corners = 4*(n//2) + 1
        if prime_numbers.is_prime(m):
            total += 1
        rat = total/n_corners
        print(n,":",total,'/',n_corners,rat)
        if rat < 0.1:
            sys.exit(0)
                        
    n += 2
