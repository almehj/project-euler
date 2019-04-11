#!/usr/bin/env python3

def seq_string(l,**kwargs):
    sep = kwargs.get("separator"," ")

    return sep.join([str(n) for n in l])

def binary_str(n):
    answer = []
    while n > 0:
        answer.append(n%2)
        n //= 2
    return seq_string(reversed(answer),separator="")

