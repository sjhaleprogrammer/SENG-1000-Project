import random
import os


class Game:


    def __init__(self):
        self.introscenes = ["You come across a Door"]


    def introscene(self):

        os.system('cls')        
        scene = self.list[random.randint(0,0)]
        

        print('')
        print('')
        print(f'            {scene}                ')
        print('')
        print('')                                   



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
            self.introscene()

        if option == 0:
            exit()
        
        
            


    
    