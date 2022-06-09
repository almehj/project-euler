#!/usr/bin/env python

import sys

lowers = {}

n_max = int(sys.argv[1])

n = 2
while n <= n_max:
    m = n
    while m <= n_max:

        diff = m*n - (m+n)
        print(n,m,diff)
        if diff <= 0 :
            if n not in lowers:
                lowers[n] = []
            if m not in lowers:
                lowers[m] = []

            lowers[n].append(m)
            lowers[m].append(n)
        
        m+=1
    
    n+= 1


ns = [n for n in lowers]
ns.sort()

for n in ns:
    print(n,lowers[n])

    
