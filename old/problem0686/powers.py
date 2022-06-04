#!/usr/bin/env python

import sys

lead = sys.argv[1]
lead = lead.strip()
min_l = len(lead)

max_pow = int(sys.argv[2])

n = 1
power = 0
n_occurs = 0
last_answer = 0
for i in range(max_pow+1):
    str_n = str(n)
    if len(str_n) >= min_l:
        if str_n[:min_l] == lead:
            n_occurs += 1
            print("%10d"%(n_occurs),power,power-last_answer)
            last_answer = power
            sys.stdout.flush()
    n *= 2
    power += 1
    

    
