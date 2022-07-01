#!/usr/bin/env python


import sys


def is_increasing(n):

    d0 = n%10
    n //= 10
    while n > 0:
        d = n%10
        if d > d0:
            return False
        d0 = d
        n //= 10

    return True


def is_decreasing(n):

    d0 = n%10
    n //= 10
    while n > 0:
        d = n%10
        if d < d0:
            return False
        d0 = d
        n //= 10

    return True


def is_steady(n):
    d = n%10

    while n > 0:
        if n%10 != d:
            return False
        n //= 10

    return True


e_max = int(sys.argv[1])

if e_max < 10:
    n_max = str(10**e_max)
else:
    n_max = "10^%d"%e_max
    
print("Increasing numbers less than",n_max)

num_poss = {0:0}
for i in range(1,10):
    num_poss[i] = 1

e = 1
while e < e_max:
    old_poss = [num_poss[d] for d in range(10)]
    for d in range(10):
        num_poss[d] = sum(old_poss[d:])
    e += 1

n_inc_new = sum([num_poss[d] for d in range(10)])

print("Decreasing numbers less than",n_max)
num_poss = {0: 0}
for i in range(1, 10):
    num_poss[i] = 1
e = 1
while e < e_max:
    old_poss = [num_poss[d] for d in range(10)]
    num_poss[0] = sum(old_poss)
    for d in range(1,10):
        num_poss[d] = sum(old_poss[1:d+1]) + 1
    e += 1

n_dec_new = sum([num_poss[d] for d in range(10)])

n_ste_new = 9*e_max

print(n_inc_new,"increasing with new calc")
print(n_dec_new,"decreasing with new calc")
print(n_ste_new,"steady with new calc")

print("total =", n_inc_new + n_dec_new - n_ste_new)

if e_max < 10:
    n_max = 10**e_max
    n = 1
    n_increase = 0
    n_decrease = 0
    n_steady = 0
    n_bounce = 0
    while n < n_max:
        bounce = True
        if is_increasing(n):
            #print("INC:",n)
            bounce = False
            n_increase += 1
        if is_decreasing(n):
            #print("DEC:",n)
            bounce = False
            n_decrease += 1
        if is_steady(n):
            #print("STE:",n)
            bounce = False
            n_steady += 1
        if bounce:
            #print("BNC:",n)
            n_bounce += 1
        n += 1

    print("Using old calc:",n_increase,"up or steady,",n_decrease,"down or steady,",n_steady,"steady,",n_bounce,"bouncy")
    print("total =",n_increase+n_decrease-n_steady+n_bounce)