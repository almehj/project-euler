#!/usr/bin/env python


import sys


def is_bouncy(n):
    if n < 100:
        return False

    d0 = n%10
    n //= 10
    dir = 0
    while n > 0:
        d = n%10
        if dir == 0:
            if d > d0:
                dir = 1
            elif d < d0:
                dir = -1
        else:
            if dir == 1:
                if d < d0:
                    return True
            else:
                if d > d0:
                    return True
        d0 = d
        n//=10

    return False


def main():
    n_max = int(sys.argv[1])

    n_bounce = 0
    n = 100
    goals = {}
    bounds = [(1,2,50),(9,10,90),(99,100,99)]
    goal_ndx = 0
    a,b,frac = bounds[goal_ndx]

    while n <= n_max:
        bounce = "      "
        if is_bouncy(n):
            n_bounce += 1
            bounce = "BOUNCY"

        print(n,bounce, n_bounce,"%.4f"%(n_bounce/n))

        if a*n == b*n_bounce:
            if frac not in goals:
                print("****** %d%% ******"%frac)
                goals[frac] = 1
            goal_ndx += 1
            if goal_ndx >= len(bounds):
                sys.exit(0)
            a, b, frac = bounds[goal_ndx]

        n += 1


if __name__ == "__main__":
    main()







