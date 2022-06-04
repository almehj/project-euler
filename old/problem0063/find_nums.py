#!/usr/bin/env python

from math import log10

lv = [log10(x) for x in range(1,10)]
lv.reverse()

print(lv)

n = 1
total = 0
while True:
    ln = 1 - 1/n
    print(ln)
    if ln > lv[0]:
        break

    for i,v in enumerate(lv):
        if v < ln:
            break
        print("%d^%d = %d"%(9-i,n,(9-i)**n))
        total += 1

    n += 1

print(total)

