import os
import time
from player import Player
from enemy import Enemy
from scene import Scene

class Game:


    def __init__(self):

        self.player = Player()
        self.enemy = Enemy()
        self.scene = Scene()
        


    # uses the player, enemy and scene class to create battle 
    def battle(self):

        enemyturn = False

        while self.player.health != 0:

            if (self.enemy.health <= 0):
                os.system('clear')
                self.scene.displaywin()
                break

            # clears the screen
            os.system('clear')        
        
            self.scene.displaybattle(self.enemy,self.player)

            if enemyturn == False:
                print("1) Punch")
            
                try:
                    option = int(input())
                except:
                    pass

                if option == 1:
                    os.system('clear')
                    self.scene.displaybattle(self.enemy,self.player)
                    print("Player is now attacking...")

                    self.player.punch(self.enemy)
                    enemyturn = True

            else:
                print(f"{self.enemy.currentenemy} is now attacking...")
                self.enemy.attack(self.player)
                enemyturn = False

            time.sleep(2.5)
        
        else:
            os.system('clear')
            self.scene.displaydeath()
            


         

    def menu(self):

        #displays menu
        self.scene.displaymenu()
        try:
            option = int(input())
        except:
            print("wrong that is not a 1 or 0")
            self.menu()

        return option
    
        
        
            


    
    