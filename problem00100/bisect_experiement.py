#!/usr/bin/env python3

import sys
import getopt
from math import sqrt

def n_term(n):
    return 1 + 2. * n * (n -1)

def calc_blue(n):
    return .5*(1. + sqrt(n_term(n)))
    

def find_perfect(t_min):
    n = 1
    nsq = 1
    t = t_min

    while t < 10*t_min:
        nt = n_term(t)
        while nt > nsq:
            n += 1
            nsq = n*n
        if nt == nsq:
            print("%d %d %d"%(t,nt,nsq))
            return 
        t += 1




def main():

    
    find_perfect(int(sys.argv[1]))
    
#    for val in sys.argv[1:]:
#        n = int(val)
#        prev_nt = n_term(n)
#        for i in range(n,n+20):
#            nt = n_term(i)            
#            print("%d: %d (%d) (%d)"%(i,nt,nt-prev_nt,nt-prev_nt -(4*i-2)))
#            prev_nt = nt


            
if __name__ == "__main__":
    main()
