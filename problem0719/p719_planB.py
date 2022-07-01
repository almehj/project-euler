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
                new_s.append(a)
            new_plan.append(new_s)

    return new_plan


nums = {}


def check_plan(r, n, plan):

    tot = 0

    stop_ndx = 1
    curr_n = 0
    for i,d in enumerate(n):
        if stop_ndx < len(plan) and i == plan[stop_ndx]:
            tot += curr_n
            curr_n = d
            stop_ndx += 1
        else:
            curr_n *= 10
            curr_n += d
    tot += curr_n
    if tot == r:
        # print("   ",n,":"," + ".join(splits),"=",tot,"=",r)
        return True

    return False


digits = "0123456789ABCDEF"


def main():
    plans = {}
    for n in range(2, 14):
        plan = gen_plan(n)
        plans[n] = plan

    n_max = int(sys.argv[1])

    r = 4
    n = r ** 2

    total = 0

    while n <= n_max:
        digits_n = [int(d) for d in str(n)]
        for p in plans[len(digits_n)]:
            if check_plan(r, digits_n, p):
                total += n
                break
        if r % 10000 == 0:
            sys.stdout.write('%')
            sys.stdout.flush()

        r += 1
        n = r ** 2

    print(" ")
    print("T(%d) = %d" % (n_max, total))


if __name__ == "__main__":
    main()
