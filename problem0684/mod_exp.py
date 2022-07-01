#!/usr/bin/env python


import sys


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


def exp_squaring(x,n,m):
    if n < 0:
        x = invert(x)%m
        return exp_squaring(x,n)

    if n == 0:
        return 1

    if n%2 == 0:
        return exp_squaring((x*x)%m,n//2,m)%m
    else:
        return (x*exp_squaring((x*x)%m, (n-1)//2,m)%m)%m


def main():
    m = int(sys.argv[3])
    b = int(sys.argv[1])
    e = int(sys.argv[2])

    print(log10(e)/log10(2))
    print(b,e,m,exp_squaring(b,e,m))
    if e < 1000:
        print((b**e)%m)
