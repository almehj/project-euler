#!/usr/bin/env python

import sys


def diff(a,b):
    answer = []
    for i,n in enumerate(a):
        answer.append(n - b[i])

    return tuple(answer)

def dot(a,b):
    answer = 0
    for i,n in enumerate(a):
        answer += n*b[i]

    return answer

n_max = int(sys.argv[1]) + 1


origin = (0,0)
tot_count = 0
right_count = 0
for x1 in range(n_max):
    for y1 in range(n_max):
        for x2 in range(n_max):
            for y2 in range(n_max):
                if (x1 != x2 or y1 != y2) and \
                   (x1+y1) > 0 and \
                   (x2+y2) > 0:

                    tot_count += 1
                    coords = [origin,(x1,y1),(x2,y2)]

                    # gen three side vectors
                    sides = [diff(coords[i],coords[j]) for i,j in [(0,1),(0,2),(1,2)]]
                    if (0,0) in sides:
                        print("boo")
                        sys.exit(0)
                    for i,j in [(0,1),(0,2),(1,2)]:
                        if dot(sides[i],sides[j]) == 0:
                            right_count += 1
                            print('Found',coords)

print(tot_count," total coordinate sets")
print(right_count//2,"unique right triangles")

    
