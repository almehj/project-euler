#!/usr/bin/env python3

import sys

import prime_numbers

def main():
    max_val = int(sys.argv[1])

    primes = prime_numbers.primes_less_than(max_val)

    print("%d primes less than %d"%(len(primes),max_val))

if __name__ == "__main__":
    main()
