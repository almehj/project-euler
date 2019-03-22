#!/usr/bin/env python

import sys
from string import ascii_uppercase as alphabet

def triangle(n):
    return n*(n+1)//2

def pentagonal(n):
    return n*(3*n -1)//2

def hexagonal(n):
    return n*(2*n - 1)

def read_words(infile):

    words = []
    for line in infile:
        bits = [s.strip() for s in line.split(',')]
        words += [s[1:-1] for s in bits]

    return words


def word_score(word):
    return sum([alphabet.index(c)+1 for c in word])

def main():

    with open(sys.argv[1]) as infile:
        words = read_words(infile)
        triangles = []
        max_len = max([len(w) for w in words])
        n = 1
        max_tri = 0
        while max_tri < 26*max_len:
            max_tri +=  n
            n += 1
            triangles.append(max_tri)

        n_tris = 0
        for word in words:
            score = word_score(word)
            if score in triangles:
                n_tris += 1
                print("%s %d"%(word,score))
        print("%d triangle words"%(n_tris))
    
            
    
if __name__ == "__main__":
    main()
