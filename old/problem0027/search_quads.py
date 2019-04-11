#!/usr/bin/env python3

import sys
import logging

from prime_numbers import is_prime,primes_less_than


primes = []
max_prime = -1

def setup_primes(n):
    global primes
    global max_prime
    primes = primes_less_than(n)
    max_prime = max(primes)
    print("%d primes less than %d"%(len(primes),n))

def value(a,b,n):
    return n**2 + a*n + b

def consider(b):

    print("Considering %d"%(b))
    
    max_len = 0
    max_a = 0
    n_a = 0
    for try_a in range(1000):
        if n_a%100 == 0:
            sys.stdout.write("%s "%(try_a))
            sys.stdout.flush()
            
        for a in -try_a,try_a:
            n_a += 1
            
            n = 0
            v = value(a,b,0)            
            while True:
                if (v < max_prime and v not in primes) or not is_prime(v):
                    break
                else:                
                    n += 1
                    v = value(a,b,n)

            if n > max_len:
                max_len = n
                max_a = a

    sys.stdout.write("\n")
    return max_len,max_a

def do_search(pot_b):

    max_len = -1
    max_coeff = 0,0
    
    for b in reversed(pot_b):
        for try_b in -b,b:
            if max_len > b:
                break
            len_b,a = consider(try_b)
            if len_b > max_len:
                print("Found a = %d, b = %d has series of length %d"%(a,try_b,len_b))
                max_len = len_b
                max_coeff = a,try_b


def main():

    max_val = int(sys.argv[1])
    setup_primes(max_val)
    do_search(primes)
    
if __name__ == "__main__":
    main()
