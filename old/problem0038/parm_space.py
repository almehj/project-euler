#!/usr/bin/env python

import sys

def len_int(n):
    return len(str(n))

def gen_pandigital(n,max_m):

    return "".join([str(n*i) for i in range(1,max_m+1)])
    

def check_pangigital(n):
    digits = [int(i) for i in list(str(n))]

    for i in range(1,10):
        if digits.count(i) != 1:
            return False

    return True

def main():

    max_m = int(sys.argv[1])
    for m in range(1,max_m+1):
        n = 0
        i =1
        while n < 9:
            n += len_int(m*i)
            i += 1
        if n == 9 and check_pangigital(gen_pandigital(m,i-1)):
            print(m,i-1,gen_pandigital(m,i-1))


        
if __name__ == "__main__":
    main()
    
