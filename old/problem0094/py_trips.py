#!/usr/bin/env python

import sys
import getopt

def main():

    optlist,args = getopt.getopt(sys.argv[1:],"")

    t = 1
    s = 1

    for t_max in args:
        t_max = int(t_max)
        
        t = 1
        tot = 0

        while t <= t_max:
            s = t + 2
            while True:
                a = s*t
                b = (s*s - t*t)/2
                c = (s*s + t*t)/2

                if a > b:
                    a,b = b,a

                if abs(2*a-c) == 1:
                    
                    perim = 2*a + 2*c
                    print("%10d %10d %10d: %2d %12d %12d %8d %8d"%(a,b,c,2*a-c,perim,int(perim-1.e9),t,s))
                    if perim <= int(1.e9):
                        tot = tot + perim

                if 3*c-1 > 1.e9:
                    break
                
                s = s + 2
            t = t + 2

        print("Total: %d"%tot)

if __name__ == "__main__":
    main()
