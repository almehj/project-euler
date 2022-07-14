#!/usr/bin/env python

import sys


n_fuses = int(sys.argv[1])
n_good = int(sys.argv[2])


if n_good < 2:
    print("You gotta have 2 or more good fuses! Go Away!")
    sys.exit(0)

n_bad = n_fuses - n_good

fuses = []
for i in range(n_fuses):
    if i < n_bad:
        fuses.append('X')
    else:
        fuses.append('*')

topline = "     " + " ".join(fuses)
border = "".join(['-']*len(topline))
print(topline)
print(border)
      

min_tries = 0
for i in range(n_fuses):
    line = []
    for j in range(n_fuses):
        if i >= j:
            line.append(' ')
        elif fuses[i] == 'X' or fuses[j] == 'X':
            line.append('X')
            min_tries += 1
        else:
            line.append('*')

    print("%3s:"%fuses[i]," ".join(line))

print("\nTry at least %d"%(min_tries+1))
