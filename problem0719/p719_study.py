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
        if len(s) < 2:
            continue
        new_s = []
        for seg in s:
            ex = 10 ** (len(seg) - 1)
            while ex > 0:
                new_s.append(ex)
                ex //= 10
        new_s.reverse()
        new_plan.append(new_s)
    return new_plan


nums = {}


def check_plan(r, n, plan):
    tot = 0
    for i in range(len(n)):
        tot += n[i]*plan[i]

    if tot == r:
        # print("   ",n,":"," + ".join(splits),"=",tot,"=",r)
        return True

    return False


digits = "0123456789ABCDEF"

def dot(a,b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]

    return answer

import random


def main():
    plans = [0]*15
    for n in range(2, 14):
        plan = gen_plan(n)
        plans[n] = plan
        print("Length %d has %d plans"%(n,len(plan)))

    n_max = int(sys.argv[1])

    r =4
    n = r ** 2

    total = 0
    n_plans = {}
    sizes = {}
    for i in range(len(str(n_max))+2):
        n_plans[i] = 0
        sizes[i] = 0

    r_inc = 10000
    r_bound = r_inc
    while n <= n_max:
        digits_n = []
        while n > 0:
            digits_n.append(n%10)
            n //= 10
        len_n = len(digits_n)
        sizes[len_n] += 1
        for p in plans[len_n]:
            n_plans[len_n] += 1
            tot = dot(p,digits_n)
            if tot == r:
                total += r**2
                break
        if r > r_bound:
            sys.stdout.write('%')
            sys.stdout.flush()
            r_bound += r_inc
            while r_bound < r:
                sys.stdout.write('%')
                sys.stdout.flush()
                r_bound += r_inc

        r+=1
        while r%9 > 1:
            r += 1
        n = r ** 2

    print(" ")
    print("T(%d) = %d" % (n_max, total))

    for i in range(len(str(n_max))):
        if sizes[i] > 0:
            print("%d: %10d occurs, avg number of plans %.4f"%(i,sizes[i],float(n_plans[i])/sizes[i]))

if __name__ == "__main__":
    cProfile.run("main()")
