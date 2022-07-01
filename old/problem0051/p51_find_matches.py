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
                k = find_matches(str(n),str(m))
                if len(k) > 0:
                    if k not in matches:
                        matches[k] = {}
                    matches[k][n] = 1
                    matches[k][m] = 1

for k in matches:
    lk = sum([len(tk[1:]) for tk in k]) 
    if lk > 1 or l_max < 3:

        l = [n for n in matches[k]]
        cl = clean_list(l,k,l_max)

        after = "  "
        if len(l) > len(cl):
            after = "SHORTER!"
            if len(cl) > 0:
                after = "INTERESTING! %d"%len(cl)
        print(k,":",l,cl,after)

            
