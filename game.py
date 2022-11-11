import os
import time
from player import Player
from emeny import Emeny
from scene import Scene

class Game:


    def __init__(self):

        self.player = Player()
        self.emeny = Emeny()
        self.scene = Scene()
        


    # uses the player, emeny and scene class to create battle 
    def battle(self):

        while self.player.health != 0:
            
            # clears the screen
            os.system('cls')        
        
            self.scene.displaybattle(self.emeny,self.player)
            
            #to be changed 
            print("1 to Fight")
            print("2 to Run")
            

            time.sleep(2.0)

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
        
        
            


    
    