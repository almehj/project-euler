#!/usr/bin/env python3

import sys
from math import log

def read_file(infile):
    answer = []

    for line in infile:
        l = [int(s.strip()) for s in line.split(',')]
        answer += [tuple(l)]

    return answer

def main():
    with open(sys.argv[1],'r') as infile:
        nums = read_file(infile)

        vals = [log(b)*e for b,e in nums]

        for num,val in zip(nums,vals):
            print("log(%d^%d) == %f"%(num[0],num[1],val))

        i = vals.index(max(vals))
        print("\nLine %d: log(%d^%d) == %f"%(i+1,nums[i][0],nums[i][1],vals[i]))
            
if __name__ == "__main__":
    main()
    
