#!/usr/bin/env python3

import sys
import math

import euler_config

def read_existing_primes():
    prime_filename = "%s/existing_primes.txt"%(euler_config.data_path)
    answer = []
    try:
        with open(prime_filename,'r') as infile:
            for line in infile:
                if line.strip() != "":
                    n = int(line.strip())
                    answer.append(n)
    except:
        pass

    return answer

existing_primes = read_existing_primes()

def dump_existing_primes():
    prime_filename = "%s/existing_primes.txt"%(euler_config.data_path)
    with open(prime_filename,'w') as outfile:
        for n in existing_primes:
            outfile.write("%d\n"%(n))
            
def is_prime_brute_force(n):

    max_factor = int(math.sqrt(n))+1

    for i in range(2,max_factor+1):
        if n%i == 0:
            return False
    return True

def find_next_prime(n_start):
    n = n_start
    while True:
        if is_prime_brute_force(n):
            return n
        else:
            n += 1
    
def extend_primes(n_max):
    global existing_primes
    while existing_primes[-1] < n_max:
        n = find_next_prime(existing_primes[-1] + 1)
        existing_primes += [n]
    
        
def is_prime_use_existing(n):
    
    max_factor = int(math.sqrt(n))+1
    extend_primes(max_factor)

    if n in existing_primes:
        return True

    for f in existing_primes:
        if f >= n:
            return True
        if n%f == 0:
            return False
        if f > max_factor:
            return True

def is_prime(n):
    if n < 0:
        n = -n

    if n in [0,1]:
        return False

    return is_prime_use_existing(n)


def factorization(n):
    answer = []

    raise RuntimeError("not implemented yet")
    
    return answer


def main():
    for n in [int(s.strip()) for s in sys.argv[1:]]:
        print("%4d: %s"%(n,is_prime(n)))
    dump_existing_primes()
    
if __name__ == "__main__":
    main()
