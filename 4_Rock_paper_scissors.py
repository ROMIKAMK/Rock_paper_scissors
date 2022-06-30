#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Hp
#
# Created:     23-06-2022
# Copyright:   (c) Hp 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def play():
    user = input("What's your choice?? 'r' for Rock , 'p' for Paper , 's' for Scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It is a tie'
    # Rule: r>s, s>p, p>r
    if is_win(user,computer):
        return 'You won!!'

    return 'You lost!'


def is_win(player, opponent):
    #returns true if the player wins
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
    or (player == 'p' and opponent == 'r' ):

        return True



print(play())





