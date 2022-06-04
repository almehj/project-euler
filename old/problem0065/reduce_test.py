#!/usr/bin/env python

import sys
import prime_numbers

def parse(frac):
    bits = frac.split(',')
    if len(bits) != 2:
        print("Huh?")
        return 0,0

    num = int(bits[0].strip())
    den = int(bits[1].strip())

    return num,den

def product(fact_l):
    answer = 1

    for f,p in fact_l:
        answer *= f**p

    return answer

for frac in sys.argv[1:]:
    num,den = parse(frac)

    num_f = prime_numbers.factorization(num)
    den_f = prime_numbers.factorization(den)

    print("num: %d: %s"%(num,num_f))
    print("den: %d: %s"%(den,den_f))


    for t in num_f[:]:
        fact = t[0]
        l = [g for g in den_f if g[0] == fact]
        if len(l) > 0:
            num_f.remove(t)
            for k in l:
                den_f.remove(k)
                if t[1] < k[1]:
                    den_f.append((k[0],k[1]-t[1]))
                elif t[1] > k[1]:
                    num_f.append((t[0],t[1]-k[1]))


    print("num: %d: %s"%(product(num_f),num_f))
    print("den: %d: %s"%(product(den_f),den_f))

    print("\n  ")
