#!/usr/bin/env python3

import sys

def read_grid(grid_file):
    grid = []
    for line in grid_file:
        if line.strip() != "":
            grid.append([int(s) for s in line.split(',')])

    return grid

def print_grid(grid):
    width=len("%d"%(max([max(row) for row in grid])))
    fmt_str="%%%dd"%(width)
    for row in grid:
        print("%s"%(" ".join([fmt_str%i for i in row])))

def find_min_path_total(grid):

    n_rows = len(grid)
    n_cols = len(grid[0])
    n_elements = n_rows*n_cols
    
    path_vals = [[0]*n_cols for i in range(n_rows)]
    path_vals[0][0] = grid[0][0]

    i_sum = 1
    paths = {}
    for i_sum in range(1,n_rows+n_cols+1):
        for i in range(i_sum+1):
            j = i_sum - i
            if i in range(n_rows) and j in range(n_cols):
                potentials = []
                if i > 0:
                    potentials.append(tuple([path_vals[i-1][j],(-1,0)]))
                if j > 0:
                    potentials.append(tuple([path_vals[i][j-1],(0,-1)]))
                val,d_p = min(potentials)
                path_vals[i][j] = grid[i][j] + val
                paths[(i,j)] = d_p
        
    return path_vals[-1][-1]
    
    
def main():
    with open(sys.argv[1],'r') as grid_file:
        grid = read_grid(grid_file)
        print_grid(grid)
        print("  ")
        print("Min path total is",find_min_path_total(grid))
        
        

if __name__ == "__main__":
    main()
