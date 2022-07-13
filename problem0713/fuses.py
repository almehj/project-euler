#!/usr/bin/env python


import sys
import random
import itertools


def main():

    n_fuses = int(sys.argv[1])
    n_good = int(sys.argv[2])

    fuses = [i for i in range(n_fuses)]

    max_tries = 0
    for goods in itertools.combinations(fuses,n_good):
        curr_tries = 0
        i = 0
        while i < n_fuses:
            curr_tries += 1
            if i in goods and (i+1) in goods:
                if curr_tries > max_tries:
                    max_tries = curr_tries
                    break
            i += 2
    print(max_tries)


if __name__ == "__main__":
    main()
