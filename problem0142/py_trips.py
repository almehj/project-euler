#!/usr/bin/env python


import sys
import factor
from math import sqrt


def is_perfsq(n):
    if n < 0:
        return False

    rn = sqrt(n)
    if rn == int(rn):
        return True

    return False


def check(a, b, c):
    if not is_perfsq(c - b) or \
            not is_perfsq(c + b) or \
            not is_perfsq(c - a) or \
            not is_perfsq(c + a) or \
            not is_perfsq(b - a) or \
            not is_perfsq(b + a):
        return False

    return True


def main():
    t_max = int(sys.argv[1])

    t = 1
    while t <= t_max:
        s = t + 1
        while s <= t_max:
            if (s % 2 == 0 or t % 2 == 0) and factor.gcd(s, t) == 1:
                ba = s * s - t * t
                bb = 2 * s * t
                bc = s * s + t * t

                if ba > bb:
                    ba, bb = bb, ba

                k = 1
                while k <= t_max:
                    a = k * ba
                    b = k * bb
                    c = k * bc

                    if check(a, b, c):
                        print(a, b, c, ":", c - a, c - b, b - a, c + a, c + b, b + c)
                    k += 1
            s += 1
        t += 1


if __name__ == "__main__":
    main()
