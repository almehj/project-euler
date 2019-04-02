#!/usr/bin/env python3

import sys

def do_recip_calc(r):

    answer = []
    remain = 10
    in_nonzero = False
    done = False
    seen = []
    while not done:
        d = remain//r
        if d != 0 and not in_nonzero:
            in_nonzero = True
        remain -= d*r
        remain *= 10

        if in_nonzero:
            if r in seen:
                done = True
                if d != 0:
                    answer.insert(answer.index(str(d)),'(')
                    answer.append(')')
            else:
                seen.append(r)
        
        answer.append(str(d))


    return "0."+"".join(answer)

    
    
def main():

    max_pat_len = -1,-1
    for r in range(1,int(sys.argv[1])+1):

        result = do_recip_calc(r)

        pat_len = 0
        if '(' in result:
            pat_len = result.index(')') - result.index('(')
        if max_pat_len[0] < pat_len:
            max_pat_len = pat_len,r

        print("%4d: %2d %s"%(r,pat_len,result))

    print("Max length %d for r == %d"%max_pat_len)
if __name__ == "__main__":
    main()
