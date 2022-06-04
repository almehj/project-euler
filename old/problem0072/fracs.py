#!/usr/bin/env python

import sys

def gcd(a,b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a


max_d = int(sys.argv[1])

n_reds = 0
d = 1
while d <= max_d:
    n = 1
    while n < d:
        if gcd(n,d) == 1:
            #print(n,"/",d)
            n_reds += 1
        n += 1
    d += 1
    if d%1000 == 0:
        sys.stdout.write('.')
        sys.stdout.flush()
        
print(n_reds,"in set for d =",max_d) 
