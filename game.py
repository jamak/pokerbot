from random import shuffle
from cards import Card
from hand import Hand

for i in xrange(4):
    royal_flush = [Card(i, 10 + p) for p in xrange(5)]

class Deck(object):
    """A standard deck of cards"""
    def __init__(self):
        self.clubs = {Card(0, k) for k in xrange(13)}
        self.diamonds = {Card(1, k) for k in xrange(13)}
        self.hearts = {Card(2, k) for k in xrange(13)}
        self.spades = {Card(3, k) for k in xrange(13)}
        self.all_cards =  list(self.clubs | self.diamonds | self.hearts | self.spades)

    def yshuffle(self):
        """shuffles the deck"""
        shuffle(self.all_cards)


class Player(object):
    """one holdem player"""
    def __init__(self, hand, money):
        self.hand = hand
        self.money = money

    def take_action(self):
        """raises, bets or folds based on given information"""
        pass
