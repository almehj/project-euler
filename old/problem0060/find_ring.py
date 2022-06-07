#!/usr/bin/env python

import sys

def read_reln2follow(infile):
    answer = {}
    for line in infile:
        a,b = [s.strip() for s in line.split()]
        if a not in answer:
            answer[a] = []
        answer[a].append(b)

    return answer

def commons(l1,l2):
    answer = []
    for n in l1:
        if n in l2:
            answer.append(n)
            
    return answer

def find_groups_from(a,follows):
    group = [a]
    fa = follows[a]
    for b in fa:
        if b in follows:
            fb = follows[b]
            lc = commons(fa,fb)
            for c in lc:
                if c in follows:
                    fc = follows[c]
                    ld = commons(lc,fc)
                    for d in ld:
                        print(a,b,c,d) 
                        if d in follows:
                            fd = follows[d]
                            le = commons(ld,fd)
                            for e in le:
                                print(a,b,c,d,e,":",sum([int(n) for n in [a,b,c,d,e]]))
        


def find_groups(infile_name):
    with open(infile_name) as infile:
        follows = read_reln2follow(infile)

#        for n in follows:
#            print(n,":",follows[n])

        for a in follows:
            find_groups_from(a,follows)


def main():
    for infile_name in sys.argv[1:]:
        find_groups(infile_name)


if __name__ == "__main__":
    main()
