#!/usr/bin/env python

import sys

i_max = int(sys.argv[1])

a = 1504170715041707
m = 4503599627370517
f = 3451657199285664


def euler(n):
    return (a*n)%m

n = 1
i = 0
past = []
coin = a
coin_n = 1
while i < i_max:
    x = euler(n)
    past.append(x)
    diff = 0
    if i > 2:
        diff = past[i]-past[i-3]

    is_coin = " "
    if x < coin:
        is_coin = "COIN %7d %d"%(n - coin_n, euler(n - coin_n))
        coin = x
        coin_n = n
        print("%18d %18d %20d %18d %s "%(n,x,diff,diff%m,is_coin))
    n += 1
    i += 1
