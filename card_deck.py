from random import randint

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __repr__(self):
        return(f'{self.rank}({self.value}) of {self.suit} ' )

class Deck:
    def __init__(self):
        self.contents = []
        self.construct_deck()
    
    def construct_deck(self):
        suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']

        for suit in suits:
            for value in range (1,14):
                rank = ""

                if value == 1:
                    rank = 'Ace'
                elif value > 1 and value < 11:
                    rank = str(value)
                elif value == 11:
                    rank = "Jack"
                elif value == 12:
                    rank = 'Queen'
                else:
                    rank = 'King'

                self.contents.append(Card(suit,rank,value))
        return self

    def shuffle_deck(self):
        for i in range(0, len(self.contents)):
            x = randint(0, len(self.contents )-1)
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i]
        return self

    def draw_card(self):
        return self.contents.pop()

    def print_deck(self):
        for card in self.contents:
            print(card)
        return self


myDeck = Deck()
myDeck.shuffle_deck()
print(myDeck.draw_card())