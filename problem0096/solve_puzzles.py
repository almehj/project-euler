#!/usr/bin/env python3

import sys

import sudoku


def parse_grid(lines):
    index = int(lines[0].split()[1])
    grid = sudoku.sudoku_puzzle(lines[1:])
    grid.name = "Puzzle %d"%(index)
    
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

        n_solved = 0
        total = 0
        for index in puzzles:
            grid = puzzles[index]

            print("Puzzle %d"%(index))
            print("%s"%(grid))
            
            grid.solve()

            if grid.is_solved():
                print("%3d: Solved. Solution:"%(index))
                n_solved += 1
            else:
                print("%3d: Not Solved. End State:"%(index))
            print("%s"%(grid))
                
            if grid.is_solved():
                total += 100*grid.grid[0][0] + 10*grid.grid[0][1] + grid.grid[0][2]
            else:
                if grid.is_possible():
                    print(" Solution still possible")
                else:
                    print(" Solution not possible")
                print("\nPossible distribution:")
                for n in range(10):
                    poss_list = grid.get_cells_by_n_possible(n)
                    print("%d: %d"%(n,len(poss_list)))
                    if len(poss_list) <= 400:
                        for ndx in poss_list:
                            poss_str = " ".join([str(i) for i in grid.possibles[ndx]])
                            print("   %d,%d: %s"%(ndx[0],ndx[1],poss_str))
                        

#                print("%3d: Possible lists when no more progress could be made:"%(index))
#                grid.report_possibles()

                
            print("\n")
        print("\nSolved %d of %d"%(n_solved,len(puzzles)))
        print("Total of upper left corners of all solved puzzles is %d"%(total))
        
if __name__ == "__main__":
    main()
