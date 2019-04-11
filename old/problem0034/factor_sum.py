#!/usr/bin/env python

import sys

from utils import seq_string

def build_factorials(n):
    answer = [1]*n
    for i in range(1,n):
        for j in range(i,n):
            answer[j] *= i

    return answer

digit_factorials = build_factorials(10)

def digits(n):
    return [int(c) for c in str(n)]

def factorial_check(n):
    return n == sum([digit_factorials[i] for i in digits(n)])

def print_report(n):
    factorials = [digit_factorials[i] for i in digits(n)]
    digit_strs = ["%d!"%(i) for i in digits(n)]
    
    print("%d: %s == %s"%
          (
              n,
              seq_string(digit_strs,separator=" + "),
              seq_string(factorials,separator=" + ")
          )
    )
    
def main():

    max_val = int(sys.argv[1])
    
    total = 0
    for n in range(3,max_val+1):
        if factorial_check(n):
            total += n
            print_report(n)
    print("\nTotal is %d"%(total))



if __name__ == "__main__":
    main()
