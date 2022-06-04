#!/usr/bin/env python


import sys
from functools import reduce

def permute(l,n):

    if n == 0:
        return [[]]
    
    answer = []
    for c in l:
        sub_l = l[:]
        sub_l.remove(c)
        front = [c]
        for new_l in permute(sub_l,n-1):
            answer.append(front + new_l)
    return answer

def main():

    l = [n for n in range(1,10)]
    found = []
    for pl in permute(l,5):
        for fl in [1,2]:
            two = int("".join([str(n) for n in pl[:fl]]))
            three = int("".join([str(n) for n in pl[fl:]]))
            prod = two*three
            new_l = pl + [int(i) for i in list(str(prod))]
            if len(new_l) == len(l):
                good = True
                for i in l:
                    if i not in new_l:
                        good = False
                        break
                if good:
                    print("%d * %d = %d"%(two,three,prod))
                    if prod not in found:
                        found.append(prod)

    total = reduce(lambda x,y: x+y, found)
    print(found)
    print(total)
    
if __name__ == "__main__":
    main()
