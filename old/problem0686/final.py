#!/usr/bin/env python

import sys

def seq(n):
    answer = [485]
    n -= 1
    while n > 0:
        n -= 2
        answer.append(196)
        answer.append(289)

    answer[-1] = 485

    n = 0
    for i,v in enumerate(answer):
       if v == 289:
           n += 1
           if n%4 == 0:
               answer[i] = 485
                    
    return answer

seqs = {}
seqs['A'] = seq(25)
seqs['B'] = seq(7)
seqs['C'] = seq(33)


def expand_seq(l):
    answer = ['A']
    for n in l:
        answer += ['B']*n
        answer += ['C']
    answer = answer[:-1]

    return answer 

def full_seq(l):
    answer = []
    for d in l:
        answer += seqs[d][:]
    return answer

first_seq = expand_seq([3,2,3])
second_seq = expand_seq([3,2,3,2,2,3,2,3,2,2,3,2,3,2,2,3,2,3,2,2,3,2,3])

first_seq = full_seq(first_seq)
second_seq = full_seq(second_seq)

sum_first = sum(first_seq)
partial_sum_first = [sum(first_seq[:i]) for i in range(len(first_seq))]

sum_second = sum(second_seq)
partial_sum_second = [sum(second_seq[:i]) for i in range(len(second_seq))]

start_p = 1060
start_n = 5

def p_func(top_n):
    if top_n < 5:
        return None

    p = start_p
    top_n -= start_n

    
    # first seq
    if top_n < len(first_seq):
        print("within first seq")
        p += partial_sum_first[top_n]
        return p

    top_n -= len(first_seq)
    p += sum_first

    # second seq
    print("within second seq")
    n_all = top_n // len(second_seq)
    partial_ndx = top_n%len(second_seq)

    print(" n_all =",n_all," partial_ndx =",partial_ndx)
    
    p += n_all*sum_second
    p += partial_sum_second[partial_ndx] 
    
    return p
    

def main():

    print(5 + len(first_seq))
    print(5 + len(first_seq) + len(second_seq))
    print(5 + len(first_seq) + 2*len(second_seq))
    
    
    for n in [int(s) for s in sys.argv[1:]]:
        print("p(123,%d) = %d"%(n,p_func(n)))
        
              
if __name__ == "__main__":
    main()
