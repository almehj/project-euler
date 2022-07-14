#!/usr/bin/env python
import getopt
import sys
from riffle_chains import next_index


def test_chain(n_cards, n_max):
    i = next_index(1, n_cards)
    n = 1
    while i != 1:
        i = next_index(i, n_cards)
        n += 1
        if n > n_max:
            return False

    return n == n_max


def main():
    optlist, args = getopt.getopt(sys.argv[1:], "n:g:")
    n_max = 2
    goal_shuffles = 1

    for opt, val in optlist:
        if opt in ["-n"]:
            n_max = int(val)
        elif opt in ["-g"]:
            goal_shuffles = int(val)

    if n_max > 2**goal_shuffles:
        print(n_max, "too high, max for",goal_shuffles,"is",2**goal_shuffles)
        n_max = 2**goal_shuffles

    n = 2
    n_goals = 0
    total = 0
    last_success = 0
    while n <= n_max:
        if test_chain(n, goal_shuffles):
            n_goals += 1
            total += n
            print(n_goals, n, n-last_success, total)
            last_success = n
            sys.stdout.flush()
        n += 2


if __name__ == "__main__":
    main()
