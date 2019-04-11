#!/usr/bin/env python3

import prime_numbers
import itertools

def is_abundant(n):
    d_l = prime_numbers.divisors(n)
    d_l.remove(n)
    return sum(d_l) > n
    

max_val = 28123
#max_val = 281

print("Building required abundant list")
abundants = [n for n in range(2,max_val+1) if is_abundant(n)]
print("%d abundant numbers < %d"%(len(abundants),max_val))

print ("Building cross sums")
cross = []
for i in range(len(abundants)):
    for j in range(i,len(abundants)):
        cross_sum = abundants[i]+abundants[j]
        if cross_sum <= max_val:
            cross += [cross_sum]

print ("Sorting cross sums")
cross.sort()

print ("Uniquing cross sums")
unique = [0]
for n in cross:
    if n != unique[-1]:
        unique += [n]
print ("Start of unique: %s"%(" ".join([str(n) for n in unique[:100]])))
print("%d unique two-element sums"%(len(unique)))

print("Summing cross sums")
cross_tot = sum(unique)

total = max_val*(max_val+1)/2
print("Full sum is %d"%(total))
print("Less cross sum sums is %d"%(total-cross_tot))

