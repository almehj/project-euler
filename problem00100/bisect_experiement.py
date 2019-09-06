#!/usr/bin/env python3

import sys
import getopt
from math import sqrt

def n_term(n):
    return 1 + 2. * n * (n -1)

def calc_blue(n):
    return .5*(1. + sqrt(n_term(n)))
    

def find_min_total(n):

    disc = 1 - 2*(1 - n**2)
    if disc < 0:
        return 0
    flt_val = .5*(1 + sqrt(disc))

    return int(flt_val)


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


    n = int(sys.argv[1])

    print(n_term(n))
    sys.exit(10)
    
    for i in range(n,n*10):
        #print("%d %d: %d"%(i,i**2,find_min_total(i)))
        n = find_min_total(i)
        while n_term(n) <= i**2:
            if n_term(n) == i**2:
                print("   *** FOUND: %d => %d == %d"%(n,n_term(n),i**2))
                print("              %d blue, %d red"%(calc_blue(n),n-calc_blue(n)))
                sys.exit()

            n += 1
        
#    for val in sys.argv[1:]:
#        n = int(val)
#        prev_nt = n_term(n)
#        for i in range(n,n+20):
#            nt = n_term(i)            
#            print("%d: %d (%d) (%d)"%(i,nt,nt-prev_nt,nt-prev_nt -(4*i-2)))
#            prev_nt = nt


            
if __name__ == "__main__":
    main()
