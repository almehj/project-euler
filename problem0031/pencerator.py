#!/usr/bin/env python3

import sys

pences=[1,2,5,10,20,50,100,200]


def compute_combos(goal,possibles):

    comps = possibles[:]
    comps.sort()
    min_val = min(comps)
    
    combos = {}
    combos[min_val] = 1

    total = min_val + 1
    while total <= goal:
        
        total += goal

def main():
    goal = int(sys.argv[1])

    possibles = [x for x in pences if x<=goal]

    print("%d ways to make %d pence"%(compute_combos(goal,possibles),goal))


    
if __name__ == "__main__":
    main()
