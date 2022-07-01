#!/usr/bin/env python


def max_in_table(table):
    answer = -1
    for row in table:
        for n in row:
            if n > answer:
                answer = n
    return answer
            

def print_table(table):
    m = max_in_table(table)
    width = len(str(m))
    fmt_str = "%%%dd"%width

    i = 1
    for row in table:
        print("%3d: %s"%(i," ".join([fmt_str%n for n in row])))
        i += 1

table = []
n = 1

while True:
    table.append([1]*n)
    table[0].append(1)
    for i in range(1,n):
        table[i].append(-1)
        for j in range(n+1):
            table[i][j] = table[i-1][j]
            if j >= i+1:
                table[i][j] += table[i][j-i-1]
    n_parts = table[-1][-1]
    print("%5d: %d"%(n,n_parts))
    if n_parts%1000000 == 0:
        break
    n += 1
