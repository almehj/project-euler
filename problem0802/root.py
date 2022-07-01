#!/usr/bin/env python

def f(x):
    return x*(1-x)**3 - .25

def yfunc(x):
    return .5 / (1-x)

import sys

x_min = float(sys.argv[1])
x_max = float(sys.argv[2])

x = (x_min + x_max)/2.
y = f(x)


max_iter = 100
n = 0
while abs(y) > 1.e-6 and n < max_iter:

    print(x,y,x_min,x_max)
    
    if y > 0.:
        x_max = x
    else:
        x_min = x

    x = (x_min + x_max)/2.
    y = f(x)
    n += 1

print(x,yfunc(x))
