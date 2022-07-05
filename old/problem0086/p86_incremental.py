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

M = int(sys.argv[1])

n_int = 0
n_tot = 0
a = 1


max_n = 1
while max_n <= M:
    a = 1
    while a <= max_n:
        b = a
        while b <= max_n:
            c = b
            while c <= max_n:
                if (a*b*c) > 0 and (a == max_n or b == max_n or c == max_n):
                    print("     ",a,b,c)
                    n_tot += 1
                    if (c,a+b) in trips:
                        print(a,b,c,":",trips[(c,a+b)])
                        n_int += 1
                c+=1
            b+=1
        a+=1
    print("report:",max_n,n_int,n_tot)
    max_n += 1
print("\n")    
print(n_int,"integer paths")
print(n_tot,"cuboids")
