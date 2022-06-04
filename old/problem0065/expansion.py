#!/usr/bin/env python

import sys
import prime_numbers
import logging

def product(fact_l):
    answer = 1

    for f,p in fact_l:
        answer *= f**p

    return answer

def reduce(num,den):
    num_f = prime_numbers.factorization(num)
    den_f = prime_numbers.factorization(den)

    logging.debug("   num_fact: %s"%(num_f))
    logging.debug("   den_fact: %s"%(den_f))
    for t in num_f[:]:
        fact = t[0]
        l = [g for g in den_f if g[0] == fact]
        if len(l) > 0:
            num_f.remove(t)
            for k in l:
                den_f.remove(k)
                if t[1] < k[1]:
                    den_f.append((k[0],k[1]-t[1]))
                elif t[1] > k[1]:
                    num_f.append((t[0],t[1]-k[1]))

    return product(num_f),product(den_f)


def e_frac_term(n):

    if n == 0:
        return 2
    
    n -= 1
    pos = n//3
    ndx = n%3

    if ndx == 1:
        return 2*(pos+1)
    else:
        return 1

def frac_string(num,den):
    if num == 0:
        return "0"
    elif den == 1:
        return "%d"%(num)
    else:
        return "%d/%d"%(num,den)

    
def main():
    logging.basicConfig(level=logging.INFO)
    
    for max_n in sys.argv[1:]:
        max_n = int(max_n)
        for start_n in range(max_n,max_n+1):
            num = 0
            den = 1
            n = start_n
            
            print("Convergent number %d of e"%(n+1))        
            while n > 0:

                logging.debug("Top of loop (n=%d): %d %d"%(n,num,den))
                term = e_frac_term(n)
                logging.debug("Term is %d"%(term))
                num += term*den
                logging.debug("After adding term %d: %d %d"%(term,num,den))
                num,den = reduce(num,den)
                logging.debug("After reduce: %d %d"%(num,den))
                den,num = num,den
                logging.debug("After flip: %d %d"%(num,den))
                n -= 1
            
            # first term is a 2
            num += e_frac_term(0)*den
            num,den = reduce(num,den)
            print("   %.9f or %s"%(float(num)/den,frac_string(num,den)))            


if __name__ == "__main__":
    main()

    
