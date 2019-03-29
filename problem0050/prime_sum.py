#!/usr/bin/env python

import sys
import prime_numbers

max_val = int(sys.argv[1])
min_len = int(sys.argv[2])

below = prime_numbers.existing_primes[:min_len][:]
for n in prime_numbers.existing_primes[min_len:]:
    if n + sum(below[-min_len:]) <= max_val:
        below += [n]
    else:
        break

print("%d primes, max %d"%(len(below),max(below)))

max_sum = -1
max_start = 0
max_len  = 0

for i in range(len(below) - min_len):
    offset = 0
    n = 0
    if i>0 and i%1000 == 0:
        sys.stdout.write('.')
        sys.stdout.flush()
    while i+offset < len(below) and n + below[i + offset] < max_val:
        n += below[i+offset]
        offset += 1
        
        if offset > 0 and prime_numbers.is_prime(n):
            if offset > max_len:
                max_sum = n
                max_start = i
                max_len = offset 

print(" ")
print("Max length is %d summing to %s"%(max_len,max_sum))
print("  Terms are %s"%(" ".join(str(n) for n in below[max_start:max_start+max_len])))
