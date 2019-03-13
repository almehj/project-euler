#!/usr/bin/env python3

n = 2**1000
s = str(n)
print(n)

total = 0
for c in s:
    total += int(c)

print(total)
