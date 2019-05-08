#!/usr/bin/env python3

import sys
import getopt
import string

from utils import seq_string

def read_data(infile):
    answer = []
    for line in infile:
        answer += [int(s.strip()) for s in line.split(',')]

    return answer


def compute_freq_table(text):
    counts = {}
    for c in text:
        counts[c] = counts.get(c,0) + 1

    answer = [(counts[x],x) for x in counts]

    return answer


def divide_text(text,cycle_len):
    answer = [[] for i in range(cycle_len)]

    i = 0
    for c in text:
        answer[i].append(c)
        i = (i+1)%cycle_len

    return answer

def analyze_text(text,cycle_len):
    divided = divide_text(text,cycle_len)

    for i in range(cycle_len):
        print(" %2d: %s"%(i,seq_string(divided[i])))
        table = compute_freq_table(divided[i])
        print("      %s"%(seq_string(table)))
        print(string.ascii_lowercase[table[0][1] - ord('a')])

def main():

    optlist,args = getopt.getopt(sys.argv[1:],"n:")

    cycle_len = 1

    for opt,val in optlist:
        if opt in ["-n"]:
            cycle_len = int(val)

    for infile_name in args:
        with open(infile_name,"r") as infile:
            cipher = read_data(infile)

            print("Read %d numbers from %s"%(len(cipher),infile_name))
            analyze_text(cipher,cycle_len)
            
if __name__ == "__main__":
    main()
