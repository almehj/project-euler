#!/usr/bin/env python

from itertools import product
from combinatorics import combinator


C = combinator([0,1,2,3,4,5,6,7,8,9],6)
confs = [tuple(c) for c in C]

squares = ["%02d"%(n**2) for n in range(1,10)]
digit_pairs = [(int(c[0]),int(c[1])) for c in squares]

def check(c1,c2):

    testc1 = c1
    testc2 = c2

    if 9 in c1 or 6 in c1:
        testc1 = testc1 + (6,9)
    if 9 in c2 or 6 in c2:
        testc2 = testc2 + (6,9)

    
    for i,j in digit_pairs:
        if not((i in testc1 and j in testc2) or (j in testc1 and i in testc2)):
            return False
        
    return True

def main():
    solns = []
    n = 0
    for i,j in product(range(len(confs)),range(len(confs))):
        if i >= j:
            continue
        n+=1
        if check(confs[i],confs[j]):
            l = [confs[i],confs[j]]
            l.sort()
            t = tuple(l)
            if t not in solns:
                solns += [t]

    n_solns = len(solns)

    print("%d considered"%(n))
    print("%d solutions"%(n_solns))
    #for c1,c2 in solns:
    #    print("%s and %s"%(''.join([str(c) for c in c1]),
    #                       ''.join([str(c) for c in c2])))
if __name__ == "__main__":
    main()
