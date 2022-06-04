#!/usr/bin/env python

import sys

factorial = [1]
for i in range(1,10):
    factorial.append(i*factorial[i-1])

def value(n):
    if n == 0: return 1

    sum_fact = 0
    while n > 0:
        d = n%10
        sum_fact += factorial[d]
        n //= 10

    return sum_fact


def get_chain(n):
    chain = [n]
    while True:
        n = value(n)
        if n in chain:
            chain.append(n)
            break
        chain.append(n)

    return chain

magic_number = 60
chain_lens = {}


def analyze_lengths(chain,n):

#    print("consider",chain,"repeater",n)
    ndx = chain.index(n)
    lead = chain[:ndx]
    loop = chain[ndx:]
#    print("lead",lead)
#    print("loop",loop)

    for k in loop:
        chain_lens[k] = len(loop)
    lead.reverse()
    offset = len(loop) + 1
    for k in lead:
        chain_lens[k] = offset
        offset += 1
    

def chainify(n):

    chain = [n]
    while True:
        n = value(n)
        if n in chain_lens:
            term_val = chain_lens[n]
            chain.reverse()
            for k in chain:
                term_val += 1
                chain_lens[k] = term_val
            break
        elif n in chain:
            analyze_lengths(chain,n)
            break
        else:
            chain.append(n)
    
n = 1
max_len = -1
num_60 = 0
while n < int(sys.argv[1]):
    if n not in chain_lens:
        #        print("chainfying",n)
        chainify(n)
        #        print(chain_lens)
    if chain_lens[n] > max_len:
        max_len = chain_lens[n]
        print("new max_len",max_len," for n =",n)
    if chain_lens[n] == 60:
        num_60 += 1
        print(n,"is 60",num_60,"total")
        
    n += 1

