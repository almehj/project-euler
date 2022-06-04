#!/usr/bin/env python

import sys
import prime_numbers

def dig_sum(n):
    digits = [int(d) for d in list(str(n))]
    return sum(digits)
    
def int_root(n,max_l):
    r = 1
    l = 1
    while l <= max_l+1:
        while (r**2)//(10**(l-1)) < n:
            r += 1
        r -= 1

        r *= 10
        n *= 10

        l = len(str(r))

    return r // 100


sqs = [n*n for n in range(2,11)]

total = 0
for n in range(2,100):
    if n not in sqs:
        fint = int_root(n,100)
        print("%3d: %d %d"%(n,fint,len(str(fint))))
        total += dig_sum(fint)


print(total)

