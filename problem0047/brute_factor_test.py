#!/usr/bin/env python3

import sys

import prime_numbers

def main():
    goal_factors = int(sys.argv[1])
    max_val = int(sys.argv[2])

    in_seq = False
    seq_len = 0
    for n in range(2,max_val+1):
        n_fact = len(prime_numbers.factorization(n))
        if n_fact == goal_factors:
            in_seq = True
            seq_len += 1
            if seq_len == goal_factors:
                print("Found %d consecutive with %d factors:"%
                      (goal_factors,goal_factors))
                for i in range(n-goal_factors+1,n+1):
                    print("  %d: %s"%(i,str(prime_numbers.factorization(i))))
                sys.exit(0)
        else:
            in_seq = False
            seq_len = 0
                    


            
if __name__ == "__main__":
    main()
