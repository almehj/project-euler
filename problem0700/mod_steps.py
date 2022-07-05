#!/usr/bin/env python


import sys


n0 = int(sys.argv[1])
dn = 8912517754604
a = 1504170715041707

n = n0

ops = 0
while n >= n0:
    n += dn
    n %= a
    ops += 1

print(n0,n,ops,n0-n)

