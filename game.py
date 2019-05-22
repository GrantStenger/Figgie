# Import Dependencies
import random
from player import Player

class Game:

    def __init__(self):

        # Create each of the four players
        self.player1 = Player()
        self.player2 = Player()
        self.player3 = Player()
        self.player4 = Player()
        self.players = [self.player1, self.player2, self.player3, self.player4]

        # Set the initial pot to zero
        self.pot = 0

        # Choose which suits to be common and goal and initialize the deck
        self.choose_deck()

        # Given the new deck, deal each player 10 cards randomly
        self.deal_cards()

        # Output info
        print("Deck:", self.deck)
        print("Common Suit:", self.common_suit)
        print("Goal Suit:", self.goal_suit)
        print("Small Suit:", self.small_suit)

        for player in self.players:
            print(player.hand)

    def choose_deck(self):
        """
        Create a deck object with one random common suit and a separete random
        short suit. The goal suit will be the suit of the same color as the
        common suit.
        """

        # For ease, create a deck of 10 cards per suit (will override two suits)
        self.deck = {
            'spades': 10,
            'hearts': 10,
            'clubs': 10,
            'diamonds': 10,
        }

        # Select two random suits
        suits = ['spades', 'hearts', 'clubs', 'diamonds']
        two_suits = random.sample(suits, k=2)

        # Assign one random suit to be the common and one to be the small suit
        self.common_suit = two_suits[0]
        self.small_suit = two_suits[1]

        # Correct these values in the deck dictionary
        self.deck[self.common_suit] = 12
        self.deck[self.small_suit] = 8

        # Define the goal suit as the same color as the goal suit
        if self.common_suit == "spades":
            self.goal_suit = "clubs"
        elif self.common_suit == "hearts":
            self.goal_suit = "diamonds"
        elif self.common_suit == "clubs":
            self.goal_suit = "spades"
        else:
            self.goal_suit = "hearts"

    def deal_cards(self):

        ordered_deck = []

        for suit in self.deck:
            for _ in range(self.deck[suit]):
                ordered_deck.append(suit)

        random.shuffle(ordered_deck)

        for player in self.players:
            hand = ordered_deck[:10]
            player.deal(hand)
            ordered_deck = ordered_deck[10:]

    def play_round(self):

        # Players Ante
        for player in self.players:
            player.chips -= 50
            self.pot += 50
