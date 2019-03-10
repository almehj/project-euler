#!/usr/bin/env python3

import sys

prev_seqs = {}

def next_term(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return int(3*n+1)

def collatz_seq(start):

    answer = [start]
    n = start

    while n != 1:
        if n in prev_seqs:
            answer = answer[:-1] + prev_seqs[n]
            break
        else:
            n = next_term(n)
            answer.append(n)

    prev_seqs[start] = answer
    return answer

max_data = (0,0)
for n in range(1,int(sys.argv[1])+1):
    seq = collatz_seq(n)
    if len(seq) > max_data[0]:
        max_data = (len(seq),n)
print("Longest was %d elements for n = %d"%max_data)
print(collatz_seq(max_data[1]))
