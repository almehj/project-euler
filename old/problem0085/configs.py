#!/usr/bin/env python

import sys

ideal = 2000000
min_diff = 1000000000000
min_diff_size = 2

max_n = int(sys.argv[1])
max_m = int(sys.argv[2])


n = 1

while n <= max_n:
    m = n
    nf = n*(n+1)//2
    if nf > ideal:
        break
    while m <= max_m:
        mt = m*(m+1)*nf//2
        diff = abs(mt - ideal)
        if diff < min_diff:
            min_diff = diff
            min_diff_size=m,n
            print(n,m,mt,diff)
            
        if mt > ideal:
            break
        m += 1
    n+=1

print(" ")
print(min_diff_size[0],min_diff_size[1],min_diff,min_diff_size[0]*min_diff_size[1])

