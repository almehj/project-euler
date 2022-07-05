#!/usr/bin/env python

import sys
import getopt
import logging

def check_DLV(n):
    for c in ['D','L','V']:
        if n.count(c) > 1:
            return False
    return True

def is_legal(n):
    logging.debug("Checking validity of Roman numeral %s"%(n))

    logging.debug("   Checking DLV only once")
    if check_DLV(n) == False:
        logging.debug("      %s FAILS"%(n))
        return False
    
    return True

def reduce_roman(num):
    logging.debug("Reducing roman numeral %s"%(num))

    answer = []
    for c in num:
        answer.append(c)
        
    return "".join(answer)

def process_file(infile_name):

    total_saved = 0
    with open(infile_name,"r") as infile:
        for line in infile:
            num = line.strip()
            if is_legal(num):
                r_num = reduce_roman(num)
                total_saved += (len(num) - len(r_num))
            else:
                print("Numeral %s is invalid"%(num))
                
    return total_saved

def main():

    optlist,args = getopt.getopt(sys.argv[1:],"v")

    log_level = logging.INFO

    for opt,val in optlist:
        if opt in ["-v"]:
            log_level = logging.DEBUG


    logging.basicConfig(level=log_level)
    
    for infile_name in args:
        print("Processing %s..."%(infile_name))
        n_saved = process_file(infile_name)
        print("   %d characters saved"%(n_saved))


if __name__ == "__main__":
    main()
