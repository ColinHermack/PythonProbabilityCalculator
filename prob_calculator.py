import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num):
        if num > len(self.contents):
            return self.contents
        drawn = []
        for i in range (num):
            drawn.append(self.contents.pop(random.randint(0, len(self.contents) - 1)))
        return drawn
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    numSuccessful = 0
    drawn = {}
    success = True
    for i in range(num_experiments):
        currHat = copy.deepcopy(hat)
        drawn = {}
        for j in (currHat.draw(num_balls_drawn)):
            if j in drawn.keys():
                drawn[j] += 1
            else:
                drawn[j] = 1
        success = True
        for j in expected_balls.keys():
            if not j in drawn.keys():
                success = False
            elif expected_balls[j] > drawn[j]:
                success = False

        if success:
            numSuccessful += 1
    
    return (float(numSuccessful) / float(num_experiments))