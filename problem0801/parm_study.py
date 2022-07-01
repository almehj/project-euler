#!/usr/bin/env python

import sys


n = int(sys.argv[1])

n_max = n**2 - n

print("Going up to",n_max)

n_found = n_max 
for x in range(1,n_max+1):
    for y in range(1,n_max+1):
        if x != y:
            if (x**y)%n == (y**x)%n:
#                print(x,y)
                n_found += 1

print("\n",n_found,"found")
