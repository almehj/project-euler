#!/usr/bin/env python3

import sys

def next_xy(x,y):
    x_new = 3*x + 2*y -2
    y_new = 4*x + 3*y -3

    return x_new,y_new


def main():

    max_y = int(sys.argv[1])
    min_y = int(sys.argv[2])
    
    x = y = 1

    while y < max_y:
        if y > min_y:
            print(x,y)
        x,y = next_xy(x,y)
        
if __name__ == "__main__":
    main()
