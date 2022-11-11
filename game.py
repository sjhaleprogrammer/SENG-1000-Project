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

            # clears the screen
            os.system('cls')        
        
            self.scene.displaybattle(self.enemy,self.player)

            if enemyturn == False:
                print("1) Punch")
            
                try:
                    option = int(input())
                except:
                    pass

                if option == 1:
                    self.player.punch(self.enemy)
                    enemyturn = True

            else:
                print("Enemy is now attacking !")
                self.enemy.attack(self.player)
                enemyturn = False

            time.sleep(1.5)
        
        else:
            os.system('cls')  

            self.scene.displaydeath()



         

    def run(self):

        #displays menu
        self.scene.displaymenu()

      
        try:
            option = int(input())
        except:
            print("wrong that is not a 1 or 0")
            self.run()

        if option == 1:
            self.battle()

        if option == 0:
            exit()
        
        
            


    
    