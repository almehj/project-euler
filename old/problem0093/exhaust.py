#!/usr/bin/env python

import sys
import expr

def all_combos(l,n):
    if n == 0:
        return [[]]
    
    answer = []
    for c in l:
        l_new = [d for d in l if d != c]
        for nc in all_combos(l_new,n-1):
            answer.append([c]+nc)

    return answer

def all_ops(var_vec,ops):
    ops_combos = all_combos(ops,len(var_vec)-1)

    answer = []
    for oc in ops_combos:
        curr_ex = []
        for i,op in enumerate(oc):
            curr_ex.append(var_vec[i])
            curr_ex.append(oc[i])
        curr_ex.append(var_vec[-1])
        answer.append(curr_ex)

    return answer

                            
def gen_neg_key(s,l):
    return ''.join([":"] + [x for x in l if x not in s])

def gen_pos_key(s,l):
    return ''.join([":"] + [x for x in l if x in s])

def join_keys(k1,k2):

    answer = list(k1[1:])
    for c in k2[1:]:
        if c not in answer:
            answer.append(c)
    answer.sort()
    return ''.join([":"]+answer)

def main():

    l = ['A','B','C','D']
    ops = "+-/*"

    digits = {}
    for name,val in zip(l,sys.argv[1]):
        digits[name] = int(val)
    
    combos = []
    for n in range(1,len(l)+1):
        combos += all_combos(l,n)

    subexprs = []
    for combo in combos:
        subexprs += all_ops(combo,ops)

    foo = {}
    for s1 in subexprs:
        key = gen_neg_key(s1,l)
        if key in foo:
            continue
        rest = []
        for s2 in subexprs:
            good = True
            for c in key:
                if c in s2:
                    good = False
                    break
            if good:
                rest.append(s2)
        foo[key] = rest

    full_key = ''.join([":"] + l)
    foo[full_key] = []

    full_expr = [[s] for s in subexprs]
    done = False
    while not done:
        new_full_expr = []
        done = True
        for ex in full_expr:
            print("Thinking about",ex)
            k = gen_pos_key(ex[0],l)
            for s in ex[1:]:
                k = join_keys(k,gen_pos_key(s,l))
            print("  key=",k)
            print("    foo[k]=",foo[k])
            if k == full_key:
                new_full_expr.append(ex)
            else:
                done = False
                for s in foo[k]:
                    new_full_expr.append(ex + [s])
        full_expr = new_full_expr

            
        
        
    



if __name__ == "__main__":
    main()
