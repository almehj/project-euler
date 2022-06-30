#!/usr/bin/env python


import sys


def gcd(a,b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a


def invert(a,m):

    t = 0
    r = m
    new_t = 1
    new_r = a

    while new_r != 0:
        q = r//new_r
        t,new_t = new_t,t - q*new_t
        r,new_r = new_r,r - q*new_r

    if r > 1:
        print("really, no inverse")
        return None
    if t < 0:
        t += m

    return t
    



a = int(sys.argv[1])
m = int(sys.argv[2])

if gcd(a,m) != 1:
    print("no inverse")

a_inv = invert(a,m)
if a_inv != None:
    print("  ",a,"*",a_inv,"mod",m,"=",(a*a_inv)%m)

    

