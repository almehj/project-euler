#!/usr/bin/env python3

import sys

from digit_set import set_generator
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

    s = set_generator(max_len)

    total = 0
    for t in s:
        combo = tuple(sorted([i for i in t if i != 0]))
        v = value(combo,exponent)
        if v < 2:
            continue
        vt = value_tuple(v)
        if vt == combo:
            total += v
            print("%d (%s) from %s"%(v,seq_string(vt),seq_string(combo)))
            
    print("Total of all is %d"%(total))
if __name__ == "__main__":
    main()
    
