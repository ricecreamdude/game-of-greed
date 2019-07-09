import random

# Application should simulate rolling between 1 and 6 dice
diceHand = [None] * 6
diceSaved = [None]

def rollNewDice():
  for (i,v) in enumerate(diceHand):
    diceHand[i] = random.randint(1,6)
  print(diceHand)


# Application should allow user to set aside dice each roll
def saveDice():
  # Capture user input and split into an array 
  diceSaved = input("Please enter which dice values you would like to keep:").split()
  # Remove selected values from diceHand
  for die in diceSaved:
    index = diceHand.index( int(die) )
    diceHand.pop( index )
  print(diceHand)


#Game Logic
rollNewDice()
saveDice()


  # Create a function that takes values out of array "Hand" 
  # and adds them to a Aside array


# Application should user to enter score per roll


# Application should allow “banking” current score or rolling again.


# Application should keep track of total score


# Application should keep track of current round
  #Set score to 0
  #

