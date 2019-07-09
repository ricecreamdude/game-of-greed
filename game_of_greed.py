import random

#dice variables
diceHand = [None] * 6
diceSaved = [None]

#game variables
# Application should keep track of total score
gameScore = 0

# Application should keep track of current round
gameRound = 1

def rollNewDice():
  count = 0
  for (i,v) in enumerate(diceHand):
    diceHand[i] = random.randint(1,6)
    count += 1
  print(f"Rolled {str(count)} new dice")
  print(diceHand)

# Application should allow user to set aside dice each roll
  # Create a function that takes values out of array "Hand" 
  # and adds them to a Aside array

def saveDice():
  global gameScore
  response = input("Would you like to save any die? (y/n)")

  if response == ('y' or 'Y' or 'yes' or 'YES'):
    diceSaved = input("Please enter which dice values you would like to keep:").split()
    for die in diceSaved:
      index = diceHand.index( int(die) )
      diceHand.pop( index )
    gameScore += int( input("How many points is this worth?") )

  elif response == ('n' or 'N' or 'no' or 'NO'):
  # Capture user input and split into an array 
    print('You decide to roll again')  
  # Remove selected values from diceHand
  else:
    response = input("Please enter a valid reponse (y/n)")
  #Python scope is weird

def endgame(gameScore):
    print('Thanks for playing. You scored: ' + str(gameScore) )

#Game Logic

# Application should user to enter score per roll

#One turn consists of the following actions:
  #0. Check if round is =4.  If yes, end game.
  #1. Roll dice 
  #2. Prompt user to save
    #a If yes, prompt user which die to save
    #  Prompt user for score associated for which die to save
  #3. Roll again

while (gameRound<4):
  print('Round ' + str(gameRound) )  
  rollNewDice()
  saveDice()
  gameRound += 1

endgame(gameScore)

