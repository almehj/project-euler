#!/usr/bin/env python3

import sys

from utils import binary_str

def is_palindrome(n):
    digits = str(n)
    seq_len = len(digits)//2

    odd_offset = len(digits)%2
    half1 = digits[:seq_len]
    half2 = "".join(reversed(digits[seq_len+odd_offset:]))

    return half1 == half2

def main():
    max_val = int(sys.argv[1])

    n_both = 0
    total_both = 0
    for n in range(1,max_val+1):        
        if is_palindrome(n):
            bn = binary_str(n)

            if is_palindrome(bn):
                print("%d and %s"%(n,bn))
                n_both += 1
                total_both += n
                
    print("\n%d double-base palinddromes total to %d"%(n_both,total_both))
if __name__ == "__main__":
    main()
    
