#!/usr/bin/env python


import sys


a = 1504170715041707
m = 4503599627370517


def dumb_factor(n):
    answer = []
    f = 2

    while n > 0:
        if n % f == 0:
            answer.append(f)
            n //= f
        else:
            if f == 2:
                f = 3
            else:
                f += 2
    return answer


def euler_val(n):
    answer = n
    answer *= a
    answer %= m

    return answer


coins = [a]
n = 1
print("Found", a, "<", "Infinity","it's number",n)
print("N_ONLY", 1)
while True:
    v = euler_val(n)
    if v < coins[-1]:
        print("Found", v, "<", coins[-1],"it's number",n,"%.2e"%(float(n)/a))
        print("N_ONLY",n)
        sys.stdout.flush()
        coins.append(v)
    n += 1
