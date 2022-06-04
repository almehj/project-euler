#!/usr/bin/env python

import sys
max_d = int(sys.argv[1])

with (open("totient.txt","r")) as infile:
    total = -1
    for line in infile:
        d,td = [int(x) for x in line.split()]

        if d > max_d:
            print(total)            
            sys.exit(0)
            
        total += td
        
