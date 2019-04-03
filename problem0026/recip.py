#!/usr/bin/env python3

import sys
import logging

from utils import seq_string

def do_recip_calc(r):

    answer = []
    remain = 10
    in_nonzero = False
    done = False
    seen = []

    while not done:
        d = remain//r
        logging.debug("remain = %d d = %d in_nonzero = %s. seen: %s"%(remain,d,in_nonzero,str(seen)))
        if d != 0 and not in_nonzero:
            in_nonzero = True
        remain -= d*r
        remain *= 10

        if in_nonzero:
            try:
                if remain in seen:
                    done = True
                    if d != 0:
                        if d not in answer:
                            answer.append(d)
                        answer.insert(answer.index(d),'(')
                        answer.append(')')
                else:
                    seen.append(remain)
            except Exception as e:
                print("Died with answer [%s]"%(seq_string(answer)))
                print(str(e))
                sys.exit(-1)
                
        if not done:
            answer.append(d)


    return "0."+seq_string(answer,separator="")

    
    
def main():

    logging.basicConfig(level=logging.DEBUG)
    
    for r in [int(n) for n in sys.argv[1:]]:

        result = do_recip_calc(r)

        pat_len = 0
        if '(' in result:
            pat_len = result.index(')') - result.index('(')

        print("%4d: %2d %s"%(r,pat_len,result))

if __name__ == "__main__":
    main()
