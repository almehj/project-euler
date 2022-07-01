#!/usr/bin/env python


import sys

a = 1504170715041707
m = 4503599627370517

def euler_val(n):
    answer = n
    answer *= a
    answer %= m

    return answer


n_laps = m // a
n_a = n_laps + 1
m_inc = n_a * a
dn = m_inc % m
coins = [a]
n = a
while True:
    if n < coins[-1]:
        print(n,"<",coins[-1],coins[-1]-n)
        delta = coins[-1] - n
        coins.append(n)
        while n > delta:
            n -= delta
            print(n, "<", coins[-1], coins[-1] - n)
            coins.append(n)

    if n <= 1:
        break

    n = (n+dn)%a




print("\nSum is",sum(coins))
