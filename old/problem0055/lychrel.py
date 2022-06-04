#!/usr/bin/env python

import sys


def is_palindrome(n):

    digits = list(str(n))

    for i in range(len(digits)//2):
        if digits[i] != digits[-i-1]:
            return False

    return True

def reverse_digits(n):
    digits = list(str(n))
    digits.reverse()

    return int(''.join(digits))


exist_lychrels = []
max_tries = 50

def is_lychrel(n):
    if n in exist_lychrels:
        return True

    i = 0
    while i < max_tries:

        n = n + reverse_digits(n)
        if is_palindrome(n):
            return False
        elif n in exist_lychrels:
            print("cache!")
            return True
        
        i += 1

    return True


    
max_n = int(sys.argv[1])
n = 1
total = 0
while n <= max_n:

    if is_lychrel(n):
        total += 1
        print("  ",n,"is lychrel")
    n+=1

print(total)
