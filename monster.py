import random

class Monster:

    def __init__(self):
        self.health = 100


    def generatemonster(self):

        list = ['Goblin','Bat','Spider','Wolf']
        type = ['Big','Giant','Demon']



        return random.choice(type) + " " + random.choice(list)