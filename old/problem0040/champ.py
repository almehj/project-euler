#!/usr/bin/env python

import sys


tot_digits = 0
max_digits = int(1.e6)

base = 1
nine = 9
ndx = 1
increments = [0]
max_ndxs = [0]

while tot_digits <= max_digits:
    increment = base*nine
    tot_digits += increment
#    print ("%2d: %7d %7d"%(base,increment,tot_digits))

    increments.append(increment)
    max_ndxs.append(tot_digits)
    
    base += 1
    nine *= 10


def nth_digit(n):

    # find with length section we are in
    l = 1
    while max_ndxs[l] < n:
        l += 1
    print("  %d length section"%(l))
    # adjust n to start of section
    n -= max_ndxs[l-1]
    n -= 1
    print("  Adjusted index",n)
    # which number?
    sec_ndx = n // l
    sec_num = sec_ndx + 10**(l-1) 
    print("  section index",sec_ndx)
    print("  section number",sec_num)
    digit_ndx = l - n%l - 1
    print("  digit index",digit_ndx)
    while digit_ndx > 0:
        sec_num //= 10
        digit_ndx -= 1
    answer = sec_num%10
    print(" Answer is",answer)
    
    
    
    return answer


def main():

    product = 1
    for n in sys.argv[1:]:
        n = int(n)
        nth = nth_digit(n)
        product *= nth
        
        print("Digit %d is %d (product %d)"%(n,nth,product))


if __name__ == "__main__":
    main()
