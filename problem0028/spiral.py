#!/usr/bin/env python3

import sys

import utils

def compute_spiral(n):

    i,j = (0,0)
    z = 1
    spiral = 0
    dirs = [(0,1),(-1,0),(0,-1),(1,0)]
    dir_lims = [0,0,0,0]
    dir_ndx = 0

    answer = []
    while z <= n:
        answer.append(((i,j),z))

        
        di,dj = dirs[dir_ndx]
        i += di
        j += dj

        ndx = i
        if dir_ndx%2 == 0:
            ndx = j
        if abs(ndx) > dir_lims[dir_ndx]:
            dir_lims[dir_ndx] += 1
            dir_ndx += 1
            dir_ndx %= 4

        z += 1
            
    return answer
        
def print_spiral(spiral):

    first_row = max([t[0][0] for t in spiral])
    last_row = min([t[0][0] for t in spiral])

    width = max([len(str(n)) for n in [t[1] for t in spiral]])
    format_str = "%%%ds"%(width)

    first_col = min([t[0][1] for t in spiral])
    last_col = max([t[0][1] for t in spiral])
    n_in_row = last_col - first_col + 1


    
    r_ndx = first_row

    while r_ndx >= last_row:

        nums = [format_str%(" ")]*n_in_row
        pts = [t for t in spiral if t[0][0] == r_ndx]
        pts.sort()
        for pt in pts:
            j = pt[0][1] + n_in_row//2 + n_in_row%2 - 1 
            nums[j] = format_str%(pt[1])
                            
        print(utils.seq_string(nums))
        
        r_ndx -= 1
    
def sum_diagonals(spiral):

    total = 0
    for pt,n in spiral:
        if abs(pt[0]) == abs(pt[1]):
            total += n

    return total
    
def main():
    n = int(sys.argv[1])
    spiral = compute_spiral(n)
    if n < 1000:
        print_spiral(spiral)
    print("\nSum on diagonals is %d"%(sum_diagonals(spiral)))


if __name__ == "__main__":
    main()
