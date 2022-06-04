#!/usr/bin/env python

import sys


c = 485
a = 196
b = 289

fa = 2**a
fb = 2**b
fc = 2**c

n = 5
p = 1060
t = 2**p

lead = sys.argv[1]
min_l = len(lead)

def has_lead(n):
    return (str(n)[:min_l] == lead)


while True:
    for delta,factor in [(a,fa),(b,fb),(c,fc)]:
        possible = t*factor
        if has_lead(possible):
            n += 1
            p += delta
            t = possible
            print(n,p,delta)
            sys.stdout.flush()
            break
            
