import string
import random

class BoggleBoard:
  
  def __init__(self, board=[[]]*4):
    self.board = board

  def shake(self):
    abc = string.ascii_uppercase.replace('Q','Qu')
    print(abc)
    for line in self.board:
      for j in range(len(self.board)):
        rand = random.choice(abc)
        line.append(rand)
      print(self.board)



game = BoggleBoard()
print(game.board)
game.shake()