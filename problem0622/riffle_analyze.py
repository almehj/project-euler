#!/usr/bin/env python
import getopt
import sys
from riffle_chains import index_chain, index_chain_length
from math import log10
from factor import factors, n_divisors


def main():

    optlist,args = getopt.getopt(sys.argv[1:],"al")
    list_mode = False
    length_only = False
    for opt,val in optlist:
        if opt in ["-a"]:
            list_mode = True
        elif opt in ["-l"]:
            length_only = True

    for n_max in args:
        n_max = int(n_max)
        if n_max < 2 or n_max%2 != 0:
            print("Can't do %d: number of cards must be an even number greater than 0"%n_max)
        if list_mode:
            n = 2
            while n <= n_max:
                chain = index_chain_length(1,n)
                ln2 = log10(n)/log10(2)
                print("%5d"%n, chain, "factors of n:"," ".join([str(f) for f in factors(n)])," (%d divisors)"%n_divisors(n))
                n += 2
        else:
            ln = log10(n_max)
            ln2 = ln/log10(2)

            if length_only:
                chain_length = index_chain_length(1,n_max)
                print(n_max, "(l10: %.4f, l2: %.4f)" % (ln, ln2), chain_length)
            else:
                chain = index_chain(1, n_max)
                print(n_max, "(l10: %.4f, l2: %.4f)"%(ln,ln2), len(chain), ":", "->".join([str(n) for n in chain] + [str(chain[0])]))


if __name__ == "__main__":
    main()
              
