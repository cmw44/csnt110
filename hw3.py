"""
hw3 by Cameron Wertelka
Ask user to enter suit of card, store as suit
Strip suit, force suit to lower case letters
If suit is "hearts" or suit is "diamonds"
    Print "That card is red"
Else If suit is "clubs" or suit is "spades"
    Print "That card is black."
    Ask user to enter value of card, store as value
Convert value to an integer
"""

suit = input("Enter suit of card: ")
suit = suit.strip().lower()

if (suit == "hearts" or suit == "diamonds"): 
    print("That card is red.")
elif (suit == "clubs" or suit == "spades"):
    print("That card is black.")

card = input("Enter value of card: ")
card = int(card)
if (card == 1):
    print("That has a value of 1 or 11")
elif (card >= 2 and card <= 10):
    print("That has a value of " + str(card))
elif (card >= 11 and card <= 13):
    print("That has a value of 10")
else: print("That card does not exist")
