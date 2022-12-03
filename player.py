import random

class Player:

    def __init__(self):

        self.inventory = []
        self.health = 100
        self.damage = 0
        self.resistance = 0

   
    #punch emeny
    def punch(self, enemy):
        print("Player is now attacking...")
        enemy.health -= random.randint(16,20)


    #uses first item in inventory
    def useItem(self, enemy, item):
        
        if (item.ToEnemy == True):
            print(f"Used {item.name} on the enemy!")
            enemy.health -= int(item.damage)
        else:
            print(f"Used {item.name}")
            self.health += int(item.damage)
        
        self.inventory.remove(item)
        

    #change all the values of a player at once
    def defBaseValues(self, health, damage, resistance):
        self.health = health
        self.damage = damage
        self.resistance = resistance


    


