#!/usr/bin/env python

import sys

import prime_numbers
from utils import seq_string

def n_digits(n):
    return len(str(n))

def rotation(s):
    return s[1:] + s[0]

def gen_rot_set(s):
    answer = [s]
    for i in range(len(s)):
        s = rotation(s)
        if s not in answer:
            answer.append(s)
    return answer
    
def check_circle_with_removal(n,primes):
    n_s = str(n)
    n_rots = 0

    rot_set = gen_rot_set(n_s)
    
    for n_check in rot_set:
        if n_check in primes:
            n_rots += 1
            primes.remove(n_check)

    return n_rots == len(rot_set)
            

def filter_impossibles(l):
    answer = ['2']
    for p in l:
        include = True
        for c in p:
            if int(c)%2 == 0:
                include = False
        if include:
            answer.append(p)

    return answer

def main():

    max_n = int(sys.argv[1])
    primes = [str(p) for p in prime_numbers.primes_less_than(max_n)]

    len_p = len(primes)
    primes = filter_impossibles(primes)
    print("Filter dropped length from %d to %d (%d gone)"%(len_p,len(primes),len_p-len(primes)))
    
    p_set = []
    while len(primes) > 0:
        p = primes[0]
        if check_circle_with_removal(p,primes):
            p_set += gen_rot_set(p)
            print("%s is one base (added %d)"%(p,len(gen_rot_set(p))))
    print("\n%d circular primes < %d"%(len(p_set),max_n))
    p_set = sorted([int(i) for i in p_set])    
    print(" List: %s"%(seq_string(p_set)))
    
if __name__ == "__main__":
    main()
