#!/usr/bin/env python3

import sys
import prime_numbers

def main():
    max_val = int(sys.argv[1])

    result = {}
    for n in range(2,max_val):
        d_list = prime_numbers.divisors(n)
        d_list.remove(n)

        s = sum(d_list)
        if s < max_val:
            result[n] = s

    total = 0
    for n in result:
        Dn = result[n]
        if n >= Dn:
            continue
        if Dn in result and result[Dn] == n:
            print("%d %d"%(n,Dn))
            total += n+Dn

    print("Total is %d"%(total))
    

if __name__ == "__main__":
    main()
