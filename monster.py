import random

class Monster:

    def __init__(self):
        
        self.health = 100
        self.damage = 0
        self.resistance = 0

        self.currentmonster = ""
        self.generatenewmonster()
        #when creating a new monster object a monster will be created by default 



    #creates random monster idea and returns a string
    #TODO add acsii art from a acsii class or something
    def generatenewmonster(self):
        list = ['Goblin','Bat','Spider','Wolf']
        type = ['Big','Giant','Demon']

        monster = random.choice(list)

        output = random.choice(type) + " " + monster

        if monster == 'Spider':
            pass



        self.currentmonster = output