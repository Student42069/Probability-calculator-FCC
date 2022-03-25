import copy
import random
# Consider using the modules imported above.
from collections import Counter

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, number):
    if number > len(self.contents):
      return self.contents
    
    drawned = []
    # temp = self.contents[:]
    # for i in range(number):
    #   element = temp[random.randrange(0, len(temp))]
    #   drawned.append(element)
    #   temp.remove(element)
    
    for i in range(number):
      element = self.contents[random.randrange(0, len(self.contents))]
      drawned.append(element)
      self.contents.remove(element)
      
    return drawned
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = num_experiments
  for i in range(num_experiments):
    hatt = copy.deepcopy(hat)
    drawned = Counter(hatt.draw(num_balls_drawn))
    for key, value in expected_balls.items():
      if not (drawned.get(key, 0) >= value):
        m -= 1
        break
  return m/num_experiments