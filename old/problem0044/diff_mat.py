#!/usr/bin/env python


def pent(n):
    return int((3*n*n - n)/2)


len_arr = 10000

pents = [pent(n+1) for n in range(len_arr)]

for i in range(len_arr//2):
    
    for j in range(i+1,len_arr//2):
        d = abs(pents[i] - pents[j])
        s = pents[i] + pents[j]
        if d in pents and s in pents:
            print("Found ",i,j,pents[i],pents[j],d,s)
    
