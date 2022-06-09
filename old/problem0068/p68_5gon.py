#!/usr/bin/env python

import sys

n_max = int(sys.argv[1])

tot_l = []

r = [n for n in range(1,2*n_max+1)]

for i in r:
    old_l = [[i]]
    while len(old_l[0]) < n_max:
        new_l = []
        for l in old_l:
            for i in [n for n in r if n not in l]:
                new_l.append(l + [i])
        old_l = new_l
    tot_l += old_l

    
        
def dual(l):
    answer = []
    for i in range(len(l)):
        j = (i + 1)%len(l)
        answer.append(l[i]+l[j])

    return answer

def check(d,l):

    not_l = [n for n in r if n not in l]

    not_l.reverse()

    add_l = [d[i]+not_l[i] for i in range(len(l))]
    base = add_l[0]
    for n in add_l:
        if n != base:
            return False,-1

    return True,base


def rotation_check(l1,l2):
    if len(l1) != len(l2):
        return False

    v = l1[0]
    if v not in l2:
        return False
    iv = l2.index(v)
    for i in range(len(l1)):
        j = (i+iv)%len(l1)
        if l1[i] != l2[j]:
            return False

    return True

def gons(l,total):
    answer = []
    sum_max = 0
    i_max = 0
    for i in range(0,len(l)):
        j = (i+1)%len(l)
        s = l[i]+l[j]
        if s > sum_max:
            sum_max = s
            i_max = i

    for i in range(len(l)):
        ip = (i+i_max)%len(l)
        jp = (ip+1)%len(l)
        s = l[ip]+l[jp]
        n = total-s
        
        answer.append((n,l[ip],l[jp]))

    return answer

seen = []

for l in tot_l:
    d = dual(l)
    sd= d[:]
    sd.sort()
    good,total = check(sd,l)
    if good:
#        print("seen:",seen)
        g = gons(l,total)

        full_s = []
        for t in g:
            for n in t:
                full_s.append(str(n))
        full_s = "".join(full_s)
        
        sg = "%2d"%total + ": "+ ";".join([str(t) for t in g]) + " " + full_s + " " + str(len(full_s))
        if sg not in seen:
            seen.append(sg)

for s in seen:
    print(s)
        
    
