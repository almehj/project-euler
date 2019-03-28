#!/usr/bin/env python3

import sys
from string import ascii_uppercase as alphabet
import itertools

def gen_key(word):
    l = list(word)
    l.sort()

    answer = []
    n = 0
    curr_c = l[0]
    for c in l:
        if c != curr_c:
            n += 1
        answer += [alphabet[n]]
        curr_c = c

    return ''.join(answer)

def process_line(line):
    words = [s.strip() for s in line.split()]

    key = gen_key(words[0])
    for word in words:
        if gen_key(word) != key:
            print("Huh? gen_key(%s) == %s not %s"%(word,gen_key(word),key))
    print("%s: %s"%(key," ".join(words)))


def process_file(infile):
    for line in infile:
        process_line(line)

def read_anagram_file(infile):
    answer_set = {}
    
    for line in infile:
        words = [s.strip() for s in line.split()]        
        key = gen_key(words[0])
        answer_set[key] = answer_set.get(key,[]) + words
        
    return answer_set

def check_anagram(word1,word2):
    return gen_key(word1) == gen_key(word2)
    
def check_match(word1, word2):
    return gen_transform(word1,word2) != {}    

def gen_transform(clear,cipher):
    if len(clear) != len(cipher):
        return {}

    answer = {}
    for c1,c2 in zip(clear,cipher):
        if c1 not in answer:
            answer[c1] = c2
        if answer[c1] != c2:
            return {}

    return answer

def transform(word,d):
    answer = []
    for c in word:
        answer.append(d.get(c,"*"))
    return "".join(answer)

def print_matches(match_list):

    match_dict = {}
    for word,number in match_list:
        if word not in match_dict:
            match_dict[word] = []
        match_dict[word] += [number]

    for word in match_dict:
        l = match_dict[word]
        l.sort(reverse=True)
        print("  %s: %s"%(word,l[0]))

def dict_key(d):
    l = [(a,d[a]) for a in d]
    l.sort()
    return str(l)
    
def look_for_match(words,numbers):

    word2num = {}
    xforms = {}

    for word,number in itertools.product(words,numbers):
        d = gen_transform(word,number)
        if d != {}:
            word2num[word] = d
            key = dict_key(d)
            if key not in xforms:
                xforms[key] = []
            xforms[key] += [(word,number)]

    for key in xforms:
        if len(xforms[key]) > 1:
            print(" and ".join(["%s -> %s"%t for t in xforms[key]]))
        
    
def main():

    word_file = sys.argv[1]
    number_file = sys.argv[2]

    word_set = read_anagram_file(open(word_file,'r'))
    number_set = read_anagram_file(open(number_file,'r'))

    possibles = []
    for key in word_set:
        words = word_set[key]
        if key in number_set:
            possibles += [key]
            
    possibles.sort(key=len,reverse=True)

    for key in possibles:
        look_for_match(word_set[key],number_set[key])
            
if __name__ == "__main__":
    main()
            
    
