# HigherOrLower
import random


# Card constants

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9',
'10', 'Jack', 'Queen', 'King')
NCARDS = 8


# Pass in a deck and this function returns a random card fromthe deck
def getCard(deckListIn):
 thisCard = deckListIn.pop() # pop one off the top of thedeck and return
 return thisCard
# Pass in a deck and this function returns a shuffled copy ofthe deck 
def shuffle(deckListIn):
 deckListOut = deckListIn.copy() # make a copy of thestarting deck
 random.shuffle(deckListOut)
 return deckListOut