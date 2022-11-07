

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
            print('------------------------------------------------')
            print('Input 0 to exit')
            print('Input 1 to add a variable to the list')
            print('Input 2 to remove a variable from the list ')
            print('Input 3 to display the list')
            print('------------------------------------------------')
            

            option = int(input())
        
            if option == 1:
                self.add()
                print(self.list)
                print('')
            elif option == 2:
                self.remove()
                print(self.list)
                print('')
            elif option == 3:
                print(self.list)
                print('')
            elif option == 0:
                print(self.list)
                exit()


    
    