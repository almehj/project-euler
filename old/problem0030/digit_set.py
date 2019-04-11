#!/usr/bin/env python3

import sys

import utils

class set_generator:

    def __init__(self,set_size,**kwargs):
        self.items = kwargs.get('items',[i for i in range(10)])[:]
        self.n_items = len(self.items)        

        self.ndxs = [0]*set_size
        self.n_ndxs = set_size

        self.done = False
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.done:
            raise StopIteration

        answer = [self.items[i] for i in self.ndxs]

        # Try to advance to next set (or declare victory)
        i = 0
        while i < self.n_ndxs and self.ndxs[i] == self.n_items - 1:
            i += 1
        if i < self.n_ndxs:
            self.ndxs[i] += 1
            for j in range(i,-1,-1):
                self.ndxs[j] = self.ndxs[i]
        else:
            self.done = True
            
        return reversed(answer)

        
def main():

    max_len = int(sys.argv[1])
    max_value = int(sys.argv[2])

    items = [i for i in range(0,max_value + 1)]
    s = set_generator(max_len,items=items)

    n = 0
    for t in s:
        n += 1
        combo = [i for i in t if i != 0]
        print(utils.seq_string(combo))

    print("\n%d combos"%(n))

if __name__ == "__main__":
    main()
