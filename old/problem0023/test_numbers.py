#!/usr/bin/env python3

import sys
import prime_numbers

def verbose_report(n,d_list):
    s = sum(d_list)
    result = None
    if s == n:
        result = "perfect"
    elif s < n:
        result = "deficient"
    else:
        result = "abundant"
        
    sum_str = " + ".join([str(d) for d in d_list])
    print("%d is %s: %s = %d"%(n,result,sum_str,s))


def main():
    max_val = int(sys.argv[1])
    step = 1
    start = 2
    if len(sys.argv[1:]) > 1:
        step = int(sys.argv[2])
        start = step

    result = []
    for n in range(start,max_val+1,step):

        d_list = prime_numbers.divisors(n)
        d_list.remove(n)
        verbose_report(n,d_list)

if __name__ == "__main__":
    main()
