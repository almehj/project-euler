#!/usr/bin/env python

import sys

start = 31
normal = [485,196,289,196,289,196,485]

with open(sys.argv[1]) as infile:
    n = 1
    for line in infile:
        nums = [int(s) for s in line.split()]
        i = nums[0]
        p = nums[1]
        d = nums[2]
        if n >= start:
            ndx = (n - start)%len(normal)
            if d != normal[ndx]:
                print("oops!",n,ndx,normal[ndx],d)
                      
        n += 1
