#!/usr/bin/env python3

import sys

class heap(object):

    def __init__(self):        
        self.clear()

    def clear(self):
        self.max_depth = 0
        self.n_items = 0
        self.data = [0]

    def add_level(self):
        self.max_depth += 1
        self.data += [0]*(2**self.max_depth)
        
def main():
    pass

if __name__ == "__main__":
    main()
