import random

class Monsters:

    def __init__(self):

        pass


    def generatemonster(self):

        list = ['Goblin','Bat','Spider','Wolf']
        type = ['Big','Giant','Demon']



        return random.choice(type) + " " + random.choice(list)