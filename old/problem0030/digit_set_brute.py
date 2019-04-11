#!/usr/bin/env python3

import sys

import utils

class set_generator:

    def __init__(self,n):
        self.digits = [0]*n
        self.done = False
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.done:
            raise StopIteration

        answer = [i for i in self.digits if i != 0]

        self.digits[0] += 1

        for i in range(len(self.digits)-1):
            if self.digits[i]%10 == 0:
                self.digits[i] = 0
                self.digits[i+1] += 1
            else:
                break

        if self.digits[-1] >= 10:
            self.digits[-1] = 0
            self.done = True

        return answer
    
def compute_sets(n):
    s = set_generator(n)

    seen = []
    for l in s:
        l.sort()
        t = tuple(l)
        if t not in seen:
            seen.append(t)

    return seen
    

def main():
    max_size = int(sys.argv[1])

    seen = compute_sets(max_size)
    seen.sort()

    print("%d distinct sets:"%(len(seen)))
    for t in seen:
        print("  %s"%(utils.seq_string(t,separator=",")))

if __name__ == "__main__":
    main()
