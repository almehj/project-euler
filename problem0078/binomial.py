#!/usr/bin/env python


def list_func(l):
    if len(l) < 2: return 1

    answer = 2
    for i in range(1,len(l)-1):
        answer += int(l[i]/(i+1) + .5)

    return answer

l = [1]
n = 1
while n < 10:
    print(n,":",list_func(l))

    new_l = [0]*(n+1)
    new_l[0] = new_l[-1] = 1
    for i in range(1,n):
        new_l[i] = l[i-1]+l[i]

    n += 1
    l = new_l


