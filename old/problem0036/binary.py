#!/usr/bin/env python3

import sys

from utils import seq_string

def binary_str(n):
    answer = []
    while n > 0:
        answer.append(n%2)
        n //= 2
    return seq_string(reversed(answer),separator="")

def main():
    for i in [int(i) for i in sys.argv[1:]]:
        print ("%d %s"%(i,binary_str(i)))

if __name__ == "__main__":
    main()
    
