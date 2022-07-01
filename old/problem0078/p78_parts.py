#!/usr/bin/env python

import sys

n_max = int(sys.argv[1])
f_max = int(sys.argv[2])

table = [1 for n in range(n_max+1)]

n = 1
while n <= n_max:
    n += 1
    for i in range(n,n_max+1):
        table[i] += table[i-n]
        table[i] %= f_max
        if i == n:
            print(i,table[i])
            if table[i] == 0:
                print("Found",i)
                sys.exit(0)
    
print("\nFinal:",n-1,table[-1])
            
