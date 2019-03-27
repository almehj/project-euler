#!/usr/bin/env python3

import sys

def prep(word):
    word = word.strip()
    if word[0] == '"':
        word = word[1:-1]
    return word
    
def read_words(infile,max_len=100):
    answer = []
    for line in infile:        
        answer += [prep(s) for s in line.split(',')]
        answer = [w for w in answer if len(w) <= max_len]
    return answer

def main():

    max_len = int(sys.argv[2])
    with open(sys.argv[1],'r') as infile:
        words = read_words(infile,max_len)
        by_key = {}
        for word in words:
            key = list(word)
            key.sort()
            key = ''.join(key)

            by_key[key] = by_key.get(key,[]) + [word]

        for l in by_key.values():
            if len(l) > 1:
                print(" ".join(l))

if __name__ == "__main__":
    main()
