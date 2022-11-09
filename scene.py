class Scene:


    def __init__(self):

        pass


    #displays the menu TO BE CHANGED    
    def displaymenu(self):
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




    #displays the battle screen TO BE CHANGED
    def displaybattle(self, monster, player):
        print('')
        print('')
        print(f'                 Health:{monster.health}')
        print('')
        print('')
        print(f'         {monster.currentmonster}       ')
        print('')
        print('')
        print('')
        print('')
        print(f' Health:{player.health}                 ')
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
