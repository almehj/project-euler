#!/usr/bin/env python3

import sys
import collatz

prev_seqs = {}

def next_term(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return int(3*n+1)

def collatz_seq_len(start):

    n = start
    answer = 1
    
    while n != 1:
        if n in prev_seqs:
            answer = answer + prev_seqs[n]
            break
        else:
            n = next_term(n)
            answer += 1

    prev_seqs[start] = answer
    return answer

def main():
    max_data = (0,0)
    for n in range(1,int(sys.argv[1])+1):
        l = collatz_seq_len(n)
        if l > max_data[0]:
            max_data = (l,n)
        
    print("Longest was %d elements for n = %d"%max_data)
    print(collatz.collatz_seq(max_data[1]))

if __name__ == "__main__":
    main()
