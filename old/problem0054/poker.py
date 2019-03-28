#!/usr/bin/env python3

import sys


card_ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
card_suits = ['C','D','H','S']

def parse_card_pair(pair):
    rank = card_ranks.index(pair[0])
    suit = card_suits.index(pair[1])

    return (rank,suit)

def parse_hands_from_line(line):
    cards = [parse_card_pair(s.strip()) for s in line.split()]
    return (poker_hand(cards[:5]),poker_hand(cards[5:]))

def card_str(c):
    return "%c%c"%(card_ranks[c[0]],card_suits[c[1]])

def hand_str(h):
    return " ".join([card_str(c) for c in h])        

def card_rank_counts(h):
    counts = {}
    for r in h.rank_list():
        counts[r] = counts.get(r,0) + 1

    return counts

def card_rank_set_counts(h):

    counts = card_rank_counts(h)
    answer = [0]*5
    for r in range(len(card_ranks)):
        i = counts.get(r,0)
        answer[i] += 1

    return answer

# Classifiers
def has_straight(h):
    hand_ranks = [c[0] for c in h]
    hand_ranks.sort()
    for i,r in enumerate(hand_ranks[:-1]):
        if (hand_ranks[i+1] - r) != 1:
            return False
    return True

def has_flush(h):
    suit = h[0][1]
    for s in [c[1] for c in h[1:]]:
        if s != suit:
            return False
    return True

def is_straight(h):
    return has_straight(h) and not has_flush(h)

def is_flush(h):
    return has_flush(h) and not has_straight(h)

def is_straight_flush(h):
    return has_straight(h) and has_flush(h)

def is_four_kind(h):
    counts = card_rank_set_counts(h)
    if counts[4] > 0:
        return True
    return False

def is_full_house(h):
    counts = card_rank_set_counts(h)
    return (counts[2] == 1) and (counts[3] == 1)

def is_three_kind(h):
    counts = card_rank_set_counts(h)
    return (counts[3] == 1) and (counts[1] == 2)

def is_two_pair(h):
    counts = card_rank_set_counts(h)
    return (counts[2] == 2)

def is_one_pair(h):
    counts = card_rank_set_counts(h)
    return (counts[2] == 1) and (counts[1] == 3)

def is_bust(h):
    counts = card_rank_set_counts(h)
    return (counts[1] == 5) and not(has_flush(h) or has_straight(h))

def rank_by_sets(h):
    counts = card_rank_counts(h)
    ranks = {}
    for r in counts:
        if counts[r] not in ranks:
            ranks[counts[r]] = []
        ranks[counts[r]].append(r)
    answer = []
    for s in range(max(counts.values()),0,-1):
        if s in ranks:
            ranks[s].sort(reverse=True)
            answer += ranks[s]

    return tuple(answer)        


UNKNOWN = -1
BUST = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_KIND = 7
STRAIGHT_FLUSH = 8

hand_names = {
    UNKNOWN:"Unknown",
    BUST:'Bust',
    ONE_PAIR:'One Pair',
    TWO_PAIR:'Two Pair',
    THREE_KIND:'Three of a Kind',
    STRAIGHT:'Straight',
    FLUSH:'Flush',
    FULL_HOUSE:'Full House',
    FOUR_KIND:'Four of a Kind',
    STRAIGHT_FLUSH:'Straight Flush',
    }

hand_classifiers = {
    STRAIGHT_FLUSH:is_straight_flush,
    FOUR_KIND:is_four_kind,
    FULL_HOUSE:is_full_house,
    FLUSH:is_flush,
    STRAIGHT:is_straight,
    THREE_KIND:is_three_kind,
    TWO_PAIR:is_two_pair,
    ONE_PAIR:is_one_pair,
    BUST:is_bust
}

def compute_hand_rank(hand):

    for hand_rank in hand_classifiers:
        if hand_classifiers[hand_rank](hand):
            return hand_rank
        
    return UNKNOWN

def hand_name(rank):
    return hand_names[rank]


class poker_hand(object):

    def __init__(self,cards):
        self.cards = cards[:]
        self.cards.sort(reverse=True)
        self.rank = (compute_hand_rank(self),rank_by_sets(self))
        
    def __eq__(self,other):
        return self.rank == other.rank

    def __gt__(self,other):
        return self.rank > other.rank
        
    def __lt__(self,other):
        return not (self > other or self == other)
    
    def __str__(self):
        return hand_str(self.cards)

    def __iter__(self):
        return iter(self.cards)

    def __getitem__(self,i):
        return self.cards[i]

    def rank_list(self):
        return [c[0] for c in self.cards]

    def high_rank(self):
        return max([c[0] for c in self.cards])

    def hand_name(self):
        return hand_name(self.rank[0])

def main():
    with open(sys.argv[1]) as infile:
        results = {}
        n_hands = 0
        for line in infile:
            if line.strip() == "":continue
            
            A,B = parse_hands_from_line(line)
            result = "Draw"
            if A > B:
                result = "A Wins"
            elif B > A:
                result = "B Wins"

            results[result] = results.get(result,0) + 1

            print("A:%s %s"%(A,A.hand_name()))
            print("B:%s %s"%(B,B.hand_name()))
            print(result)
            print("\n")

            n_hands += 1
            
        print("\nFinal Results (%d hands)"%(n_hands))
        for result in results:
            print(" %s: %d"%(result,results[result]))


if __name__ == "__main__":
    main()
