#!/usr/bin/env python3

import sys
import getopt
from math import sqrt

def n_term(n):
    return 1 + 2 * n * (n -1)

def calc_blue(n):
    return .5*(1. + sqrt(n_term(n)))
    

def find_min_total(n):

    disc = 1 - 2*(1 - n**2)
    if disc < 0:
        return 0
    flt_val = .5*(1 + sqrt(disc))

    return flt_val


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


    n_max = int(sys.argv[1])
    n_min = int(10**12*sqrt(2) - 1)
    
    print("Searching up to n^2 == (%d)^2 == %d (%10.5e)"%(n_max,n_max**2,float(n_max**2)))
    print("  n_max implies t_max of ~%10.5e"%(float(n_max)/sqrt(2.)))
    print("  n_min ==",n_min)
    
    n = n_min
    i = 1
    if n%2 == 0:
        n -= 1
    while n < n_max:
        t = int(find_min_total(n))

        while n_term(t-1) < n**2:
            if n_term(t) == n**2 and n%2 != 0:
                print("   FOUND ONE!")
                b = int(calc_blue(t))
                r = t - b
                print(t,n,n_term(t),n**2,"  b:",b," r:",r)
            t += 1

        
        n += 2
        if i%100000 == 0:
            tn = n_term(find_min_total(n))
            print("  ",n**2,int(tn),n**2 - int(tn))
        i += 1
        

            
if __name__ == "__main__":
    main()
