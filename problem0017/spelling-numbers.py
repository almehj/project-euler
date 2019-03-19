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
    
    thousands = int(n/1000)
    hundreds = int((n%1000)/100)
    tens = int((n%100)/10)
    units = n%10

    assert(n == (1000*thousands + 100*hundreds + 10*tens + units))
    
    answer = 0
    if thousands > 0:
        answer += gen_name_len(thousands) + name_lens[1000]
    if hundreds > 0:
        answer += gen_name_len(hundreds) + name_lens[100]
    if tens == 1:        
        answer += gen_name_len(10+units)
    else:
        answer += gen_name_len(10*tens)+gen_name_len(units)
        
        
    # The "and"
    if n > 99 and (tens + units) > 0:
        answer += 3
        
    return answer


def compute_letter_total(n_max,n_min=1):
    total = 0
    for n in range(n_min,n_max+1):
        total += gen_name_len(n)
        print("  %5d: %d (%d)"%(n,gen_name_len(n),total))

    return total

def main():
#    for n in [int(s) for s in sys.argv[1:]]:
#        print("%7d: %d"%(n,gen_name_len(n)))

    n_max = int(sys.argv[1])
    n_min = 1
    if len(sys.argv[1:]) > 1:
        n_min = int(sys.argv[2])
    print("Total of {%d,...,%d} is %d"%(n_min,n_max,compute_letter_total(n_max,n_min)))

if __name__ == "__main__":
    main()
