#!/usr/bin/env python3

import sys
import getopt
from functools import reduce

def read_grid(infile):
    answer = []

    for line in infile:
        line = line.strip()
        if line == "": continue
        answer.append([int(x) for x in line.split()])

    return answer

def row_str(row):
    return ' '.join(["%02d"%n for n in row])
    
def print_grid(grid):
    for row in grid:
        print("   %s"%(row_str(row)))


def extract_diagional(grid,start,increment):

    answer = []

    if len(grid) > 0:
        di,dj = increment

        if abs(di) + abs(dj) != 0:
            n_row = len(grid)
            n_col = len(grid[0])

            i,j = start
            while (i >= 0 and i < n_row) and (j >=0 and j < n_col):
                answer.append(grid[i][j])
                i += di
                j += dj
    
    return answer

def max_product(row,n):

    start_i = 0
    max_prod = -1
    
    if len(row) >= n:
        for i in range(start_i,len(row)-n+1):
            p = reduce(lambda x, y: x*y, row[i:i+n])
            if p > max_prod:
                max_prod = p
                start_i = i
                
    return max_prod,start_i

def row_report(row,prod,start_i,n):
    print(" Max %10d @ %2d [%s]: %s"%(prod,start_i,row_str(row[start_i:start_i+n]),row_str(row)))
    
def main():

    optlist,args = getopt.getopt(sys.argv[1:],'n:')
    n = 4 # The length from the problem spec is the default

    for opt,val in optlist:
        if opt in ['-n']:
            n = int(val)

    print("Searching for products of length %d"%(n))
    for infile_name in args:
        print(" Examining %s"%(infile_name))
        with open(infile_name) as infile:              
            grid = read_grid(infile)
            print(" Grid:\n")
            print_grid(grid)
            print("\nExamining...")

            to_do = True
            n_rows = len(grid)
            n_cols = 0
            if n_rows == 0 or len(grid[0]) == 0:
                print("Empty Grid! No answer")
                to_do = False
            else:
                n_cols = len(grid[0])
                if n_rows < n and n_cols < n:
                    print("Grid too small! No answer")
                    to_do = False
            

            if to_do:
                max_prod = -1
                for dj in [-1,0,1]:
                    for start_col in range(len(grid[0])):
                        start_rows = [0]
                        dis = [1]
                        if (start_col == 0 and dj in [0,1]) or \
                           (start_col == n_cols - 1 and dj == -1):
                            start_rows = range(n_rows)
                        if start_col == 0 and dj == 1:
                            dis = [0,1]
                        for start_row in start_rows:
                            for di in dis:
                                row = extract_diagional(grid,(start_row,start_col),(di,dj))
                                if len(row) < n:
                                    continue
                                p,i = max_product(row,n)
                                row_report(row,p,i,n)                        

                                if p > max_prod:
                                    max_prod = p

                print("\n\nMax Product is %d"%(max_prod))
                
                    


            
if __name__ == "__main__":
    main()
