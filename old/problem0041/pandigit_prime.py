#!/usr/bin/env python

import sys
import prime_numbers

def is_pandigital(n):
    str_n = str(n)
    
    for d in range(1,len(str_n)+1):
        if str_n.count(str(d)) != 1:
            return False

        return True


def perms(l):
    if len(l) < 1:
        return [l]
    
    answer = []
    for d in l:
        front = [d]
        new_l = l[:]
        new_l.remove(d)
        for l2 in perms(new_l):
            answer.append(front + l2)

    return answer
    
def main():
    for a in perms([str(i) for i in range(7,0,-1)]):
        ld = int(a[-1])
        if ld%2 != 0 and ld != 5:
            n = int("".join(a))
            print("checking",n)
            if prime_numbers.is_prime(n):
                print("  ",n)
                
        

if __name__ == "__main__":
    main()
