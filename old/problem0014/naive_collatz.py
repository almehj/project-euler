#!/usr/bin/env python3

import sys

def collatz_seq(start):

    answer = [start]
    n = start
    while n != 1:
        if n%2 == 0:
            n = int(n/2)
        else:
            n = int(3*n+1)
        answer.append(n)

    return answer



for n in [int(x) for x in sys.argv[1:]]:
    print(n,":",collatz_seq(n))
