

class Game:


    def __init__(self):
        self.list = []
    

    def add(self):
        x = input()
        self.list.append(x)
        print(f"{x} has been added to the list")
        

    def remove(self):
        x = input()
        if x in list:
            self.list.remove(x)
        else:
            print(f"{x} is not in the list")


    def run(self):

        while True:
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
                pass

            if option == 0:
                exit()
            
        
            


    
    