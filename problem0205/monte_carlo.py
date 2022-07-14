#!/usr/bin/env python

import sys
import random


def main():
    n_samps = int(sys.argv[1])

    n_pete = 0
    for i in range(n_samps):
        peter = sum([random.randint(1,4) for j in range(9)])
        colin = sum([random.randint(1,6) for j in range(6)])
        if peter > colin:
            n_pete += 1

        if n_samps < 1000 or i%1000 == 0:
            print(n_pete/(i+1))

    print("# final:",n_pete/n_samps)

        
        
if __name__ == "__main__":
    main()
