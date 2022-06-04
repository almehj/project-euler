#!/usr/bin/env python

import os

from prime_numbers import is_prime
from utils import seq_string


data_path = os.getenv("EULER_DATAPATH")
if data_path == None:
    data_path = "."

def suitable(n):

    while n > 10:
        digit = n%10
        if digit%2 == 0:
            return False
        n //= 10

    return is_prime(n)    


def setup_prime_lists(max_len):

    answer = {}
    
    with open(os.path.join(data_path,"existing_primes.txt")) as infile:
        for line in infile:
            n = line.strip()
            if len(n) > max_len:
                break

            l = len(n)
            if l not in answer:
                answer[l] = []

            n = int(n)
            if suitable(n):
                answer[l].append(n)

    return answer

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






def main():
    max_len = 6
    lists = setup_prime_lists(max_len)

    i = 2
    n_found = 0
    tot = 0
    while i <= max_len and n_found < 12:

        for n in lists[i]:
            if n//10 in lists[i-1]:
                if is_left_truncatable(n):
                    if is_right_truncatable(n):
                        n_found += 1
                        tot += n
                        print("%2d: %d"%(n_found,n))
        
        i += 1

    print("Total",tot)

if __name__ == "__main__":
    main()
