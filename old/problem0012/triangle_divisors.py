#!/usr/bin/env python3

import sys
from math import sqrt
from functools import reduce

# A List of rpime numbers <= primes[-1]
primes = [2]

def max_factor(n):
    return int(sqrt(n))+1

def is_simple_prime(n):
    # Try for an easy answer
    if n in [0,1]:
        return False
    
    if n in primes:
        return True
    return None

def check_existing_primes(n,max_fact):
    for f in primes:
        if n%f == 0:
            return False
        
        if f > max_fact:
            return True

    return None

def is_prime(n):

    n = abs(n)
    
    answer = is_simple_prime(n)
    if answer != None:
        return answer
        
    # OK, we do it the hard way...
    # If we need more prime numbers, find them the hard way
    max_fact = max_factor(n)
    if primes[-1] < max_fact:
        extend_primes(max_fact)
    # We only need consider prime numbers up to sqrt(n)+1
    assert(max_fact <= primes[-1])
    return check_existing_primes(n,max_fact)

def is_prime_bruteforce(n):
    # Simple?
    answer = is_simple_prime(n)    
    if answer != None:
        return answer

    # Maybe we already know?
    max_fact = max_factor(n)
    answer = check_existing_primes(n,max_fact)
    if answer != None:
        return answer

    # We assume that primes contains all primes <= primes[-1]
    # Starting factor: smallest odd number >= last prime 
    f = primes[-1]
    if f%2 == 0:
        f+=1

    while f <= max_fact:
        if n%f == 0:
            return False
        f += 2
    # Tried all we need to
    return True
        
def next_highest_prime(n):
    if n%2 == 0:
        n += 1
    else:
        n += 2
        
    while not is_prime_bruteforce(n):
        n += 2

    return n

def extend_primes(max_fact):
    max_fact = abs(max_fact)
    while True:
        if primes[-1] <= max_fact:
            primes.append(next_highest_prime(primes[-1]))
        else:
            return

def prime_factorization(n):
    if n < 0:
        return prime_factorization(-n)

    if n in [0,1]:
        return {n:1}

    extend_primes(n)
    factors = {}

    for f in primes:
        while n%f == 0:
            factors[f] = factors.get(f,0) + 1
            n /= f
        if n == 1:
            break
        
    return factors

def product(factors,exps):
    answer = 1

    for f,e in zip(factors,exps):
        answer *= f**e

    return answer

def gen_divisor_list(factors):
    prime_factors = list(factors.keys())
    exps = [0]*len(prime_factors)

    answer = []
    n_combos = reduce(lambda x, y: x*y, [factors[i]+1 for i in factors])
    n = 0
    while n < n_combos:
        answer.append(reduce(lambda x, y: x*y, [x**e for x,e in zip(prime_factors,exps)]))
        for i in range(len(exps)):
            exps[i] += 1
            if exps[i] <= factors[prime_factors[i]]:
                break
            exps[i] = 0
        n += 1
            
    answer.sort()
    return answer
    
def calc_n_divisors(n):
    factors = prime_factorization(n)
    return reduce(lambda x, y: x*y, [factors[i]+1 for i in factors])
    
def main():

    goal = int(sys.argv[1])

    n = 2
    curr_factors = prime_factorization(n)
    prev_factors = prime_factorization(n-1)

    while True:
        factors = curr_factors.copy()
        for k in prev_factors:
            factors[k] = factors.get(k,0) + prev_factors[k]
        if 2 in factors:
            factors[2] -= 1

        n_divs = reduce(lambda x, y: x*y, [factors[i]+1 for i in factors])
        print(int(n*(n-1)/2),":",n_divs,"divisors")
        if n_divs >= goal:
            break
        else:
            prev_factors = curr_factors
            n += 1
            curr_factors = prime_factorization(n)
            
            
    n = int(n*(n+1)/2)
    print(factors )
    print(n)
    print(gen_divisor_list(factors))
    print(len(gen_divisor_list(factors)))
    pfl = list(factors.keys())
    exps = [factors[x] for x in pfl]
    print(product(pfl,exps))
    
    
def foo():
    n = 1
    next_n = 2
    done = False
    max_divlist_len = -1
    
    while not done:
        divlist_len = calc_n_divisors(n)
        if divlist_len > max_divlist_len:
            max_divlist_len = divlist_len
        print("%10d: %d divisors (max so far is %d)"%(n,divlist_len,max_divlist_len))
        if max_divlist_len >= goal_divlist_len:
            done = True
        else:
            n += next_n
            next_n += 1
    
if __name__ == "__main__":
    main()
    
