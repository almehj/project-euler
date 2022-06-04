#!/usr/bin/env python

from math import log10
import sys

log_2 = log10(2)

log_lo = log10(1.23)
log_hi = log10(1.24)


for max_n in [int(s) for s in sys.argv[1:]]:

    p = 1
    n = 0
    while n < max_n: 
        log_n = p*log_2
        log_m = log_n - int(log_n)
        if (log_m >= log_lo) and (log_m < log_hi):
            n += 1
            if n%10000 == 0:
                sys.stdout.write('.')
                sys.stdout.flush()

        p += 1
            

    print("\n",n,p-1)

