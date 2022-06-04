#!/usr/bin/env python

from factor_tools import gcd
import sys

def expand(n):

    num = 0
    den = 1

    while n > 0:

        num += 2*den
        f = gcd(num,den)
        num //= f
        den //= f
        num,den = den,num
        
        n-= 1
    

    # add 1
    num += den
    f = gcd(num,den)
    num //= f
    den //= f
    
    return num,den


max_n = int(sys.argv[1])

total = 0
while max_n > 0:
    n,d = expand(max_n)
    if len(str(n)) > len(str(d)):
        print(max_n,n,d,n/d)
        total += 1

    max_n -= 1
    
print(total,"total")
