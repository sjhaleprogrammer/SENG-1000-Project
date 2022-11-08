import random
import os
import time
from player import Player
from monsters import Monsters


class Game:


    def __init__(self):

        self.player = Player()
        self.scene = Monsters().generatemonster()



    def displayscene(self):

        while self.player.health != 0:

            os.system('cls')        
        
    
            print('')
            print('')
            print('')
            print('')
            print('')
            print(f'            {self.scene}                ')
            print('')
            print('')
            print('')
            print('')
            print(f' Health:{self.player.health}       ')
            print('')


            print("1 to Fight")
            print("2 to Run")
            

            time.sleep(2.0)

         
                       



    def run(self):

        
        print('')
        print('               Group 2 Project                  ')
        print('                                                ')
        print('------------------------------------------------')
        print('')
        print('               Enter 1 to Play                  ')
        print('                                                ')
        print('               Enter 0 to exit                  ')
        print('')
        print('------------------------------------------------')
        print('')

        option = int(input())

        if option == 1:
            player = Player()
            self.displayscene()

        if option == 0:
            exit()
        
        
            


    
    