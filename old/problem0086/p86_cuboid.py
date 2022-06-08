#!/usr/bin/env python

import sys
from math import sqrt

max_dim = int(sys.argv[1])

max_l = 5*max_dim**2

sqs = [n**2 for n in range(int(sqrt(max_l))+1)]

squares = {}
for s in sqs:
    squares[s] = 1

n_int = 0
a = 1
while a <= max_dim:
    b = a
    while b <= max_dim:
        c = b
        while c <= max_dim:

            lsq = c**2 + (a+b)**2
            if lsq in squares:
                print(a,b,c,":",int(sqrt(lsq)))
                n_int += 1
            c+=1
        b+=1
    a+=1

print(n_int,"integer paths")
