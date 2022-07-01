#!/usr/bin/env python


import sys


n0 = int(sys.argv[1])
dn = 8912517754604
a = 1504170715041707

n = n0
states = [n0]
ops = 0
while n >= n0:
    n += dn
    n %= a
    ops += 1
#    states.append(n)

print("new n:",n)
print("ops:", ops,"delta:",n0-n)
sys.exit(0)


segs = {}
ndx = 0
segs[ndx] = []
for i,n in enumerate(states):
    if i == 0:
        segs[0].append(n)
        continue
    if states[i] < states[i-1]:
        ndx += 1
        segs[ndx] = []
    segs[ndx].append(n)

print(len(segs),"segments")
print("   lengths:")
for ndx in range(len(segs)-1):
    print("  ",ndx,":",len(segs[ndx]),segs[ndx+1][0]-segs[ndx][0],(segs[ndx+1][0]-segs[ndx][0])%a)

print(dn,dn*(int(a/dn)+1),dn*(int(a/dn)+1)%a)
