from random import randint


def create_cards():
    cards = []
    for i in ['S', 'H', 'D', 'C']:
        for j in range(2, 15):
            cards.append(i+str(j))
    return cards


class Deck(object):
    CARDS = create_cards()

    def __init__(self):
        self.cards = self.shuffle_cards()

    def fisher_yates_shuffle(self, cards):
        n = len(cards)
        for i in range(n - 1, 0, -1):
            j = randint(0, i)
            cards[j], cards[i] = cards[i], cards[j]
        return cards

    def shuffle_cards(self):
        cards = self.fisher_yates_shuffle(self.CARDS)
        return cards

    def take(self, num_of_cards):
        return [self.cards.pop(0) for _ in range(num_of_cards)]

    def draw(self, num_of_cards):
        self.cards.pop(0)
        return self.take(num_of_cards)

    def deal(self, num_of_players):
        return list(zip(self.take(num_of_players), self.take(num_of_players)))

    def flop(self):
        return self.draw(3)

    def turn(self):
        return self.draw(1)

    def river(self):
        return self.draw(1)