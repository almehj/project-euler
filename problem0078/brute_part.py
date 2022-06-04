#!/usr/bin/env python

import sys

def gen_combos(n,m):
    
    if m == 1:
        return [[n]]

    answer = []
    for i in range(1,n-m+2):
        for sub in gen_combos(n-i,m-1):
            answer.append([i]+sub[:])
            
    return answer    


existing_facts = [1]
def factorial(n):
    if n > len(existing_facts) - 1:
        i = len(existing_facts)
        while i <= n:
            existing_facts.append(i*existing_facts[i-1])
            i += 1

    return existing_facts[n]
        

def choose(n,r):

    if r > n: return 1

    answer = factorial(n)/factorial(n-r)
    return answer/factorial(r)

n = int(sys.argv[1])

total = 0
for m in range(1,n+1):
    if m <= n:
        combos = gen_combos(n,m)
        tups = {}        
        for combo in combos:
            combo.sort()

        for combo in combos:
            k = tuple(combo)
            if k not in tups:
                tups[k] = 0
            tups[k] += 1
        total += len(tups)
        print("%3d %5d %5d %5d"%(m,len(combos),len(tups),choose(n-1,m-1)))
print("\nTotal is %d"%total)
