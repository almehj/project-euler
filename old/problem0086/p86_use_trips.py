#!/usr/bin/env python

import sys

trips = {}
with open("trips.txt") as infile:
    for line in infile:
        bits = [int(s) for s in line.split()]
        key1 = (bits[0],bits[1])
        key2 = (bits[1],bits[0])
        
        trips[key1] = bits[2]
        trips[key2] = bits[2]

print(len(trips),"entries")

max_n = int(sys.argv[1])

n_int = 0
n_tot = 0
a = 1

a_frac = max_n//20
frac = a_frac

while a <= max_n:
    if a > frac:
        sys.stderr.write('.')
        sys.stderr.flush()
        frac += a_frac
    b = a
    while b <= max_n:
        c = b
        while c <= max_n:
            n_tot += 1
            if (c,a+b) in trips:
                #print(a,b,c,":",trips[(c,a+b)])
                n_int += 1
            c+=1
        b+=1
    a+=1

sys.stderr.write('\n')
print(n_int,"integer paths")
print(n_tot,"cuboids")
