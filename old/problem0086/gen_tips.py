#!/usr/bin/env python

import sys

def trip(t,s):
    a = s**2 - t**2
    b = 2*t*s
    c = s**2 + t**2

    return a,b,c

def gcd(a,b):
    while b != 0:
        t = b
        b = a%b
        a = t

    return a

max_n = int(sys.argv[1])

t = 1




while True:
    s = t + 1
    while gcd(t,s) > 1 or (t%2==1 and s%2==1):
        s += 1        
    a,b,c = trip(t,s)
    if a > max_n or b > max_n or c > max_n:
        break
    if a>b: a,b = b,a
    
    while True:        
        if a > max_n or b > max_n or c > max_n:
            break
        k = 1
        while True:
            if k*a > max_n or k*b > max_n or k*c > max_n:
                break
            print(k*a,k*b,k*c)
            k += 1

            
        s += 1
        while gcd(t,s) > 1 or (t%2==1 and s%2==1):
            s += 1
        a,b,c = trip(t,s)
        if a>b: a,b = b,a
    t += 1
