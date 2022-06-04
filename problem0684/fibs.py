#!/usr/bin/env python

def fib(n):
    if n == 0: return 0
    if n == 1: return 1

    return fib(n-2) + fib(n-1)


f = [0,1]
n = 2

while n < 91:
    f.append(f[-1]+f[-2])
    n += 1

for i,n in enumerate(f):
    print("%2d: %d"%(i,n))
    


def s(n):
    n_nines = n // 9
    rem = n - 9*n_nines

    answer = rem
    for i in range(n_nines):
        answer *= 10
        answer += 9

    return answer

total = 0
for n in range(1,21):
    total += s(n)

print(total)
#print(s(2880067194370816120))

total = 0
total2 = 0
for i in range(200):
    total += s(i)
    total2 = total + 1
    print("%3d: %30d %30d %30d %30d"%(i,s(i),s(i)+1,total,total2))
