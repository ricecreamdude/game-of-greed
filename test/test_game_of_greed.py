from app.game_of_greed import countPoints

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
  assert countPoints( ['1','1'] ) == 200
  assert countPoints( ['1','1','1']) == 1000
  assert countPoints(['1']*4) == 2000
  assert countPoints(['1']*5) == 3000
  assert countPoints(['1']*6) == 4000

# rolls with various number of 5s should return correct score
def test_fives():
  # test_leftover_fives
  assert countPoints(['5']) == 50
  assert countPoints( ['5']*2 ) == 100
  assert countPoints( ['5']*3) == 500
  assert countPoints(['5']*4) == 1000
  assert countPoints(['5']*5) == 2000
  assert countPoints(['5']*6) == 3000

# test_twos
# rolls with various number of 2s should return correct score
# test_threes
# rolls with various number of 3s should return correct score
# test_fours
# rolls with various number of 4s should return correct score
# test_sixes
# rolls with various number of 6s should return correct score
# test_straight
# 1,2,3,4,5,6 should return correct score
# test_three_pairs
# 3 pairs should return correct score

# test_two_trios
# 2 sets of 3 should return correct score
# test_roll
# doing a roll with x number of dice should return sequence of x length random integers between 1 and 6 inclusive