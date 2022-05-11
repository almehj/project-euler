#!/usr/bin/env python

import sys
import getopt

def func(n,s):
    return 3*n*n + 2*n*s + 1

def check(n,i):
    A = n*i
    if A%4 == 0:
        print("   found?: n")

def main():

    optlist,args = getopt.getopt(sys.argv[1:],"")

    for n_max in args:
        n_max = int(n_max)
        n = 2
        i = 1
        isq = i*i
        fp = func(n,1)
        fm = func(n,-1)
        while n <= n_max:


            #print ("i:%10d n:%10d %10d %10d %10d"%(i,n,isq,fp,fm))
            if isq == fp:
                print ("(n+1): %10d %10d %20d %20d %20d"%(n,i,isq,fp,fm))
                check(fp,i)
            elif isq == fm:
                print ("(n-1): %10d %10d %20d %20d %20d"%(n,i,isq,fp,fm))
                check(fm,i)
                
            i = i + 1
            isq = i*i

            if isq >= fp:
                n = n + 1
                fp = func(n,1)
                fm = func(n,-1)
                

            
            
        print (" ")


if __name__ == "__main__":
    main()
