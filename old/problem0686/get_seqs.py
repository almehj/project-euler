#!/usr/bin/env python

import sys

with open(sys.argv[1]) as infile:
    seq = []
    for line in infile:
        nums = [int(s) for s in line.split()]
        i = nums[0]
        p = nums[1]
        d = nums[2]

        if d not in [90,196,289,485]:
            print("oops!")
            sys.exit(0)
        seq.append(d)


    curr = []
    maybe_end = False
    for d in seq[seq.index(485):]:

        if d == 485:
            if maybe_end:
                print("%2d"%(len(curr)),curr)
                curr = []
                maybe_end = False
            else:
                maybe_end = True
        else:
            maybe_end = False

        curr.append(d)
    print("%2d"%(len(curr)),curr)
