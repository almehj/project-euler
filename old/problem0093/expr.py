#!/usr/bin/env python

import sys

ops = "+-*/"
vals = "ABCD"
l_paren = "("
r_paren = ")"

def tokenize(s):
    tokens = []
    for c in s:
        if str.isspace(c):
            continue
        else:
            if c in ops or\
               c in vals or\
               c == l_paren or c == r_paren:
                tokens.append(c)
            else:
                sys.stderr.write("Error: %s makes no sense\n"%c)
                return None

    return tokens

def crunch(initial_e):
    curr_e = initial_e[:]
    
    while len(curr_e) > 1:
        new_e = []
        if "*" in curr_e or "/" in curr_e:
            i = 0
            while i < len(curr_e):
                val = curr_e[i]
                op = curr_e[i+1]
                if op == "*":
                    val = val*curr_e[i+2]
                    if int(val) == val:
                        val = int(val)
                    new_e += [val] + curr_e[i+3:]
                    break
                elif op == "/":

                    if curr_e[i+2] == 0:
                        return -1
                    
                    val = val/curr_e[i+2]
                    if int(val) == val:
                        val = int(val)
                    new_e += [val] + curr_e[i+3:]
                    break
                else:
                    new_e += curr_e[i:i+2]
                    i += 2
        else:
            i = 0
            while i < len(curr_e):
                val = curr_e[i]
                op = curr_e[i+1]
                if op == "+":
                    val = val+curr_e[i+2]
                    new_e = [val] + curr_e[i+3:]
                    break
                elif op == "-":
                    val = val - curr_e[i+2]
                    new_e = [val] + curr_e[i+3:]
                    break
                i += 2
        curr_e = new_e
    return curr_e[0]


        
def evaluate(tokens,digits):


    answer = []

    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t in vals:
            answer.append(digits[t])
        elif t in ops:
            answer.append(t)
        elif t in l_paren:
            level = 1
            subex = []
            while level > 0:
                i += 1
                t = tokens[i]
                if t in l_paren:
                    level += 1
                if t in r_paren:
                    level -= 1
                subex.append(t)
            subex = subex[:-1]
            answer.append(evaluate(subex,digits))
        i += 1

    return crunch(answer)
            

def main():

    
    digits = {}
    for name,val in zip(vals,sys.argv[2]):
        digits[name] = int(val)

    print(digits)
        
    with open(sys.argv[1]) as infile:

        for line in infile:
            line = line.strip()
            print("line: /%s/"%line)
            tokens = tokenize(line)
            print("  Tokens:",tokens)
            value = evaluate(tokens,digits)
            print("  Eval:",value)

            print("\n\n")

if __name__ == "__main__":
    main()
