from game_of_greed import countPoints
# from app.load_rules import getCustomRules

def test_init_countPoints():
  assert countPoints

# non scoring roll should return 0
def test_zilch():
  expected = 0
  actual = countPoints(['2','3','4','6'])
  assert actual == expected

# rolls with various number of 1s should return correct score
def test_ones():

  # 1s not used in set of 3 (or greater) should return correct score
  assert countPoints(['1']) == 100
  assert countPoints( ['1']*2) == 200
  assert countPoints( ['1']*3) == 1000
  assert countPoints(['1']*4) == 2000
  assert countPoints(['1']*5) == 3000
  assert countPoints(['1']*6) == 4000

# rolls with various number of 2s should return correct score
def test_twos():
  assert countPoints(['2']) == 0
  assert countPoints( ['2']*2 ) == 0
  assert countPoints( ['2']*3) == 200
  assert countPoints(['2']*4) == 400
  assert countPoints(['2']*5) == 800
  assert countPoints(['2']*6) == 1200

# rolls with various number of 3s should return correct score
def test_threes():
  assert countPoints(['3']) == 0
  assert countPoints(['3']*2 ) == 0
  assert countPoints(['3']*3) == 300
  assert countPoints(['3']*4) == 600
  assert countPoints(['3']*5) == 1200
  assert countPoints(['3']*6) == 1800

# rolls with various number of 4s should return correct score
def test_fours():
  assert countPoints(['4']) == 0
  assert countPoints(['4']*2 ) == 0
  assert countPoints(['4']*3) == 400
  assert countPoints(['4']*4) == 800
  assert countPoints(['4']*5) == 1600
  assert countPoints(['4']*6) == 2400

# rolls with various number of 5s should return correct score
def test_fives():
  # test_leftover_fives
  assert countPoints(['5']) == 50
  assert countPoints(['5']*2) == 100
  assert countPoints(['5']*3) == 500
  assert countPoints(['5']*4) == 1000
  assert countPoints(['5']*5) == 2000
  assert countPoints(['5']*6) == 3000

# rolls with various number of 6s should return correct score
def test_sixes():
  assert countPoints(['6']) == 0
  assert countPoints(['6']*2) == 0
  assert countPoints(['6']*3) == 600
  assert countPoints(['6']*4) == 1200
  assert countPoints(['6']*5) == 2400
  assert countPoints(['6']*6) == 3600

# 1,2,3,4,5,6 should return correct score
# def test_straight():
#   assert countPoints(['1','2','3','4','5','6']) == 1500
# test_straight

def test_straight():
  straight = ["1","2","3","4","5","6"]
  assert countPoints(straight) == 1111
# test_three_pairs
def test_three_pairs():
  assert countPoints(['1','1','2','2','3','3']) == 2222
# 3 pairs should return correct score
def test_two_trios():
  assert countPoints(['1','1','1','2','2','2']) == 3333
# test_two_trios
# 2 sets of 3 should return correct score

# test_roll
# doing a roll with x number of dice should return sequence of x length random integers between 1 and 6 inclusive