#!/usr/bin/env python

import sys


with open(sys.argv[1]) as infile:
    total = 0
    for line in infile:
        n = int(line.split()[0])
        print(n)
        total += n

    print(total)
    
