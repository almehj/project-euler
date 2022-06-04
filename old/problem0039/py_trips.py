#!/usr/bin/env python

import sys
import getopt
from factor_tools import gcd

def main():

    optlist,args = getopt.getopt(sys.argv[1:],"")

    max_p = int(args[0])
    perims = {}
    n = 1

    
    while True:
        m = n+1        
        while True:

            if (m%2 == 0 or n%2 == 0) and gcd(n,m) == 1:

                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2

                p = a+b+c
                n_k = max_p // p

                for k in range(1,n_k+1):
                    print(a*k,b*k,c*k)
                    if k*p not in perims:
                        perims[k*p] = 0
                    perims[k*p] += 1
                        
                if n_k < 1:
                    break
            m += 1


        n += 1
        if n > max_p:
            break

    perim_list = [(perims[p],p) for p in perims]
    perim_list.sort()
    print(perim_list)
    

    

    
if __name__ == "__main__":
    main()
