import random
from load_rules import getCustomRules

#dice variables
custom_rules = getCustomRules()
diceHand = [None] * 6
diceSaved = [None]

#game variables
# Application should keep track of total score
gameScore = 0

# Application should keep track of current round
gameRound = 1

def rollNewDice():
  count = 0
  for (i, v) in enumerate(diceHand):
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
    print(diceSaved)
    for die in diceSaved:
      index = diceHand.index( int(die) )
      diceHand.pop( index )
      gameScore += int( input("How many points is this worth?") )

  if response == ('n' or 'N' or 'no' or 'NO'):
  # Capture user input and split into an array 
    print('You decide to roll again')  
  # Remove selected values from diceHand
  else:
    response = input("Please enter a valid reponse (y/n)")
  #Python scope is weird

def endgame():
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

def createDiceTallyDictionary(list):
  newDist = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
  }
  for x in list:
    newDist[ int(x) ] += 1
  return newDist

def countPoints(list):

  pointsEarned = 0

  diceTally = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
  }

  pairCounter = 0
  tripleCounter = 0

  straight = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1}

  for x in list:
    diceTally[ int(x) ] += 1

  #for value of dice(1-6), count of times rolled
  #calculate points for single values
  for value,count in diceTally.items():
    # ONES
    if count == 2:
      pairCounter += 1
    if count == 3:
      tripleCounter += 1
    if value == 1:
      if (count == 1 or count == 2):
        pointsEarned += 100*count
      if count == 3:
        pointsEarned = 1000
      if count == 4:
        pointsEarned = 2000
      if count == 5:
        pointsEarned = 3000
      if count == 6:
        pointsEarned = 4000
  
    if value == 2:
      if count == 3:
        pointsEarned = 200
      if count == 4:
        pointsEarned = 400
      if count == 5:
        pointsEarned = 800
      if count == 6:
        pointsEarned = 1200

    if value == 3:
      if count == 3:
        pointsEarned = 300
      if count == 4:
        pointsEarned = 600
      if count == 5:
        pointsEarned = 1200
      if count == 6:
        pointsEarned = 1800

    if value == 4:
      if count == 3:
        pointsEarned = 400
      if count == 4:
        pointsEarned = 800
      if count == 5:
        pointsEarned = 1600
      if count == 6:
        pointsEarned = 2400

    if value == 5:
      if count == 1 or count == 2:
        pointsEarned += 50*count
      if count == 3:
        pointsEarned = 500 
      if count == 4:
        pointsEarned = 1000
      if count == 5:
        pointsEarned = 2000
      if count == 6:
        pointsEarned = 3000

    if value == 6:
      if count == 3:
        pointsEarned = 600 
      if count == 4:
        pointsEarned = 1200
      if count == 5:
        pointsEarned = 2400
      if count == 6:
        pointsEarned = 3600 

  # check for special hands
  if diceTally == straight:
    pointsEarned = 1500 

  if pairCounter == 3:
    pointsEarned = 1000

  if tripleCounter == 2:
    pointsEarned = 2000

  return pointsEarned

if __name__ == "__main__":
  while (gameRound < 4):
    print('Round ' + str(gameRound) )  
    rollNewDice()
    saveDice()
    gameRound += 1