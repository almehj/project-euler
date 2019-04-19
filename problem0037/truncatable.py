#!/usr/bin/env python3

import sys
import logging

from prime_numbers import is_prime, prime_iter
from utils import seq_string

def is_truncatable(n):

    if n < 10:
        return False

    n_str = str(n)
    for i in range(len(n_str)-1,0,-1):
        if not is_prime(int(n_str[:i])) or \
           not is_prime(int(n_str[i:])):
            return False

    return True



def main():

    logging.basicConfig(level=logging.DEBUG)

    max_val = int(sys.argv[1])

    n_checked = 0
    n_found = 0
    total_found = 0
    p_it = prime_iter(max_val=max_val)
    for p in p_it:
        if p < 10:
            continue        
        if is_truncatable(p):
            print("%d is truncatable"%(p))
            n_found += 1
            total_found += p
        n_checked += 1
        if n_checked%1000 == 0:
            sys.stdout.write('%d '%(p))
            sys.stdout.flush()
            
    print("\nFound %d left/right truncatable primes totalling %d"%(n_found,total_found))

if __name__ == "__main__":
    main()
