#!/usr/bin/env python3


import sys

with open(sys.argv[1]) as infile:

    total = 0
    for line in infile:
        i = int(line.strip())
        total += i
        print(i)

    print("\n\n%s"%(total))
