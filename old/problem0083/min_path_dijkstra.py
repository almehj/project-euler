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

    max_val = max([max(row) for row in grid])
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    unvisited = []
    visited = []
    node_map = {}
    for i,row in enumerate(grid):
        for j,val in enumerate(row):
            if (i,j) == (0,0): # 'Source' node
                val = grid[i][j]
            else:
                val = max_val*n_rows*n_cols
            unvisited.append([val,(i,j)])
            node_map[(i,j)] = unvisited[-1]

    unvisited.sort()
    while len(unvisited) > 0:
        curr = unvisited.pop(0)
        i,j = curr[1]

        for nbr_loc in [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]:
            if nbr_loc in node_map:
                if nbr_loc not in visited:
                    nbr = node_map[nbr_loc]
                    val = curr[0] + grid[nbr_loc[0]][nbr_loc[1]]
                    if val < nbr[0]:
                        nbr[0] = val
        visited.append(curr[1])
        unvisited.sort()

        
        
    return node_map[(n_rows-1,n_cols-1)][0]
                
    
def main():
    with open(sys.argv[1],'r') as grid_file:
        grid = read_grid(grid_file)
        #print_grid(grid)
        print("  ")
        print("Min path total is",find_min_path_total(grid))
        
        

if __name__ == "__main__":
    main()
