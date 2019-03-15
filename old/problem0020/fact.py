#!/usr/bin/env python3

def fact(n):

    prod = 1
    while n != 1:
        prod *= n
        n -= 1

    return prod


total = 0
for c in str(fact(100)):
    total += int(c)


print(total)
