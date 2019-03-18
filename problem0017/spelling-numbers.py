#!/usr/bin/env python3

import sys
import math



name_lens = {}
name_lens[0] = 0
name_lens[1] = len('one')
name_lens[2] = len('two')
name_lens[3] = len('three')
name_lens[4] = len('four')
name_lens[5] = len('five')
name_lens[6] = len('six')
name_lens[7] = len('seven')
name_lens[8] = len('eight')
name_lens[9] = len('nine')
name_lens[10] = len('ten')
name_lens[11] = len('eleven')
name_lens[12] = len('twelve')
name_lens[13] = len('thirteen')
name_lens[14] = len('fourteen')
name_lens[15] = len('fifteen')
name_lens[16] = len('sixteen')
name_lens[17] = len('seventeen')
name_lens[18] = len('eighteen')
name_lens[19] = len('nineteen')
name_lens[20] = len('twenty')
name_lens[30] = len('thirty')
name_lens[40] = len('forty')
name_lens[50] = len('fifty')
name_lens[60] = len('sixty')
name_lens[70] = len('seventy')
name_lens[80] = len('eighty')
name_lens[90] = len('ninety')
name_lens[100] = len('hundred')
name_lens[1000] = len('thousand')


def digits(n):
    answer = []
    while n > 0:
        answer.append(n%10)
        n = int(n/10)
    answer.reverse()
    return answer

def gen_name_len(n):
    if n < 1 or n >= 10000:
        return 0

    if n < 100 and n in name_lens:
        return name_lens[n]
    
    d_list = digits(n)
    d_list.reverse()
    answer = 0

    answer = name_lens[d_list[0]]
    if len(d_list) > 1 and d_list[1] > 0:
        answer += name_lens[d_list[1]*10]

    for e,d in enumerate(d_list[2:]):
        if d > 0:
            answer += name_lens[d] + name_lens[10**(e+2)]

    # The "and"
    if n > 99 and (d_list[0] + d_list[1]) > 0:
        answer += 3
        
    return answer


def compute_letter_total(n_max):
    total = 0
    for n in range(1,n_max+1):
        total += gen_name_len(n)
        print("  %5d: %d (%d)"%(n,gen_name_len(n),total))

    return total

def main():
#    for n in [int(s) for s in sys.argv[1:]]:
#        print("%7d: %d"%(n,gen_name_len(n)))

    for n in [int(s) for s in sys.argv[1:]]:
        print("Total of {1,...,%d} is %d"%(n,compute_letter_total(n)))

if __name__ == "__main__":
    main()
