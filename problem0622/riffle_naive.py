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


def riffle_study(n_cards):
    deck = [n for n in range(1,n_cards+1)]
    n_shuffles = 0
    while True:
        n_shuffles += 1
        deck = riffle(deck)
        if in_order(deck):
            break

    return n_shuffles


def main():
    max_cards = int(sys.argv[1])
    if max_cards < 2 or max_cards%2 != 0:
        print("Max number of cards must be greater than 2")
        sys.exit(-1)

    n = 2
    while n <= max_cards:
        r = riffle_study(n)
        print("%3d:"%n,r)
        sys.stdout.flush()
        n += 2


if __name__ == "__main__":
    main()
              
