import string
import random

class BoggleBoard:
  
  def __init__(self, die=[["_"]*6 for i in range(16)], board=[["_"]*4 for i in range(4)]):
    self.die = die
    self.board = board

  def create_die(self):
    abc = string.ascii_uppercase
    # print(abc)
    for i,k in enumerate(self.die):
      for j,p in enumerate(k):
        rand = random.choice(abc)
        if rand == 'Q':
          self.die[i][j] = 'Qu'
        else:
          self.die[i][j] = rand
    # print(self.die)
    return self.die


  def shake(self):
    abc = string.ascii_uppercase
    side = 0
    for i,k in enumerate(self.board):
      # print(self.die[i])
      # print(rand)
      for j,p in enumerate(k):
        rand = random.choice(self.die[side])
        side += 1
        if rand == 'Q':
          self.board[i][j] = 'Qu'
        else:
          self.board[i][j] = rand
      # print(self.board)
    for i in self.board:
      print(i)
      # print("  ".join(i).center(2))



# print("".join(['W', 'S', 'D', 'V']))
game = BoggleBoard()
# print(game.board)
print(game.create_die())
print("------------------------------------")
game.shake()
