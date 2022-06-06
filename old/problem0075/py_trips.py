#!/usr/bin/env python

import sys
import getopt
from factor import gcd

def py_trip(t,s):
    a = (s*s - t*t)
    b = 2*s*t
    c = (s*s + t*t)

    return (int(a),int(b),int(c))
    
    

def main():

    optlist,args = getopt.getopt(sys.argv[1:],"")

    for p_max in args:
        p_max = int(p_max)

        t = 1
        n_ways = [0]*(p_max+1)
        done = False
        while not done:
            s = t+1
            if sum(py_trip(t,s)) > p_max:
                break
            
            while True:
                if (gcd(t,s) == 1) and (t%2==0 or s%2==0):            
            
                    base = py_trip(t,s)
                    base_p = sum(base)
                    if base_p > p_max:
                        break

                    n_k = p_max//base_p

                    for k in range(1,n_k+1):
                        p = base_p*k
                        n_ways[p] += 1

                s += 1
            t += 1

        total = 0
        for i,n in enumerate(n_ways):
            if n == 1:
                print("goo",i)
                total += 1

        print(p_max,total)

        
if __name__ == "__main__":
    main()
