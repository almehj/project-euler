#!/usr/bin/env python

def triangle(n):
    return( n*(n+1)//2 )

def square(n):
    return n**2

def pent(n):
    return n*(3*n - 1)//2

def hexag(n):
    return n*(2*n - 1)

def hept(n):
    return n*(5*n - 3)//2

def octag(n):
    return n*(3*n - 2)


def polyf(p,n):
    if p == 3:
        return triangle(n)
    elif p == 4:
        return square(n)
    elif p == 5:
        return pent(n)
    elif p == 6:
        return hexag(n)
    elif p == 7:
        return hept(n)
    elif p == 8:
        return octag(n)


for p in range(3,9):

    print("P =",p)

    with open("polyf_%d.txt"%p,"w") as outfile:
        n = 1

        while len(str(polyf(p,n))) < 4:
            n += 1

        while len(str(polyf(p,n))) < 5:
            outfile.write("%d\n"%polyf(p,n))
            n += 1
