#!/usr/bin/env python

import sys

digits = range(10)
str_digits = [str(d) for d in digits]



def sameness_vector(a,b):
    if len(a) != len(b):
        return []

    answer = []
    for i in range(len(a)):
        if a[i] == b[i]:
            answer.append(i)

    return tuple(answer)


for infile_name in sys.argv[1:]:
    with open(infile_name) as infile:
        numbers = []
        for line in infile:
            s = line.strip()
            numbers.append(s)

        sames = {}
        for i,a in enumerate(numbers):
            for b in numbers[i+1:]:
                t = sameness_vector(a,b)
                if len(t) > 1:
                    if t not in sames:
                        sames[t] = []
                    sames[t].append((a,b))


        vecs = [(len(a),a) for a in sames]
        vecs.sort()
        vecs = [t[1] for t in vecs]

        for v in vecs:
            d = {}
            for a,b in sames[v]:
                if a not in d:
                    d[a] = []
                d[a].append(b)

            max_l = -1
            max_a = None
            for a in d:
                if len(d[a]) > max_l:
                    max_l = len(d[a])
                    max_a = a

            print(v,max_a, d[max_a])
