import random

class Enemy:

    def __init__(self):
        
        self.health = 100
        self.damage = 0
        self.resistance = 0

        self.currentemeny = ""
        self.generateNewEnemy()
        #when creating a new enemy object a enemy will be created by default 



    #creates random enemy idea and returns a string
    #TODO add acsii art from a acsii class or something
    def generateNewEnemy(self):
        list = ['Goblin','Bat','Spider','Wolf']
        type = ['Big','Giant','Demon']

        enemy = random.choice(list)

        output = random.choice(type) + " " + enemy
        if enemy == 'Spider':
            pass



        self.currentenemy = output