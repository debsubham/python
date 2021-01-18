class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return (f"card's value is {self.value} and suit is {self.suit}")





from random import shuffle;

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.cards = []
        # print(Card(value ,suit))
        self.cards = [Card(value,suit) for suit in suits for value in values]
        # print(self.cards)
    
    def __repr__(self):
        return f"Deck of {self.count()} cards"
    def count(self):
        return len(self.cards)
    def _deal(self, num):
        if len(self.cards) == 0 : 
            raise ValueError("No cards available")
        count = self.count()
        actual = min(count,num)
        print(f"Going to remove {actual} cards")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
    
    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self,hand_size):
        return self._deal(hand_size)
    def shuffle(self):
        if self.count() != 52:
            raise ValueError("only full cards can be suffle")
        shuffle(self.cards)
        return ("cards has been shuffled")






card2 = Deck()
print(len(card2.cards))
# card2._deal(20)
# print(len(card2.cards))
# card2._deal(56)
# print(len(card2.cards))
# card2._deal(1)

# card1 = Card("A", "Hearts")


print(card2)

# print(card1)
# # class Deck: