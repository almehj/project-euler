#!/usr/bin/env python

import sys

def same_digits(a,b):

    da = list(str(a))
    db = list(str(b))

    da.sort()
    db.sort()

    return int("".join(da)) == int("".join(db))



max_n = int(sys.argv[1])

t_vec = [[] for i in range(max_n+1)]
t_vec[0] = 0
t_vec[1]=1

n = 2
ratio = -1
ratio_n = 0
while n <= max_n:
    if len(t_vec[n]) == 0:
        # n is prime
        t_vec[n] = n -1
        m = 2
        while m*n <= max_n:
            t_vec[m*n].append(n)
            m += 1
    else:
        tv = n
        for f in t_vec[n]:
            tv *= (1 - 1/f)
        t_vec[n] = int(tv)


        r = float(n)/t_vec[n]
        if r > ratio:
            ratio = r
            ratio_n = n
            print("phi(%d) = %d with ratio %.5f"%(n,t_vec[n],ratio))
    n += 1




    

