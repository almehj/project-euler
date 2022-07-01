#!/usr/bin/env python

from math import pi

def f(x,y):

    new_x = x**2 - x - y**2
    new_y = 2*x*y - y + pi

    return new_x,new_y


import sys

x = float(sys.argv[1])
y = float(sys.argv[2])

iter_max = 10

if len(sys.argv) > 3:
    iter_max = int(sys.argv[3])


n = 0
while n < iter_max:
    print(x,y)
    x,y = f(x,y)
    n += 1
