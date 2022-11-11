import random

class Emeny:

    def __init__(self):
        
        self.health = 100
        self.damage = 0
        self.resistance = 0

        self.currentemeny = ""
        self.generateNewEmemy()
        #when creating a new emeny object a emeny will be created by default 



    #creates random emeny idea and returns a string
    #TODO add acsii art from a acsii class or something
    def generateNewEmemy(self):
        list = ['Goblin','Bat','Spider','Wolf']
        type = ['Big','Giant','Demon']

        emeny = random.choice(list)

        output = random.choice(type) + " " + emeny

        if emeny == 'Spider':
            pass



        self.currentemeny = output