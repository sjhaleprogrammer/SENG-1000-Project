import random

class Monster:

    def __init__(self):
        self.health = 100



    def generatemonster(self):
        list = ['Goblin','Bat','Spider','Wolf']
        type = ['Big','Giant','Demon']

        monster = random.choice(list)

        output = random.choice(type) + " " + monster

        if monster == 'Spider':
            pass



        return output