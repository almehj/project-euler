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


def gen_numbers():
    
    numbers = {}
    for p in range(3,9):
        num_list = []
        n = 1
        while len(str(polyf(p,n))) < 4:
            n += 1
        while len(str(polyf(p,n))) < 5:
            num_list.append(polyf(p,n))
            n += 1
        numbers[p] = num_list
            
    return numbers

def gen_connects(numbers):
    fronts = {}
    front2num = {}
    backs = {}
    back2num = {}

    
    for p in range(3,9):
        l = numbers[p]
        fronts[p] = []
        backs[p] = []
        front2num[p] = {}
        back2num[p] = {}
        
        for n in l:
            front = n//100
            back = n%100

            if front < 10 or back < 10:
                continue

            fronts[p].append(front)
            backs[p].append(back)
            if front not in front2num[p]:
                front2num[p][front] = []
            front2num[p][front].append(n)
            if back not in back2num[p]:
                back2num[p][back] = []
            back2num[p][back].append(n)
            
    connections = {}
    connections['fronts'] = fronts
    connections['backs'] = backs
    connections['front2num'] = front2num
    connections['back2num'] = back2num
        
    return connections


def all_combos(l):

    if l == []:
        return [[]]

    answer = []
    for n in l:
        new_l = [x for x in l if x != n]
        for l2 in all_combos(new_l):
            answer.append([n] + l2)
    return answer


def find_rest(n,l,connects):

    print(n,l)
    if l == []:
        return [n]

    b = n%100
    p = l[0]
    
    print("  Looking for",b,"in fronts for ",p)
    fronts = connects['fronts'][p]
    if b in fronts:
        print("Yep",l[1:])
        for n_new in connects['front2num'][p][b]:
            print("   returning",[n] + find_rest(n_new,l[1:],connects))
            return [n] + find_rest(n_new,l[1:],connects)
    else:
        print("Nope\n\n")
        return []

def check(l,connects):


    print("\n\nConsidering",l)
    
    backs = connects['backs']
    fronts = connects['fronts']
    f2n = connects['front2num']
    b2n = connects['back2num']    


    cl = l + [l[0]]
    p = l[0]
    for b in backs[p]:
        for n in b2n[p][b]:
            print("\n=============   ",b,n)
            soln = find_rest(n,cl[1:],connects)
            if len(soln) > 4:
                if soln[0] == soln[-1]:
                    print("GOOGOO",soln,l,sum(soln[:-1]))
                else:
                    print("FOOGOO",soln,l)
    
    
def experiment(numbers,connects):

    backs = connects['backs']
    fronts = connects['fronts']
    f2n = connects['front2num']
    b2n = connects['back2num']    

    l = [n for n in range(4,9)]
    for l2 in all_combos(l):
        maybe = [3] + l2
        if check(maybe,connects):
            print(maybe)
            

    

def main():

    numbers = gen_numbers()
    connects = gen_connects(numbers)

    experiment(numbers,connects)

    


    
    



if __name__ == "__main__":
    main()
