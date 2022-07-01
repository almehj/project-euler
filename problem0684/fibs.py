#!/usr/bin/env python
import getopt
import sys
from math import log10
from mod_exp import exp_squaring


m = 1000000007
fibs = {0:0,1:1}


def fib(n):
    if n in fibs:
        return fibs[n]

    f = fib(n-2) + fib(n-1)
    fibs[n] = f

    return f


def s(n):
    n_nines = n // 9
    l = n%9

    # The number we want is (l+1)*10^n_nines - 1
    # Since it's modular, we can mod everything

    tens = exp_squaring(10,n_nines,m)

    return ((l+1)*tens - 1)%m


def big_s(n):

    n_segs = n//9
    base = 5*exp_squaring(10,n_segs,m) - (5 + n_segs*9)%m
    base %= m
    r = n_segs*9
    while r <= n:
        base += s(r)
        base %= m
        r += 1
    return base


def main():

    optlist,args = getopt.getopt(sys.argv[1:],"s:")

    for opt,val in optlist:
        if opt in ['-s']:
            n = int(val)
            print("S(%d) = %d"%(n,big_s(n)))

    for n_max in args:
        total = 0
        n_max = int(n_max)
        for n in range(1,n_max+1):
            fn = fib(n)
            sn = big_s(fn)
            total += sn
            total %= m

            print(n,fn,sn,total)

        print("Total for n from 2 to %d is"%n_max,total-1)


if __name__ == "__main__":
    main()

