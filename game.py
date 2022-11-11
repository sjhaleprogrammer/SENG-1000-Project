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

        while self.player.health != 0:
            
            # clears the screen
            os.system('cls')        
        
            self.scene.displaybattle(self.enemy,self.player)
            
            #to be changed 
            print("1 to Fight")
            print("2 to Run")
            
            try:
                option = int(input())
            except:
                pass

            if option == 1:
                #TODO create battle function in player.py
                pass

            if option == 0:
                #TODO create battle function in player.py
                pass


            time.sleep(2.0)
        

        else:

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
        
        
            


    
    