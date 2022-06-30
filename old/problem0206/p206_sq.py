#!/usr/bin/env python

from math import sqrt
import sys

lo = 1020304050607080900
hi = 1929394959697989990

r_lo = int(sqrt(lo)) - 1
r_hi = int(sqrt(hi)) + 1

space = r_hi-r_lo
r = r_lo
inc = int((r_hi - r_lo)/100)
bound = r_lo + inc
i_min = 10
while r <= r_hi:

    if r > bound:
        print(r)
        bound += inc

    n = r**2

    if n%10 == 0:
        i = 9
        n //= 100
        while i > 0:
            d = n%10
            if d != i:
                break
            n //= 100
            i -= 1
        if i < i_min:
            print("new i_min",i_min,r,r**2)
            i_min = i
        if i == 0:
            print(r,"^2 =",r**2)
            sys.exit(0)

    r += 1

print(r,r**2)

foo = 9
