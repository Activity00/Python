# coding: utf-8

"""
@author: 武明辉 
@time: 18-9-5 上午11:24

魔术方法in操作与for in 操作
in:
    查询顺序 __contains__  __iter__ __getitem__(执行多次)
for in:     __iter__ __getitem__

"""
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, sult) for sult in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    # if there are no below method the in operate will be sequene search
    # below then __getitem__ method
    # def __contains__(self, item):
    #     print('__contains__')

    # def __iter__(self):
    #     print('__iter__')

    def __getitem__(self, item):
        print('getitem')
        return self._cards[item]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


def test_case():
    import doctest
    doctest.testmod()
    """
    >>> deck = FrenchDeck()
    >>> len(deck)
    52
    >>> deck[1]
    Card(rank='3', suit='spades')
    >>> 
    """
    pass


if __name__ == '__main__':
    deck = FrenchDeck()
    print(len(deck))
    print(deck[1])
    for c in deck:
        print(c)
    print(choice(deck))
    print(deck[3:])
    print(deck[12::13])
    print(Card(rank='3', suit='spades') in deck)
    print(Card(rank='1', suit='spades') in deck)
    print("*****************")
    for card in sorted(deck, key=spades_high):
        print(card)
    d = Card(rank='3', suit='spades')
    print(d in deck)
