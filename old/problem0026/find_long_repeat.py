#!/usr/bin/env python3

import sys

import recip

def main():

    max_pat_len = -1,-1
    for r in range(1,int(sys.argv[1])+1):

        result = recip.do_recip_calc(r)

        pat_len = 0
        if '(' in result:
            pat_len = result.index(')') - result.index('(')
        if max_pat_len[0] < pat_len:
            max_pat_len = pat_len,r

        print("%4d: %2d %s"%(r,pat_len,result))

    print("Max length %d for r == %d"%max_pat_len)
if __name__ == "__main__":
    main()
