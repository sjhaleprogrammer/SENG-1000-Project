import random

class Player:

    def __init__(self):

        self.inventory = []
        self.health = 100
        self.damage = 0
        self.resistance = 0

    #adds a item (string) to the inventory(list)
    def addtoinventory(self,newitem):
        self.addtoinventory.append(newitem)



    #punch emeny
    def punch(self, enemy):
        enemy.health -= random.randint(16,20)


  
        
    #change all the values of a player at once
    def defBaseValues(self, health, damage, resistance):
        self.health = health
        self.damage = damage
        self.resistance = resistance


    


