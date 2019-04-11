#!/usr/bin/env python3

coeff = 28433
exp = 7830457
#exp = 5

a = 10000000000

prev = []
n = 1
i = 0
while i < exp:
    n *= 2
    n %= a
    i += 1

print(n)
print(n*coeff + 1)

