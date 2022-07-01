#!/usr/bin/env python

import sys


def main():
    d_max = int(sys.argv[1])

    totient = {}
    totient[0] = 0
    totient[1] = 1
    d = 2
    goal_num = 15499
    goal_den = 94744

    min_frac = 1.

    while d <= d_max:
        # Compute totient
        if d not in totient:
            totient[d] = d - 1
            n = 2
            while n * d <= d_max:
                if n*d not in totient:
                    totient[n*d] = []
                totient[n * d].append(d)
                n += 1
        else:
            tv = d
            for f in totient[d]:
                tv *= (1 - 1 / f)
            totient[d] = int(tv)

        # Is this it?
        num = totient[d]
        den = d - 1

        if num/den < min_frac:
            min_frac = num/den
        print("%d: %d/%d (= %f) < %d,%d (= %f) min: %f" % (d,num, den, num / den, goal_num, goal_den, goal_num / goal_den, min_frac))

        if d == 94745:
            break

        if num * goal_den < den * goal_num:
            # Found it!
            break

        d += 1


if __name__ == "__main__":
    main()
