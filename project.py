from menu import Menu


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


#def pickup

#def comsume 








if __name__ == "__main__":
  
    while True:
        Menu().display()

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