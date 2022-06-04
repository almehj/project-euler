#!/usr/bin/env python

import prime_numbers

def sum_propers(n):
    facts = prime_numbers.factorization(n)
    divs = prime_numbers.gen_divisor_list(facts)

    return sum(divs) - n

    
def chain_str(l):
    return " -> ".join([str(x) for x in l])

max_val = int(1.e6)
max_n = 6000

TERM_VAL = 0

next_term = {}

start_n = 5800
big_n = -1

while start_n < max_n:
    n = start_n
    while n in next_term:
        n += 1
        start_n = n

    seen = []
    done = False
#    print("Starting with",n)
    while not done:
        seen.append(n)
        n = next_term.get(n,sum_propers(n))
        #print("  New Value",n)
        
        if n == 1 or n > max_val or n == TERM_VAL:
            # Termination
            for s in seen:
                next_term[s] = TERM_VAL
            done = True
#            print("termination",start_n)
        elif n < 0:
            for s in seen:
                next_term[s] = n
            done = True
#            print("cycle crash",start_n)
        elif n in seen:
            # Cycle
                                   
            n_ndx = seen.index(n)
            cycle_len = len(seen) - n_ndx
            for s in seen[:n_ndx]:
                next_term[s] = n
            for s in seen[n_ndx:]:
                next_term[s] = -cycle_len
            done = True    
            print("new cycle length",cycle_len,"from",start_n,":",chain_str(seen[n_ndx:]+[sum_propers(seen[-1])]))
            
        if n > big_n: big_n = n


for n in next_term:
    if next_term[n] < 0:
        print("%d is part of %d-way cycle"%(n,-next_term[n]))

    
