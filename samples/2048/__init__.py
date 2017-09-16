# coding: utf-8

"""
@author: 武明辉 
@time: 17-9-16 下午5:53
"""

import curses

from random import randrange, choice
from collections import defaultdict

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

actions_dict = dict(zip(letter_codes, actions*2))


def get_user_action(kehbord):
    char = 'N'
    while char not in actions_dict:
        char = kehbord.getch()

    return actions_dict[char]

def transpose(field):
    return [list(row) for row in zip(*field)]

def invert(field):
    return [row[::-1] for row in field]

class GameField:
    def __init__(self):
        pass

def main(srdscr):
    def init():
        # 重置棋盘
        return 'Game'

    def not_game(state):
        responses = defaultdict(lambda :state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[actions]

    def game():
        pass

    state_actions = {
        'Init': init,
        'Win': lambda not_game('Win'),
        'GameOver': lambda not_game('GameOver'),
        'Game': game
    }

    while state != 'Exit':
        state = state_actions[state]()


if __name__ == '__main__':
    pass
