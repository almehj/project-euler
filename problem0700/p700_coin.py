#!/usr/bin/env python


import sys

a = 1504170715041707
m = 4503599627370517

n_a = int(m/a) + 1
dn = (a*n_a)%m

coins = [a]
n = dn
while True:
    if n < coins[-1]:
        print("found",n,"<",coins[-1])
        delta = coins[-1] - n
        coins.append(n)

        while n > delta:
            n -= delta
            print("found",n,"<",coins[-1])
            coins.append(n)

        dist = a - n
        n_inc = int(dist/dn) + 1
        dn = (n_inc*dn)%a

    n += dn
    n %= a



