#!/usr/bin/env python3

import sys
import prime_numbers

max_val = int(sys.argv[1])

below = []
for n in prime_numbers.existing_primes:
    if n <= max_val:
        below += [n]
    else:
        break

print("%d primes, max %d"%(len(below),max(below)))

max_sum = below[0]
max_ndx = 1
sums = []
while max_sum < max_val:
    sums += [max_sum]
    max_sum += below[max_ndx]
    max_ndx += 1

n_live = len(sums)
base_ndx = 0
max_len = -1
max_base = -1
max_sum = -1

print("Initially there are %d elements alive"%(n_live))
while n_live > max_len and base_ndx < len(below) - 1:
    for i,n in enumerate(sums[:n_live]):
        if n in below:
#            print("%d is prime and sum of %d primes"%(n,i+1))
            if max_len < i+1:
                max_len = i+1
                max_base = base_ndx
                max_sum = sums[i]
                
        sums[i] -= below[base_ndx]
        sums[i] += below[base_ndx+i+1]

        if sums[i] >= max_val:
            n_live = i+1
            break
    base_ndx += 1
    print("New base is %d, %d still alive"%(base_ndx,n_live))
    
print("Max length is %d summing to %d starting with %d: %s"%
      (max_len,max_sum,below[max_base]," ".join([str(n) for n in below[max_base:max_base+max_len]])))
