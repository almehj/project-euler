#!/usr/bin/env python

import sys
from functools import reduce

max_n = int(sys.argv[1])

nums = {}
primes = {}

n = 2
while n <= max_n:
    if n not in nums:
        k = 1
        while k*n <= max_n:
            if k*n not in nums:
                nums[k*n] = []
            base = k
            m = 1
            while base %n == 0:
                m += 1
                base //= n
            nums[k*n] += [n]*m
            k += 1
    n += 1



def sum_posibles(fn):

    if len(fn) <= 2:
        return [fn]

    print("considering",fn)
    for i in range(len(fn)):
        for j in range(i+1,len(fn)):
            a = fn[i]
            b = fn[j]
            fn.remove(a)
            fn.remove(b)
            
for n in range(k,max_n+1):
    fn = nums[n]
    lfn = len(fn)
    
    if lfn <= 1:
        continue
        
    sfn = sum(fn)
    print(n,sfn,n-sfn,fn)
            
