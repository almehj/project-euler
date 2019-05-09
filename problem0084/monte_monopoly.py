#!/usr/bin/env python3

import sys
import random
import getopt
import logging

# Global data
max_doubles = 2

# Module setup
board_map = []
with open("map.txt","r") as map_file:
    for line in map_file:
        line = line.strip()
        if line != "":
            board_map.append(line)

jail_ndx = board_map.index("JAIL")

# Card (Chance/Community Chest) handlers
def blank(n):
    return n

def goto_go(n):
    return 0

def goto_jail(n):
    return jail_ndx

def goto_name(name):
    return board_map.index(name)

def goto_C1(n):
    return goto_name('C1')

def goto_E3(n):
    return goto_name('E3')

def goto_H2(n):
    return goto_name('H2')

def goto_R1(n):
    return goto_name('R1')

def goto_next_foo(n,c):
    while board_map[n][0] != c:
        n = (n+1)%len(board_map)
    return n

def goto_next_rr(n):
    return goto_next_foo(n,'R')

def goto_next_util(n):
    return goto_next_foo(n,'U')

def goto_3back(n):
    return (n-3)%len(board_map)

chance_deck = [
    goto_go,
    goto_jail,
    goto_C1,
    goto_E3,
    goto_H2,
    goto_R1,
    goto_next_rr,
    goto_next_rr,
    goto_next_util,
    goto_3back,
    blank,
    blank,
    blank,
    blank,
    blank,
    blank
    ]
chance_ndx = 0
random.shuffle(chance_deck)

community_deck = [
    goto_go,
    goto_jail,
    blank,
    blank,
    blank,
    blank,
    blank,
    blank,
    blank,
    blank,
    blank,
    blank,
    blank,
    blank,
    blank,
    blank
    ]
community_ndx = 0
random.shuffle(community_deck)

handler_names = {
    goto_jail:"Go To Jail",
    goto_go:"Advance to Go",
    goto_C1:"Go to C1",
    goto_E3:"Go to E3",
    goto_H2:"Go to H2",
    goto_R1:"Go to R1",
    goto_next_rr:"Advance to Next RR",
    goto_next_util:"Advance to Next Utility",
    goto_3back:"Go Back Three Spaces",
    blank:"Blank Card"
    }   

# Square handlers
def null_handler(n):
    return n

def chance_handler(n):
    global chance_ndx
    card = chance_deck[chance_ndx]
    logging.debug("      Drew %s"%(handler_names[card]))
    chance_ndx = (chance_ndx+1)%len(chance_deck)

    return card(n)

def community_handler(n):
    global community_ndx
    card = community_deck[community_ndx]
    logging.debug("      Drew %s"%(handler_names[card]))
    community_ndx = (community_ndx+1)%len(community_deck)

    return card(n)

handler_names[null_handler] = "Nothing",
handler_names[chance_handler] = "Chance",
handler_names[community_handler] = "Community Chest",

square_handler_map = {
    'CC1':community_handler,
    'CC2':community_handler,
    'CC3':community_handler,
    'CH1':chance_handler,
    'CH2':chance_handler,
    'CH3':chance_handler,
    'G2J':goto_jail
    }


def next_ndx(curr_ndx,n):
    return (curr_ndx + n)%len(board_map)

def resolve(ndx):
    prev_ndx = -1

    while ndx != prev_ndx:
        name = board_map[ndx]
        logging.debug("   Moving to %s"%(name))
        handler = square_handler_map.get(name,null_handler)
        logging.debug("    Square handler: %s"%(handler_names[handler]))
        prev_ndx = ndx
        ndx = handler(ndx)

    return ndx
    
def advance(curr_ndx,n):
    logging.debug(" Moving %d spaces"%n)
    return resolve(next_ndx(curr_ndx,n))

# Returns n rolls of a d-sided die
def get_roll(n,d):
    return [random.randint(1,d) for i in range(n)]

# Main loop: run a number of trials and report occurances
# of landing squares
def run_trials(n_trials,n_sides):
    
    occurs = [0]*len(board_map)
    curr_ndx = 0
    n_doubles = 0
    
    for i in range(n_trials):
        roll = get_roll(2,n_sides)
        is_doubles = roll[0] == roll[1]
        if is_doubles:
            n_doubles += 1
        else:
            n_doubles = 0

            
        logging.debug("Rolled %d,%d == %d"%
              (roll[0],roll[1],sum(roll)))
        if is_doubles:
            logging.debug("    DOUBLES (%d)"%(n_doubles))


        # Advance        
        if n_doubles > max_doubles:
            logging.debug("    JAIL!")
            curr_ndx = jail_ndx
            n_doubles = 0
        else:
            d_ndx = sum(roll)
            curr_ndx = advance(curr_ndx,d_ndx)

        occurs[curr_ndx] += 1
        logging.debug(" Finally landed on %s (%s occurs so far)"%
              (board_map[curr_ndx],occurs[curr_ndx]))

    return occurs

def report_stats(occurs):
    n_samps = sum(occurs)

    ranks = [(n,i) for i,n in enumerate(occurs)]
    ranks.sort(reverse=True)
    
    for n,i in ranks:
        name = board_map[i]
        p = (n/n_samps)*100.

        print("%2d: %4s: %5d (%.2f%%)"%(i,name,n,p))

    
        
def main():

    logging.basicConfig(level=logging.INFO)
    
    d = int(sys.argv[1])
    n = int(sys.argv[2])

    occurs = run_trials(n,d)
    report_stats(occurs)
    
if __name__ == "__main__":
    main()
