#!/usr/bin/env python

import sys

max_n = int(sys.argv[1])


l1 = [1]
n_over = 0
val = 1000000
for n in range(max_n):
    print(" ".join([str(x) for x in l1]))
    
    l2 = [0]*(len(l1)+1)
    l2[0] = l2[-1] = 1
    for i in range(1,len(l2)-1):
        l2[i] = l1[i] + l1[i-1]
        if l2[i] > val:
            n_over += 1
            
    l1 = l2
    
print(" ".join([str(x) for x in l1]))
print("Over %d: %d"%(val,n_over))
