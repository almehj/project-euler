#!/usr/bin/env python

numerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

replace = {
    ('I',4):'IV',
    ('I',5):'V',
    ('I',6):'VI',
    ('I',7):'VII',
    ('I',8):'VIII',
    ('I',9):'IX',
    ('I',10):'X',
    ('X',4):'XL',
    ('X',5):'L',
    ('X',6):'LX',
    ('X',7):'LXX',
    ('X',8):'LXXX',
    ('X',9):'XC',
    ('X',10):'C',
    ('C',4):'CD',
    ('C',5):'D',
    ('C',6):'DC',
    ('C',7):'DCC',
    ('C',8):'DCCC',
    ('C',9):'CM'
    }

times_ten = {
    'I':'X',
    'X':'C',
    'C':'M'
    }

def descend_check(n):
    curr_top ='M'
    
    for c in n:
        print('Considering',c)

    return True

def dlv_check(n):
    for c in ['D','L', 'V']:        
        if n.count(c) > 1:
            return False
    return True

def valid(n):
    if not descend_check(n):
        return False
    if not dlv_check(n):
        return False


    return True

def tokenize(n):
    answer = []
    curr_t = None
    for c in n:
        if curr_t == None:
            curr_t = c
        elif c == curr_t:
            answer.append(curr_t)
        elif numerals[c] < numerals[curr_t]:
            answer.append(curr_t)
            curr_t = c
        elif (curr_t == 'I' and c in ['V','X']) or \
             (curr_t == 'X' and c in ['L','C']) or \
             (curr_t == 'C' and c in ['D','M']):             
                answer.append(curr_t+c)
                curr_t = None
        else:
            print("huh?",n,c,curr_t)
    if curr_t != None:
        answer.append(curr_t)

    return answer

def expand_tokens(tk):
    answer = []
    for t in tk:
        if t == 'V':
            answer += ['I']*5
        elif t == 'IV':
            answer += ['I']*4
        elif t == 'IX':
            answer += ['I']*9
        elif t == 'L':
            answer += ['X']*5
        elif t == 'XL':
            answer += ['X']*4
        elif t == 'XC':
            answer += ['X']*9
        elif t == 'D':
            answer += ['C']*5
        elif t == 'CD':
            answer += ['C']*4
        elif t == 'CM':
            answer += ['C']*9
        else:
            answer.append(t)
        
    return answer

def join_tokens(tk):
    tokens = []
    
    curr = None
    n_curr = 0
    for t in tk:
        if curr == None:
            curr = t
            n_curr = 1
        elif t == curr:
            n_curr += 1
        else:
            tokens.append((curr,n_curr))
            curr = t
            n_curr = 1
    if curr != None:
        tokens.append((curr,n_curr))

    return tokens



def reduce_roman(n):
    tokens = tokenize(n)
    tokens = expand_tokens(tokens) 
    tokens = join_tokens(tokens)
    
    answer = []
    for t in tokens:
        while t[1] > 10:
            answer.append(times_ten[t[0]])
            t[1] -= 10
            
        if t in replace:
            answer.append(replace[t])
        else:
            answer += [t[0]]*t[1]
            
    return "".join(answer)



import sys

total = 0
for n in sys.argv[1:]:

    

    print(n,len(n),"numerals")
    print("  tokens:",tokenize(n))
    print("  expand:",expand_tokens(tokenize(n)))
    print("    join:",join_tokens(expand_tokens(tokenize(n))))
    rn = reduce_roman(n)
    print("  reduce:",rn,len(rn),"numerals")
    print(" ")

    total += len(n) - len(rn)
    
print(total)
