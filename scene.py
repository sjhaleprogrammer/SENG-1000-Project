from ascii import Ascii
import sys
import os



class Scene:

    def clearScreen(self):
        if sys.platform.startswith("linux"):  
            return os.system("Clear")

        if sys.platform == "darwin":
            return os.system("Clear")

        if sys.platform == "win32":
            return os.system("cls")




    #displays the menu TO BE CHANGED    
    def displaymenu(self):
        print('')
        print('               Group 2 Project                  ')
        print('                                                ')
        print('------------------------------------------------')
        print('')
        print('                  1) Battle                      ')
        print('')
        print('                  2) Find                        ')
        print('                                                 ')
        print('                  0) Quit                        ')
        print('')
        print('-------------------------------------------------')
        print('')



    #displays the battle screen TO BE CHANGED
    def displaybattle(self, enemy, player):
        print('')
        print(f'                 HP:{enemy.health}')
        print('')
        print(f'      {enemy.currentenemy}       ')
        print('')
        if ("Spider" in enemy.currentenemy):
            Ascii.Spider()
        elif("Skeleton" in enemy.currentenemy):
            Ascii.Skeleton()
        elif("Goblin" in enemy.currentenemy):
            Ascii.Goblin()
        elif ("Wolf" in enemy.currentenemy):
            Ascii.Wolf()
        elif ("Bat" in enemy.currentenemy):
            Ascii.Bat()
        print('')
        print(f' HP:{player.health}                 ')
        print('')


    

    #displays the death screen TO BE CHANGED
    def displaydeath(self):
        print('')
        print('')
        print('')
        print('')
        print('')
        print(f'         You are dead                          ')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')

    

    #displays the death screen TO BE CHANGED
    def displaywin(self):
        print('')
        print('')
        print('')
        print('')
        print('')
        print(f'          You won !                        ')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
    

   
    def displayfind(self,item):
        print('')
        print('')
        print('')
        print('')
        print('')
        print(f'        "You have found {item}"          ')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')

