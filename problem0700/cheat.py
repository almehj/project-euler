#!/usr/bin/env python

import sys

i_max = int(sys.argv[1])

a = 1504170715041707
m = 4503599627370517
f = 3451657199285664
d = 8912517754604

def euler(n):
    return (a*n)%m

n = 1
i = 0
past = []
coin = a

while i < i_max:
    print(coin)
    coin = (coin - d)%m
    i += 1
