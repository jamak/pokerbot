suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
rankList = [ None , None, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
ranklist = dict(zip(rankList,range(20)))
class Card(object):

    def __init__(self, suit=0, rank=2):
        self.suit = suitList[suit]
        self.rank = rankList[rank]

    def __repr__(self):
        return (rankList[self.rank] +" of "+ suitList[self.suit])

    def face(self):
        """return True if it is a Face Card"""
        return self.suit not in {10, "J", "Q", "K", "A"}
