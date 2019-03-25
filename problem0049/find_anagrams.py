#!/usr/bin/env python3

import sys

def print_interleaved(s):
    s.sort()
    l = []
    for i,n in enumerate(s):
        l.append(str(s[i]))
        if i < (len(s)-1):
            l.append("<+ "+str(s[i+1]-s[i])+" >")

    print(" ".join(l))


magic=3330
def check(s):
    if 1487 in s:
        print("trying the one: %s"%(" ".join([str(i) for i in s])))
    
    for n in s:
        l = [n]
        q = n + magic
        while q in s:
            l += [q]
            q += magic
        if len(l) >= 3:
            print("Found: (sum %d) %s"%(sum(l)," ".join([str(i) for i in l])))
            
def main():
    infile = open(sys.argv[1],'r')

    sigs = {}
    for line in infile:
        line = line.strip()
        if len(line) == 4:
            l = list(line)
            l.sort()
            k = tuple(l)
            sigs[k] = sigs.get(k,[]) + [int(line)]

    for k in sigs:
        if len(sigs[k]) >= 3:
            check(sigs[k])


if __name__ == "__main__":
    main()
        
        
