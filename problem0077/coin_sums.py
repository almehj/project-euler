#!/usr/bin/env python
import sys
import prime_numbers

total = int(sys.argv[1])
coins = prime_numbers.primes_less_than(total+1)

print("coins =",coins)

table = [[1 for j in range(total+1)] for i in range(len(coins))]
for i in range(len(table[0])):
    if total%coins[0] != 0:
        table[0][i] = 0
    else:
        table[0][i] = 1
         
for i in range(1,len(coins)):
    val = coins[i]
    for j in range(total+1):
        answer = table[i-1][j]
        if j >= val:
            answer += table[i][j-val]
        table[i][j] = answer

if total < 50:
    for row in table:
        print(" ".join(["%4d"%n for n in row]))
        

for j in range(total+1):
    if table[-1][j] > 5000:
        print(j," has ",table[i][j],"combos")
        break
         
