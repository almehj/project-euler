#!/usr/bin/env python3

import sys

import sudoku


def parse_grid(lines):
    index = int(lines[0].split()[1])
    grid = sudoku.sudoku_puzzle(lines[1:])

    return index,grid
        
def read_puzzles(infile):
    grids = {}
    lines = []
    for line in infile:
        lines.append(line)
        if len(lines) == 10:
            i,grid = parse_grid(lines)
            grids[i] = grid
            lines = []
            
    return grids


def main():

    with open(sys.argv[1]) as infile:
        puzzles = read_puzzles(infile)

        for index in puzzles:
            grid = puzzles[index]

            print("Puzzle %d"%(index))
            print("%s"%(grid))

            grid.solve()
            
            print("Solution")
#            grid.report_zeros()
#            grid.report_possibles()
            print("%s"%(grid))
            print("\n")

if __name__ == "__main__":
    main()
