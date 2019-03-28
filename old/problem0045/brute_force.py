#!/usr/bin/env python

import sys

def triangle(n):
    return n*(n+1)//2

def pentagonal(n):
    return n*(3*n -1)//2

def hexagonal(n):
    return n*(2*n - 1)

def main():
    max_n = int(sys.argv[1])

    ndxs = [1,1,1]
    funcs = [triangle,pentagonal,hexagonal]
    vals = [f(1) for f in funcs]

    while max(ndxs) <= max_n:

        if vals[0] == vals[1] and vals[1] == vals[2]:
            print("T(%d) == T(%d) == H(%d) = %d"%tuple(ndxs + [vals[0]]))
            up_ndx = 2            
        else:
            up_ndx = vals.index(min(vals))

        ndxs[up_ndx] += 1
        vals[up_ndx] = funcs[up_ndx](ndxs[up_ndx])
            
    
if __name__ == "__main__":
    main()
