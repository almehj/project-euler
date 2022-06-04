#!/usr/bin/env python
import sys

def same_digits(a,b):

    da = list(str(a))
    db = list(str(b))

    da.sort()
    db.sort()

    return int("".join(da)) == int("".join(db))


facts = [2,3,4,5,6]

start = 16
min_val = 10
n = start

while True:

    good = True
    for f in facts:
        if not same_digits(n,f*n):
            good = False
            break
    if good:
        print(n)
        for f in facts:
            print(" *%d = %d"%(f,n*f))
        sys.exit(0)

    n -= 1
    if n < min_val:
        start *= 10
        start += 6
        n = start
        min_val *= 10

        print("Bumps to %d"%start)
