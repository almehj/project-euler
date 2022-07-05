#!/usr/bin/env python

import sys
from math import sqrt

def gcd(a,b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a

# Pythag triple for s,t
#  will be primitive if gcd(t,s) = 1 and s&t are not both odd
def trip(s,t):
    a = s**2 - t**2
    b = 2*s*t
    c = s**2 + t**2

    return a,b,c

max_dim = int(sys.argv[1])


def too_big(a,b):
    if a > 2*max_dim and b>2*max_dim:
        return True
    return False

t = 1
total = 0
works = {}

a = b = 0
while not too_big(a,b):

    s = t+1
    a,b,c = trip(s,t)
    while not too_big(a,b):
        k = 1
        ka = a
        kb = b
        kc = c
        while ka
            
        s += 1
        a,b,c = trip(s,t)


mf = int(sqrt(5*max_dim))+1
squares = [n**2 for n in range(2,mf+1)]

n_int = 0
a = 1
while a <= max_dim:
    b = a
    while b <= max_dim:
        c = b
        while c <= max_dim:
            old_true = (c**2 + (a+b)**2) in squares
            if (c,a+b) in works:
                if not old_true:
                    print("     ***old false, new true")
                print(a,b,c)
                n_int += 1
            else:
                if old_true:
                    print("     ***old true, new false")
            c+=1
        b+=1
    a+=1

print(n_int,"integer paths")

