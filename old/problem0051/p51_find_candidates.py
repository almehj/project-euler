#!/usr/bin/env python

import sys

l = int(sys.argv[1])
infile_name = "primes_len%02d.txt"%l

repeats = {}
with open(infile_name) as infile:

    for line in infile:

        n = line.strip()
        for d in "0123456789":
            m = n.count(d)
            if m > 0:
                t = (int(d),m)
                if t not in repeats:
                    repeats[t] = []
                repeats[t].append(n)

    for n_rep in [int(n) for n in sys.argv[2:]]:
        print(n_rep,"times repeated digit:")
        for d in range(10):
            t = (d,n_rep)
            if t in repeats:
                print("  ",d,":"," ".join(repeats[t]))
        
