#!/usr/bin/env python3

import sys
import math
import logging
import functools

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
        answer = [2]

    return answer

existing_primes = read_existing_primes()
hash_existing = {}
max_existing = -1
for n in existing_primes:
    hash_existing[n] = 1
    if n > max_existing:
        max_existing = n


def compute_max_factor(n):
    return int(math.sqrt(n))+1

def dump_existing_primes():
    prime_filename = "%s/existing_primes.txt"%(euler_config.data_path)
    logging.debug("Dumping list of first %d primes to %s"%
                  (len(existing_primes),prime_filename))
    with open(prime_filename,'w') as outfile:
        for n in existing_primes:
            outfile.write("%d\n"%(n))
            
def is_prime_brute_force(n):

    print("Brute forcing",n)
    #logging.debug("Brute forcing %d"%(n))
    max_factor = compute_max_factor(n)
    #logging.debug("Max factor is %d"%(max_factor))
    if n%2 == 0: return False
    
    for i in range(3,max_factor+1,2):
        #logging.debug("Testing %d|%d"%(i,n))
        if n%i == 0:
            return False
    return True

def find_next_prime(n_start):

    n = n_start
    if n%2 == 0: n += 1

    while True:
        if is_prime_brute_force(n):
            logging.debug("Next prime > %d is %d"%(n_start,n))
            return n
        else:
            n += 2
    
def extend_primes(n_max):

    global existing_primes
    while existing_primes[-1] < n_max:
        n = find_next_prime(existing_primes[-1] + 1)
        existing_primes += [n]
        hash_existing[n] = 1

    max_existing = existing_primes[-1]
        
def is_prime_use_existing(n):

    logging.debug("Checking primality of %s using existing list of first %d primes"%
                 (n,len(existing_primes)))
    
    max_factor = compute_max_factor(n)
    logging.debug("Max factor is %d"%(max_factor))

    if n in hash_existing:
        logging.debug("%d is in existing prime list"%(n))
        return True

    logging.debug("Trying factors from list of first %d primes"%(len(existing_primes))) 
    for f in existing_primes:
        if n%f == 0:
            logging.debug("%d|%d: COMPOSITE"%(f,n))
            return False
        if f >= max_factor:
            logging.debug("Test factor %d >= max_factor %d: %d PRIME"%(f,max_factor,n))
            return True

    logging.debug("Not in list, extending to first prime factor >= %d"%(max_factor))
    if existing_primes[-1] < max_factor:
        start_i = len(existing_primes)
        extend_primes(max_factor)

    for f in existing_primes[start_i:]:
        if n%f == 0:
            logging.debug("%d|%d: COMPOSITE"%(f,n))
            return False
        if f >= max_factor:
            logging.debug("Test factor %d >= max_factor %d: %d PRIME"%(f,max_factor,n))
            return True



        
def is_prime(n):
    if n < 0:
        n = -n

    if n in [0,1]:
        return False

    
    #    if n < existing_primes[-1]:
    #         return (n in existing_primes)
    if n in hash_existing:
        return True
    
    return is_prime_use_existing(n)


def factorization(n):
    answer = []

    max_factor = compute_max_factor(n)
    extend_primes(max_factor)
    
    for f in existing_primes:
        f_n = 0
        while n > 1 and n%f == 0:
            f_n += 1
            n = n//f
        if f_n > 0:
            answer += [(f,f_n)]
        if n <= 1:
            break
        
    return answer

def gen_divisor_list(factors):
    prime_factors = [t[0] for t in factors]
    prime_exponents = [t[1] for t in factors]
    exps = [0]*len(prime_factors)

    answer = []
    n_combos = functools.reduce(lambda x, y: x*y, [i+1 for i in prime_exponents])
    n = 0
    while n < n_combos:
        answer.append(
            functools.reduce(
                lambda x, y: x*y,
                [x**e for x,e in zip(prime_factors,exps)]
            )
        )
        for i in range(len(exps)):
            exps[i] += 1
            if exps[i] <= prime_exponents[i]:
                break
            exps[i] = 0
        n += 1
            
    answer.sort()
    return answer

def divisors(n):
    factors = factorization(n)
    return gen_divisor_list(factors)


def primes_less_than(n):
    n = abs(n)

    answer = []
    for p in existing_primes:
        if p < n:
            answer += [p]
    return answer

def main():

    logging.basicConfig(level=logging.DEBUG)

    for n in [int(s.strip()) for s in sys.argv[1:]]:
        print(n,is_prime(n))
if __name__ == "__main__":
    main()
