#!/usr/bin/env python

def gcd(a,b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a


def factors(n):
    answer = []

    f = 2
    while n > 1:
        while n%f == 0:
            answer.append(f)
            n //= f
        f += 1

    return answer


def n_divisors(n):
    answer = 1

    fs = factors(n)
    es = {}
    for f in fs:
        if f not in es:
            es[f] = 0
        es[f] += 1

    for e in es.values():
        answer *= (e+1)

    return answer
