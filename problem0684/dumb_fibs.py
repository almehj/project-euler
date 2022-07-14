#!/usr/bin/env python


import sys
from math import log

fibs = {0:1,1:1}

def fib(n):
    if n in fibs:
        return fibs[n]

    f = fib(n-1) + fib(n-2)
    fibs[n] = f
    return f


def main():
    for n_max in sys.argv[1:]:
        n_max = int(n_max)
        for n in range(n_max+1):
            f = fib(n)
            print("%5d %22d %22d %.4f"%(n,f,f%(2**64 - 1),log(f)/log(2)))
        

if __name__ == "__main__":
    main()
