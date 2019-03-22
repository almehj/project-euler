#!/usr/bin/env python3

import sys

n_max = int(sys.argv[1])

for n in range(1,n_max+1):

    T = n*(n+1)//2
    P = n*(3*n-1)//2
    H = n*(2*n -1)

    print("%5d %10d %10d %10d"%(n,T,P,H))
          
