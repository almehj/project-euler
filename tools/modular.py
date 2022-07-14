#!/usr/bin/env python


def inverse(a,m):

    t = 0
    r = m
    new_t = 1
    new_r = a

    while new_r != 0:
        q = r//new_r
        t,new_t = new_t,t - q*new_t
        r,new_r = new_r,r - q*new_r

    if r > 1:
        return None
    if t < 0:
        t += m

    return t


def power(b,e,m):
    return exp_squaring(b,e,m)


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

