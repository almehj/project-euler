#!/usr/bin/env python3

import sys
from string import ascii_uppercase as alphabet


def get_names(infile):
    names = []
    for line in infile:
        bits = [s.strip()[1:-1] for s in line.split(',')]
        names += bits

    return names

def name_score(name):
    score = 0
    for c in name:
        if c in alphabet:
            score += alphabet.index(c) + 1

    return score

    
def main():
    with open(sys.argv[1],'r') as infile:
        names = get_names(infile)
        names.sort()
        total = 0
        for i,name in enumerate(names):
            score = name_score(name)
            total += (i+1)*score
            print(i+1,name,score,(i+1)*score,total)
        print(total)

if __name__ == "__main__":
    main()
