#!/usr/bin/env python

import sys
import expr


def enparen(expr,parex):
    answer = []
    for c in parex:
        if c in "()":
            answer.append(c)
        else:
            answer.append(expr[int(c)])
    return answer
            


def all_combos(l,n):
    if n == 0:
        return [[]]
    
    answer = []
    for c in l:
        l_new = [d for d in l if d != c]
        for nc in all_combos(l_new,n-1):
            answer.append([c]+nc)

    return answer

def all_ops_combos(l,n):
    if n == 0:
        return [[]]

    answer = []
    for c in l:
        for nc in all_ops_combos(l,n-1):
            answer.append([c]+nc)
    return answer

def all_ops(var_vec,ops):
    ops_combos = all_ops_combos(ops,len(var_vec)-1)
    
    answer = []
    for oc in ops_combos:
        curr_ex = []
        for i,op in enumerate(oc):
            curr_ex.append(var_vec[i])
            curr_ex.append(oc[i])
        curr_ex.append(var_vec[-1])
        answer.append(curr_ex)

    return answer


def good_set(s):

    for i in range(len(s)-1):
        if s[i] >= s[i+1]:
            return False

    return True

def gen_digit_sets():
    digits = [int(n) for n in list("123456789")]

    base = all_combos(digits,4)
    print(len(base))
    answer = []
    for s in base:
        if good_set(s):
            answer.append(s)

    return answer


def check_set(full_set,digit_map):
    can_do = {}
    
    for ex in full_set:
        n = expr.evaluate(ex,digit_map)
        can_do[n] = 1

    n = 1
    while n in can_do:
        n += 1
    return n - 1
        
    

def main():

    l = ['A','B','C','D']
    ops = "+-/*"
    parens = [
        "0123456",
        "(012)3456",
        "01(234)56",
        "0123(456)",
        "(012)3(456)",
        "(01234)56",
        "01(23456)",
        "((012)34)56",
        "(01(234))56",
        "01((234)56)",
        "01(23(456))"
    ]



    combos = all_combos(l,len(l))
    exprs = []
    for c in combos:
        exprs += all_ops(c,ops)

    full_set = []
    for ex in exprs:
        for parex in parens:
            px = enparen(ex,parex)
            full_set.append(px)
    print(len(full_set))
    sub_sets = gen_digit_sets()

    max_result = -1
    for s in sub_sets:
        digit_map = {}
        for c,n in zip(l,s):
            digit_map[c] = n

        result = check_set(full_set,digit_map)
        if result > max_result:
            max_result = result
            print("  ",s,"->",result)

        
    



if __name__ == "__main__":
    main()
