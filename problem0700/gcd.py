#!/usr/bin/env python


import sys


def gcd(a,b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a

a = int(sys.argv[1])
b = int(sys.argv[2])


g = gcd(a,b)
print(a,b,g,a/g,b/g)


