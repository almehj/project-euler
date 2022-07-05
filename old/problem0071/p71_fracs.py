#!/usr/bin/env python

def gcd(a,b):

    while b != 0:
        t = b
        b = a%b
        a = t

    return a


crit_num = 3
crit_den = 7
crit_frac = float(crit_num)/crit_den

curr_num = 0
curr_den = 1
curr_frac = 0.

import sys

d_max = int(sys.argv[1])

d = 2
while d <= d_max:
    c_val = d*crit_num
    n = c_val//crit_den 
    if n < 1: n = 1
    while n < d:        
        # n/d: reduced proper fraction?
        if gcd(n,d) == 1:

            # less than critical? If not we can quit this value of d
            if n*crit_den >= crit_num*d:
                break

            # bigger than current? if so keep
            if n*curr_den > curr_num*d:

                frac = float(n)/d
                
                #print("%d/%d > %d/%d and %f < %f"%(n,d,curr_num,curr_den,curr_frac,crit_frac))
            
                curr_num = n
                curr_den = d
                curr_frac = frac
        n += 1
        
    d+= 1

print (curr_num,"/",curr_den)
