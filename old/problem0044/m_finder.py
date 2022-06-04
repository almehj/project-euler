#!/usr/bin/env python

from math import sqrt

def check(z):
    n = (z**2 - 1)%24
    return n == 0

def m(z):
    return (z**2 - 1)//24

def q(m):
    return (1 + int(sqrt(1 + 24*m)))//6

def pent(n):
    return int((3*n*n -n)/2)

for i in range(1,100):
    if check(i):
        print(pent(q(m(i))))
