#!/usr/bin/env python3

power_set = []

for i in range(2,101):
    for j in range(2,101):
        n = i**j
        if n not in power_set:
            power_set.append(n)
        else:
            if i != j:
                print("%d^%d (%d) == %d^%d (%d)"%(i,j,n,j,i,j**i))
                
print(len(power_set))
