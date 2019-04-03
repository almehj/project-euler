#!/usr/bin/env python3

def seq_string(l,**kwargs):
    sep = kwargs.get("separator"," ")

    return sep.join([str(n) for n in l])
