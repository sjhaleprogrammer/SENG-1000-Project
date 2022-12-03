from player import Player
from enemy import Enemy
import random

class Item:

    def __init__(self,name="",damage=0,player = Player(),enemy = Enemy(),ToEnemy=False,desc=""):
        self.name = name
        self.damage = damage
        self.ToEnemy = ToEnemy
        self.desc = desc
        

   
        
    def __str__(self):
        return f"{self.name}, {self.desc}"




    #def damage_potion(self,enemy):

        #enemy.health -= random.randint(5,10)

        #print(f'{self.enemy} now has {enemy.health} health!')

    #def health_potion(self, player):

        #player.health += random.randint(5,10)

        #print(f'{self.player} now has {player.health} health!')

    #def greater_health_potion(self, player):

       #player.health += random.randint(10,20)

        #print(f'{self.player} now has {player.health} health!')

