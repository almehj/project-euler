#!/usr/bin/env python


import sys


def riffle(l):
    k = len(l) // 2

    answer = []

    for i in range(k):
        answer.append(l[i])
        answer.append(l[k + i])

    return answer


def in_order(l):
    for i in range(len(l)):
        if l[i] - 1 != i:
            return False
    return True


def print_deck(lead_str, l):
    m = len(l)
    width = len(str(m))
    format = "%%%dd" % width
    cards = [format % n for n in l]
    print(lead_str, " ".join(cards))


def next_index(i, n_cards):
    k = n_cards // 2

    if i < k:
        return 2 * i
    else:
        return 2 * i - 2 * k + 1


def index_chain(i, n_cards):
    answer = [i]
    i = next_index(i, n_cards)
    while i != answer[0]:
        answer.append(i)
        i = next_index(i, n_cards)

    return answer


def index_chain_length(i,n_cards):
    answer = 1
    orig = i
    i = next_index(i,n_cards)
    while i != orig:
        answer += 1
        i = next_index(i,n_cards)
    return answer


def find_chain(l, i):
    answer = []
    dest_ndx = i
    while i < len(l):
        answer.append(l[i])
        i = next_index(i, len(l))
        if i == dest_ndx:
            return answer

    return answer


def main():
    n_cards = int(sys.argv[1])
    if n_cards < 2 or n_cards % 2 != 0:
        print("number of cards must be an even number greater than 0")
        sys.exit(-1)

    deck = [n for n in range(n_cards)]
    next_deck = [next_index(i, n_cards) for i in range(n_cards)]
    rif_deck = riffle(deck)
    try_deck = [0] * n_cards
    for i in range(n_cards):
        try_deck[next_deck[i]] = deck[i]

    print_deck("orig:", deck)
    print_deck("next:", next_deck)
    print_deck("riff:", rif_deck)
    print_deck("try :", try_deck)

    chain = find_chain(deck, 1)
    print("   ", len(chain), ":", "->".join([str(n) for n in chain] + [str(chain[0])]))

    print_deck("orig:", deck)
    n = 0
    while try_deck[1] != 1:
        n += 1
        print("*****SHUFFLE ", n)
        print_deck("riff:", rif_deck)
        print_deck("try :", try_deck)
        rif_deck = riffle(rif_deck)
        next_deck = [next_index(i, n_cards) for i in next_deck]
        for i in range(n_cards):
            try_deck[next_deck[i]] = deck[i]
    print("*****SHUFFLE ", n + 1)
    print_deck("riff:", rif_deck)
    print_deck("try :", try_deck)


if __name__ == "__main__":
    main()
