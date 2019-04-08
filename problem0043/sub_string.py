#!/usr/bin/env python

import sys

from utils import seq_string

def possible_segment(s):
    for i,c in enumerate(s[:-1]):
        if c in s[i+1:]:
            return False
    return True

def build_compat_table(segs):

    answer = {}
    
    for f in segs:
        answer[f] = {}
        for s in segs[f]:
            k = s[1:]
            v = s[0]
            if k not in answer[f]:
                answer[f][k] = []
            answer[f][k].append((v,s))

    return answer

def compute_possibles():
    answer = {}
    for f in [2,3,5,7,11,13,17]:
        answer[f] = []
        n = f
        while n < 1000:
            s = "%03d"%n
            if possible_segment(s):
                answer[f].append(s)
            n += f

    return answer



def main():

    segs = compute_possibles()
    compat_table = build_compat_table(segs)

    poss_keys = []
    for s in segs[17]:
        k = s[:2]
        if k not in poss_keys:
            poss_keys.append((s,k))
    print("%d possible keys..."%(len(poss_keys)))
    useful_keys = []
    for s,k in poss_keys:
        if k in compat_table[13]:
            print("  %s has: %s"%(k,seq_string(compat_table[13][k])))
            useful_keys.append((s,k))
    print("%d useful keys"%(len(useful_keys)))
                  
    for s,k in useful_keys:
        print(s,k)
    
if __name__ == "__main__":
    main()
