#!/usr/bin/env python


import sys
from math import log10


def relevant(n):
    d1 = n % 10
    nd = int(log10(n))
    d2 = n//10**nd

    return d1 <= d2


def odd_digits(n):
    while n > 0:
        d = n % 10
        if d % 2 == 0:
            return False
        n //= 10

    return True


def reverse(n):
    answer = 0

    while n > 0:
        d = n % 10
        answer *= 10
        answer += d
        n //= 10

    return answer


def main():
    n_max = int(sys.argv[1])

    n_rev = 0
    n = 10
    while n <= n_max:
        if n % 10 != 0 and relevant(n):
            rn = reverse(n)
            sn = n + rn
            if odd_digits(sn):
                n_rev += 2
                #print("%d + %d = %d" % (n, rn, sn))
        n += 1
        if n%1000000 == 0:
            sys.stderr.write('.')
            sys.stderr.flush()

    print("\n\n%d reversibles" % n_rev)


if __name__ == "__main__":
    main()
