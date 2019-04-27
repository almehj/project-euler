#!/usr/bin/env python3

import sys


def next(n):
    answer = 0

    while n > 0:
        d = n%10
        answer += d*d
        n //=10

    return answer

def cycle(n):

    sys.stdout.write("%d "%n)    
    
    while n not in [1,89]:
        n = next(n)
        sys.stdout.write("%d "%n)
        sys.stdout.flush()
        
    print(" ")


dest = {
    1:1,
    89:89
}

def test_cycle(n):

    cycle = []
    while n not in dest:
        cycle.append(n)
        n = next(n)

    answer = dest[n]
    for i in cycle:
        dest[i] = answer

    return answer
    
    
    
    
def main():
    n_89s = 0
    max_n = int(sys.argv[1])
    for n in range(1,max_n):
        if n%10000 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()
            
        if test_cycle(n) == 89:
            n_89s += 1

    print("\n%d numbers less than %d go to 89"%(n_89s,max_n))

if __name__ == "__main__":
    main()
