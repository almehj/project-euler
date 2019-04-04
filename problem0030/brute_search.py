#!/usr/bin/env python3

import sys

from digit_set_brute import compute_sets
from utils import seq_string

def value(l,n):
    return sum([i**n for i in l])

def value_tuple(n):
    val = [int(c) for c in list(str(n))]
    val.sort()
    return tuple([i for i in val if i != 0])

    
def main():
    max_len = int(sys.argv[1])
    exponent = int(sys.argv[2])
    
    total = 0
    digit_sets = compute_sets(max_len)
    for digit_set in digit_sets:
        v = value(digit_set,exponent)
        if v < 2:
            continue
        vt = value_tuple(v)
        if tuple(digit_set) == vt:
            total += v
            print("%d (%s) from %s"%(v,seq_string(vt),seq_string(digit_set)))

    print("Total of all is %d"%(total))
if __name__ == "__main__":
    main()
    
