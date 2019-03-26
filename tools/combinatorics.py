#!/usr/bin/env python3

import sys


class combinator:

    def __init__(self,l,n):
        self.l = l
        self.n_elem = len(l)
        self.n = n
        self.ndx = [i for i in range(n)]
        self.done = False
        
    def __iter__(self):
        return self

    def __next__(self):
        # If we get to the end, quit
        if self.done:
            raise StopIteration

        # Store answer we will return
        c = [self.l[i] for i in self.ndx]

        # Advance indices
        i = self.n - 1
        if self.ndx[i] < len(self.l) - 1:
            self.ndx[i] += 1
        else:
            while self.ndx[i] == self.n_elem - self.n + i:
                i -= 1
            if i < 0:
                self.done = True
            else:
                self.ndx[i] += 1
                for j,k in enumerate(range(i,self.n)):
                    self.ndx[k] = self.ndx[i] + j 
        
        return c

def main():
    items = [i+1 for i in range(int(sys.argv[1]))]
    n = int(sys.argv[2])

    comb = combinator(items,n)
    for c in comb:
        print("{ %s }"%(" ".join([str(i) for i in c])))
        
if __name__ == "__main__":
    main()
