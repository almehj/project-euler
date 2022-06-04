#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as infile:

    outfile = None
    for line in infile:
        if "Grid" in line:
            n = int(line.split()[1].strip())
            outfile_name = "Grid%03d.txt"%(n)
            if outfile != None:
                outfile.close()
            outfile = open(outfile_name,'w')
            print("Opening",outfile_name)
        outfile.write("%s\n"%line.strip())
