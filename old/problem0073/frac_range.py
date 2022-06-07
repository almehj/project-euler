#!/usr/bin/env python

import sys
from factor import gcd

max_n = int(sys.argv[1])


total = 0
n = 2
while n <= max_n:
    n_start = n//3
    n_stop = n//2
    if n%2 == 0: n_stop -= 1
    
    for k in range(n_start+1,n_stop+1):
        if gcd(k,n) == 1:
            total += 1
    
    n += 1
    if n%50 == 0:
        sys.stdout.write('.')
        sys.stdout.flush()
        if n%1000 == 0:
            print(n)

print("\n",total,"in range")




    

