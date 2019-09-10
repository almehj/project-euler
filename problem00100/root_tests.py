#!/usr/bin/env python3

import sys
import getopt
from math import sqrt

def n_term(n):
    return 1 + 2 * n * (n -1)

def calc_blue(n):
    return .5*(1. + sqrt(n_term(n)))
    

def find_min_total(n):

    disc = 1 - 2*(1 - n**2)
    if disc < 0:
        return 0
    flt_val = .5*(1 + sqrt(disc))

    return flt_val


def find_perfect(t_min):
    n = 1
    nsq = 1
    t = t_min

    while t < 10*t_min:
        nt = n_term(t)
        while nt > nsq:
            n += 1
            nsq = n*n
        if nt == nsq:
            print("%d %d %d"%(t,nt,nsq))
            return 
        t += 1


def partial_digital_root(n):

    answer = 0

    while n > 0:
        d = n%10
        if d != 9:
            answer += d
        n //= 10
        
    return answer

def digital_root(n):

    answer = n

    while answer >= 10:
        answer = partial_digital_root(answer)

    return answer


# Tests:
#  False => not a PSq, True = Maybe
def count_zeros(n):
    n_zeros = 0

    d = n%10
    while n > 0 and d == 0:
        n_zeros += 1
        n //= 10
        d = n%10
    return n_zeros

def units_test(n):

    d = n%10
        
    if d in [2,3,7,8]:
        return False
    else:
        return True

def test_root(n):

    return digital_root(n) in [1,4,7,9]
    
def test_25(n):

    if n%10 == 5 and (n//10)%10 != 2:
        return False
    else:
        return True

def test_6units(n):

    d = n%10
    td = (n//10)%10       
    if d == 6:
        return td%2 != 0
    else:
        return td%2 == 0

def test_48(n):

    if n%4 == 0:
        return n%8 == 0

    return True

def test_even4(n):
    if n%2 == 0:
        return (n%100)%4 == 0
    else:
        return True

    
def is_PSq(n):
    
    nz = count_zeros(n)
    if nz%2 != 0:
        return False
    else:
        while nz > 0:
            n //= 10
            nz -= 1
    
    if not units_test(n):
        return False

    if not test_root(n):
        return False
    
    if not test_25(n):
        return False

    if not test_6units(n):
        return False

    if not test_even4(n):
        return False
    
    return True
    
def main():
    for str_n in sys.argv[1:]:
        n = int(str_n) + 10**12
        i = 10**12
        while i < n:
            if is_PSq(n_term(i)):
                print(i,n_term(i),sqrt(n_term(i)))
            i += 1

    

        

            
if __name__ == "__main__":
    main()
