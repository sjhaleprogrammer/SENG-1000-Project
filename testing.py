#This file is to test code before it is implemented
import random
from enemy import Enemy
#This is a rough damage system
testDamage = random.randint(0,100)
testHealth = 100
testResistance = random.randint(0,100)
if testResistance > 80:
    testResistance = 80
def fightTest():
    print(testResistance, testDamage, testHealth)
    factored_damage = testDamage * ((100-testResistance)/100)
    health_difference = testHealth - factored_damage
    print(health_difference)
fightTest()