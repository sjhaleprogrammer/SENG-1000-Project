import random
import os


class Game:


    def __init__(self):

        self.inventory = ["raw meat","health potion"]

        self.scenesTypeA = ["You come across a Door"]
        self.scenesTypeB = ['']
        self.scenesTypeC = ['']



    def displayscene(self):

        os.system('cls')        
        scene = self.scenesTypeA[random.randint(0,0)]
        

        print('')
        print('')
        print(f'            {scene}                ')
        print('')
        print('') 
        print('')
        print('')         
        print(f'Your inventory: {self.inventory}')                         



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
            self.displayscene()

        if option == 0:
            exit()
        
        
            


    
    