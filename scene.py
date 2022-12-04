from ascii import Ascii

class Scene:


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

