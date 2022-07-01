#!/usr/bin/env python

import sys

l_max = int(sys.argv[1])
infile_name = "primes_len%02d.txt"%l_max



def get_checkers(k,l):

    answer = [n for n in range(l)]
    for t in k:
        for p in t[1:]:
            answer.remove(p)
    return tuple(answer)
        
def clean_list(l,k,ml):
    ck = get_checkers(k,ml)

    if len(ck) < 2:
        return [n for n in l]

    answer = []
    for n in l:
        n = str(n)
        gc = n[ck[0]]
        good = True
        for p in ck[1:]:
            if n[p] != gc:
                good = False
                break
        if good:
            answer.append(int(n))

    return answer
    

    
def find_matches(n,m):
    if len(n) != len(m):
        return ()

    matches = []

    for i,c in enumerate(n):
        if m[i] == c:
            matches.append((i,int(c)))

    answer = []
    for d in range(10):
        dm = [t for t in matches if t[1] == d]
        if len(dm) > 0:
            lm = [d] + [t[0] for t in dm]
            answer.append(tuple(lm))
    return tuple(answer)

matches = {}
with open(infile_name) as infile:
    
    nums = [int(line.strip()) for line in infile]

    ln = len(nums)
    sys.stderr.write("%d numbers to look at\n"%ln)
    sys.stderr.write("%d combos\n"%(((ln-1)*ln)//2))

    n_seen = 0
    n_found = 0
    for i,n in enumerate(nums):
        for m in nums[i+1:]:

            n_seen += 1
            if n_seen%500000 == 0:
                sys.stderr.write('.')
                sys.stderr.flush()
                    
            diff = str(m-n)
            nd = 0
            for d in "123456789":
                if diff.count(d) > 0:
                    nd += 1
                if nd > 1:
                    break
            if nd == 1:
                print(n,m)

            
