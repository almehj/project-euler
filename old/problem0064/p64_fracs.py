#!/usr/bin/env python

import sys
from math import sqrt

def gcd(a,b):
    while b != 0:
        t = b
        b = a%b
        a = t

    return a

k_max = int(sys.argv[2])

def calc_series(n):

    x = sqrt(n)
    r = int(x)

    answer = [r]
    k = 1

    p = 1
    q = r
    seen = {}
    state = (p,q)
    while k <= k_max:
        seen[state] = 1

        val = n - q**2 
        if val%p != 0:
            print("OOOF!",n,k,p,q,val)
            sys.exit(-1)
        val //= p

        num = q + r
        off_z = r
        c = 1234567
        if num <= val:
            c = 1
            off_z += (val - num)
        else:
            c = num//val
            off_z -= num%val

        answer.append(c)
        p = val
        q = off_z

        state = (p,q)
        if state in seen:
            break
        
        k += 1

    if state not in seen:
        print("OUCH!")
        sys.exit(-1)
        
    return answer



n_max = int(sys.argv[1])

squares = {}
n = 1
while n**2 <= n_max:
    squares[n**2] = 1
    n += 1

n = 2
evens = 0
odds = 0
while n <= n_max:
    if n not in squares:

        series = calc_series(n) 
        series_str = "%d; "%series[0] + " ".join([str(k) for k in series[1:]])
        l = len(series) - 1
        if (l%2 == 0):
            evens += 1
        else:
            odds += 1
            
        print(n,series_str)

    n+=1

print(evens, "even")
print(odds, "odd")
