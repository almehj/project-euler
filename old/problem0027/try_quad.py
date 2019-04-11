#!/usr/bin/env python3

import sys

from prime_numbers import is_prime

def value(a,b,n):
    return n**2 + a*n + b

def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print("Considering n^2 + %dn + %d"%(a,b))
    
    n = 0
    v = value(a,b,n)
    vals = []
    while is_prime(v):
        vals.append(v)
        n += 1
        v = value(a,b,n)

    print("%d terms: %s"%(len(vals)," ".join([str(x) for x in vals])))
    

if __name__ == "__main__":
    main()

