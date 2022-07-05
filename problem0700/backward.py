#!/usr/bin/env python

import sys



a = 1504170715041707
m = 4503599627370517
f = 3451657199285664


def euler(n):
    return (a*n)%m

n = f
i = 0
while i < 20:
    print(n,euler(n))
    n -= 1
    i += 1
