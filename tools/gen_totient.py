#!/usr/bin/env python

import sys

_totients = {}

_totients[0] = 0
_totients[1] = 1


def totient(n):
    if n == 0:
        return 0
    if n == 1:
        return 1



def goo():
    t_vec = [[] for i in range(max_n+1)]
    t_vec[0] = 0
    t_vec[1]=1

    n = 2
    ratio = 1000000.
    ratio_n = 0
    while n <= max_n:
        if len(t_vec[n]) == 0:
            # n is prime
            t_vec[n] = n -1
            m = 2
            while m*n <= max_n:
                t_vec[m*n].append(n)
                m += 1
        else:
            tv = n
            for f in t_vec[n]:
                tv *= (1 - 1/f)
            t_vec[n] = int(tv)

            if same_digits(n,t_vec[n]):
                r = float(n)/t_vec[n]
                if r < ratio:
                    ratio = r
                    ratio_n = n
                    print("phi(%d) = %d with ratio %.5f"%(n,t_vec[n],ratio))
        n += 1


    for n,v in enumerate(t_vec):
        print(n,v)

    

