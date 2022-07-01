#!/usr/bin/env python


import sys


n = 0
m = 1000000007

v = 1

while n < int(sys.argv[1]):
    v_old = v;
    v = (v*10**11)%m
    delta = v - v_old
    print(n,v,delta)
    n += 1
    
