#!/usr/bin/env python

coins = [1,2,5,10,20,50,100,200]
total = 200


table = [[1 for j in range(total+1)] for i in range(len(coins))]

         
for i in range(1,len(coins)):
    val = coins[i]
    for j in range(total+1):
        answer = table[i-1][j]
        if j >= val:
            answer += table[i][j-val]
        table[i][j] = answer

print("%d combinations"%(table[-1][-1]))
         
