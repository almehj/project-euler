#!/usr/bin/env python


import sys


def calc_roll_table(n_dice,n_sides):
    rolls = {}
    for s in range(n_dice,n_sides*n_dice+1):
        rolls[s] = 0

    roll = [1]*n_dice
    n_rolls = n_sides**n_dice
    n = 0
    while n < n_rolls:
        s = sum(roll)
        rolls[s] += 1

        for i in range(len(roll)):
            roll[i] += 1
            if roll[i] > n_sides:
                roll[i] = 1
            else:
                break
        n += 1

    return rolls


def main():
    peter = calc_roll_table(9,4)
    n_peter = sum([n for n in peter.values()])
    colin = calc_roll_table(6,6)
    n_colin = sum([n for n in colin.values()])

    c_results = {}
    p_possibles = [s for s in peter]
    for s in range(6,36):

        wins = sum([peter[n] for n in peter if n < s])
        losses = sum([peter[n] for n in peter if n > s])
        draws = sum([peter[n] for n in peter if n == s])

        c_results[s] = (wins,losses,draws)


    total = 0
    for s in range(6,36):
        total += colin[s]*c_results[s][1]
    den = n_peter*n_colin

    print(total,"/",den,"=",total/den)

import random

if __name__ == "__main__":
    main()
