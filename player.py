class Player:

    def __init__(self):
        self.chips = 1000

        self.hand = {
            'spades':   0,
            'hearts':   0,
            'clubs':    0,
            'diamonds': 0,
        }

    def deal(self, hand):

        for card in hand:
            self.hand[card] += 1
