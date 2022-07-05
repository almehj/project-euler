#!/usr/bin/env python

import sys
import cProfile


def all_combos(n):
    if len(n) == 1:
        return [[n]]

    answer = []
    d = n[0]
    for l in all_combos(n[1:]):
        cd = d + l[0]
        answer.append([cd] + l[1:])
        answer.append([d] + l)

    return answer


combo_plans = {}


def gen_plan(n):
    n_str = ''.join([digits[d] for d in range(n)])
    plan = all_combos(n_str)

    l_max = int(n / 2. + 0.5)
    new_plan = []
    for s in plan:
        l_max_plan = max([len(m) for m in s])
        if l_max_plan == l_max or l_max_plan == l_max - 1:
            new_s = []
            for n in s:
                a = digits.index(n[0])
                b = digits.index(n[-1]) + 1
                new_s.append((a, b))
            new_plan.append(new_s)

    return new_plan


nums = {}


def setup_numbers(n_max):
    sys.stdout.write("setting up %d numbers..." % n_max)
    sys.stdout.flush()

    n = 1
    while n <= n_max:
        nums[str(n)] = n
        n += 1

    print("done")


def check_plan(r, n, plan):
    n = str(n)
    r = int(r)

    splits = []
    tot = 0
    x = 0
    for a, b in plan:
        # splits.append(n[a:b])
        x = int(n[a:b])
        tot += x
        if tot > r:
            return False

    if tot == r:
        # print("   ",n,":"," + ".join(splits),"=",tot,"=",r)
        return True

    return False


digits = "0123456789ABCDEF"

from math import sqrt


def main():
    plans = {}
    for n in range(2, 14):
        plan = gen_plan(n)
        plans[n] = plan

    n_max = int(sys.argv[1])
    r_max = int(sqrt(n_max)) + 10
    #setup_numbers(r_max)

    r = 4
    n = n ** 2

    total = 0

    while n <= n_max:
        if r % 10000 == 0:
            sys.stdout.write('%')
            sys.stdout.flush()

        r += 1
        n = r ** 2

        l_n = len(str(n))
        for p in plans[l_n]:
            if check_plan(r, n, p):
                total += n
                break

    print(" ")
    print("T(%d) = %d" % (n_max, total))


if __name__ == "__main__":
    main()
