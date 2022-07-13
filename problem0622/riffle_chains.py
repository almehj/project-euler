#!/usr/bin/env python


import sys


def riffle(l):
    k = len(l)//2

    answer = []

    for i in range(k):
        answer.append(l[i])
        answer.append(l[k+i])

    return answer


def in_order(l):
    for i in range(len(l)):
        if l[i]-1 != i:
            return False
    return True


def print_deck(l):
    m = len(l)
    width = len(str(m))
    format = "%%%dd"%width
    cards = [format%n for n in l]
    print(" ".join(cards))


def next_index(i,n_cards):

    k = n_cards//2
    if i%2 == 0:
        return i//2
    else:
        n = (i-1)//2
        return k + n


def find_chains(l):

    answer = []

    i = 0
    seen = {}
    curr = []
    while i < len(l):
        curr.append(l[i])
        seen[i] = 1
        i = next_index(i,len(l))
        if i in seen:
            answer.append(curr)
            curr = []
            i = 0
            while i in seen and i < len(l):
                i += 1

    return answer

    
def main():
    n_cards = int(sys.argv[1])
    if n_cards < 2 or n_cards%2 != 0:
        print("number of cards must be an even number greater than 0")
        sys.exit(-1)

    deck = [n for n in range(1,n_cards+1)]
    next_deck = [deck[next_index(i,n_cards)] for i in range(n_cards)]
    print_deck(deck)
    print_deck(next_deck)
    print_deck(riffle(deck))

    chains = find_chains(deck)
    for chain in chains:
        print("   ",len(chain),":","->".join([str(n) for n in chain]+[str(chain[0])]))

    
if __name__ == "__main__":
    main()
              
