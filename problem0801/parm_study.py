#!/usr/bin/env python

import sys
import modular


n = int(sys.argv[1])

n_max = n**2 - n


n_found = n_max

todo = ((n_max-1)*n_max)//2
inc = todo // 100
bound = inc
k = 0

print("Going up to",n_max)
print("There are %d cases"%todo)
for x in range(1,n_max+1):
    for y in range(x+1,n_max+1):
        k += 1
        if k > bound:
            bound += inc
            sys.stderr.write('.')
            sys.stderr.flush()

        
        a = modular.power(x,y,n)
        b = modular.power(y,x,n)
        if (a)%n == (b)%n:
            #print(x,y)
            n_found += 2

print("\n",n_found,"found")
