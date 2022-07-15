#!/usr/bin/env python

import sys


def next_b(b):
    return int(b) * (b - int(b) + 1)


def next_in_seq(b):
    digits = []

    while len(digits) < 100:
        a = int(b)
        digits += list(str(a))
        b = next_b(b)

    digits = [int(d) for d in digits]
    answer = 0
    base = 1.e0
    for d in digits:
        answer += d*base
        base /= 10

    return answer


def multiply_rep(rep, k):
    # multiply digits
    answer = [k*d for d in rep]
    # get to single digits (except maybe first)
    for i in range(len(answer)-1):
        d = answer[i]%10
        answer[i+1] += answer[i]//10
        answer[i] = d
    return answer


def next_b_rep(b):
    k = b[-1]
    b[-1] = 1
    return multiply_rep(b,k)


def next_rep(b):
    answer = []

    while len(answer) < len(b):
        answer += [int(d) for d in list(str(b[-1]))]
        b = next_b_rep(b)

    answer = [d for d in reversed(answer)]
    return answer


def print_rep(b):
    digits = ["%d."%(b[-1])] + [str(d) for d in reversed(b[:-1])]
    print(''.join(digits))


def main():
    b = [2] + [0]*200
    b = [d for d in reversed(b)]

    for i in range(30):
        print_rep(b)
        b = next_rep(b)

    print_rep(b)
    for i,d in enumerate(reversed(b)):
        sys.stdout.write("%d"%d)
        if i == 0:
            sys.stdout.write('.')
        if i > 23:
            break

    print(" ")


if __name__ == "__main__":
    main()
