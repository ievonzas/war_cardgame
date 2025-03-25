import random

class Suits:

    SYMBOLS = {"clubs": "♣", "diamonds":"♦", "hearts" : "♥", "spades" : "♠"}
    def __init__(self, description):
            self._description = description
            self._symbol = Suits.SYMBOLS[description.lower()]
    
    # getter for description
    @property
    def description (self):
          return self._description
    
    # getter for symbol

    @property
    def symbol(self):
          return self._symbol
