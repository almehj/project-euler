#!/usr/bin/env python3

goal_i = 1000000
n = 0
perm_len = 10
permute = [0]*10

chunk = 1
for i in range(1,perm_len):
    chunk *= i

i = 0
digits = [i for i in range(perm_len)]
dgt_ndx = 0
while len(digits) > 0:
    print("%d %d"%(i,n))
    if n < goal_i:
        if chunk + n < goal_i:
            dgt_ndx += 1
            n += chunk
        else:
            print("Digit %d is %d (%d)"%(i,digits[dgt_ndx],dgt_ndx))
            permute[i] = digits[dgt_ndx]
            digits.remove(permute[i])
            i += 1
            dgt_ndx = 0
            if len(digits) > 0:
                chunk /= len(digits)
                
perm_str = [str(j) for j in permute]
print("".join(perm_str))
