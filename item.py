import random
import time

from enemy import Enemy
from player import Player
class Item:

    def __init__(self):
        self.enemy = Enemy()
        self.player = Player()

    def damage_potion(self,enemy):

        enemy.health -= random.randint(5,10)

        print(f'{self.enemy} now has {enemy.health} health!')

    def health_potion(self, player):

        player.health += random.randint(5,10)

        print(f'{self.player} now has {player.health} health!')

    def greater_health_potion(self, player):

        player.health += random.randint(10,20)

        print(f'{self.player} now has {player.health} health!')

