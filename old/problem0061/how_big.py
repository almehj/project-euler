#!/usr/bin/env python


def n3gon(n):
    return n*(n + 1)//2

def n4gon(n):
    return n*n

def n5gon(n):
    return n*(3*n - 1)//2

def n6gon(n):
    return n*(2*n - 1)

def n7gon(n):
    return n*(5*n - 3)//2

def n8gon(n):
    return n*(3*n - 2)


def gon_num(n,g):
    if g == 3:
        return n3gon(n)
    if g == 4:
        return n4gon(n)
    if g == 5:
        return n5gon(n)
    if g == 6:
        return n6gon(n)
    if g == 7:
        return n7gon(n)
    if g == 8:
        return n8gon(n)

    return 0


def count_digits(g,n_digits):
    total = []
    n = 1
    gn = 1
    while len(str(gn)) <= n_digits:
        if len(str(gn)) == n_digits:
            total.append(gn)
        n += 1
        gn = gon_num(n,g)

    return total

# Assumes 4 digits
def gen_reln(l):
    answer = []
    for n in l:
        front = str(n//100)
        back = "%02d"%(n%100)
        answer.append((front,back))
    return answer

def gen_reln_dict(l):
    answer = {}
    for f,b in l:
        if f not in answer:
            answer[f] = []
        answer[f].append(b)
    return answer

npaths = 1
numbers = {}
for g in range(3,9):
    l = count_digits(g,4)
    npaths *= len(l)
    print(g,len(l))
    numbers[g] = l

print(npaths,"paths")

reln_dicts = {}
for g in range(3,9):
    l = gen_reln(numbers[g])
    reln_dicts(g) = gen_reln_dict(l)
    
l = [n for n in range(3,9)]

mappings = {}
for g1 in l:
    mappings[g1] = {}
    reln1 = reln_dicts[g1]
    for g2 in l:
        reln2 = reln_dicts[g2]
        mappings[g1][g2] = []
        for f in reln1:
            fl = reln1[f]
            
        



        
