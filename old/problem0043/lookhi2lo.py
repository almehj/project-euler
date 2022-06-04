#!/usr/bin/env python



def is_possible(n):
    seen = []
    while n > 0:
        if n%10 in seen:
            return False
        seen.append(n%10)
        n //= 10

    return True


factors = [17,13,11,7,5,3,2]
possibles = {}

for k in factors:
    n = 1
    possible = []
    
    while n*k < 1000:
        if is_possible(n*k):
            possible.append(n*k)
        n += 1

    possibles[k] = possible


def get_digits(n,l):
    answer = []
    while n > 0:
        answer.append(n%10)
        n //= 10
    if len(answer) < l:
        answer.append(0)
    answer.reverse()
    return answer
    
i = 0
l = 3
candidates = possibles[factors[i]][:]
new_candidates = []

while i < len(factors)-1:

    print("\n\nk is",factors[i],"\n\n")
    next_layer = possibles[factors[i+1]][:]
    for n in candidates:
        digits = get_digits(n,l)
        top_two = digits[0]*10 + digits[1]
        print("consider",n,digits)
        print("top two",top_two)

        for d in range(10):
            if d not in digits:
                c = int(str(d) + str(top_two))
                if c in next_layer:
                    c = int(str(d)+"".join([str(x) for x in digits]))
                    print("maybe","%03d"%c)
                    new_candidates.append(c)
                    
        
    candidates = new_candidates
    new_candidates = []
    
    i += 1
    l += 1

total = 0
for n in candidates:
    digits = get_digits(n,9)
    for i in range(1,10):
        if i not in digits:
            c = int(str(i)+str(n))
            total += c
            print(c)

print(total)
            
