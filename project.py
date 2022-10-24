list = []

def add():
    x = input()
    list.append(x)
    print(f"{x} has been added to the list")
    

def remove():
    x = input()
    if x in list:
        list.remove(x)
    else:
        print(f"{x} is not in the list")


if __name__ == "__main__":
  
    while True:
        print('===============================================')
        print('Input 0 to exit')
        print('Input 1 to add a variable to the list')
        print('Input 2 to remove a variable from the list ')
        print('Input 3 to display the list')
        print('===============================================')
        print('')
    
        option = int(input())
    
        if option == 1:
            add()
            print(list)
            print('')
        elif option == 2:
            remove()
            print(list)
            print('')
        elif option == 3:
            print(list)
            print('')
        elif option == 0:
            print(list)
            exit()