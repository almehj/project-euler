#!/usr/bin/env python3

from math import log10

def n_digits(n):
    return int(log10(n)) + 1

def main():

    f1=f2=1
    n = 2

    while True:
        print("%4d (%3d): %10d"%(n,n_digits(f2),f2)) 
        if n_digits(f2) >= 1000:
            break
        
        t = f1+f2
        f1 = f2
        f2 = t
        n+=1



if __name__ == "__main__":
    main()
