#!/usr/bin/env python

b = 2.0

for i in range(20):
    print(int(b))
    b = int(b)*(b - int(b) + 1)
    
