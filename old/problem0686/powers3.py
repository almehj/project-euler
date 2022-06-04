#!/usr/bin/env python

powers = {}

def seq(n):
    answer = [485,196]
    n -= 2
    while n > 1:
        n -= 2
        answer.append(289)
        answer.append(196)
    answer.append(485)

    return answer

print(seq(7))
print(seq(25))
print(seq(33))
      
