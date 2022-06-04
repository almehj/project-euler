#!/usr/bin/env python3

import sys
import logging
import cProfile

from prime_numbers import is_prime, prime_iter
from utils import seq_string

def is_right_truncatable(n):

    if n < 10:
        return False

    while n > 0:
        if not is_prime(n):
            return False
        n //= 10

    return True

def is_left_truncatable(n):

    if n < 10:
        return False

    factor = 10**(len(str(n)) - 1)
    while n > 0:
        if not is_prime(n):
            return False
        n %= factor
        factor //= 10

    return True


def is_truncatable(n):

    log_n = len(str(n)) - 1

    f1 = 10
    f2 = 10**log_n

    for i in range(log_n+1):
        t1 = n%f1
        if not is_prime(t1):
            #print("Rejecting %d because %d not prime"%(n,n%f1))
            return False
        t2 = n//f2
        if not is_prime(t2):
            #print("Rejecting %d because %d not prime"%(n,n//f2))
            return False
        f1 *= 10
        f2 //= 10
        
    return True

def main():

    max_val = int(sys.argv[1])

    n_checked = 0
    n_found = 0
    total_found = 0
    p_it = prime_iter(max_val=max_val)
    for p in p_it:
        if p < 10:
            continue        
        if is_truncatable(p):
            print("FOUND ONE! %d"%(p))
            n_found += 1
            total_found += p
            if n_found >= 11:
                break

    print("\nFound %d left/right truncatable primes totalling %d"%(n_found,total_found))

if __name__ == "__main__":
    cProfile.run('main()')
