class Scene:


    #displays the menu TO BE CHANGED    
    def displaymenu(self):
        print('')
        print('               Group 2 Project                  ')
        print('                                                ')
        print('------------------------------------------------')
        print('')
        print('                  1) Play                          ')
        print('                                                ')
        print('                  0) Quit                          ')
        print('')
        print('------------------------------------------------')
        print('')



    #displays the battle screen TO BE CHANGED
    def displaybattle(self, enemy, player):
        print('')
        print('')
        print(f'                 Health:{enemy.health}')
        print('')
        print('')
        print(f'         {enemy.currentenemy}       ')
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
    






