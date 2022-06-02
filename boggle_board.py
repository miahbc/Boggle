import string
import random

class BoggleBoard:
  
  def __init__(self, board=[["_"]*4 for i in range(4)])):
    self.board = board

  def shake(self):
    abc = string.ascii_uppercase
    print(abc)
    for i,k in enumerate(self.board)
      for j,p in enumerate(k):
        rand = random.choice(abc)
        self.board[i][j] = rand
      print(self.board)



game = BoggleBoard()
print(game.board)
game.shake()
