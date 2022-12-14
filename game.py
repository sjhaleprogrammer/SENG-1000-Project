import time
import random
from player import Player
from enemy import Enemy
from scene import Scene
from item import Item

class Game:


    def __init__(self):

        self.player = Player()
        self.enemy = Enemy()
        self.scene = Scene()

        


    # uses the player, enemy and scene class to create battle 
    def battle(self):

        enemyturn = False

        while self.player.health >= 0:

            if (self.enemy.health <= 0):
                self.scene.clearScreen()
                self.menu()
                self.scene.displaywin()
                return "win"

            # clears the screen
            self.scene.clearScreen()       
        
            self.scene.displaybattle(self.enemy,self.player)

            if enemyturn == False:

                
                print("1) Punch")
                print("2) Inventory")

            
              
                option = int(input())
                

                if option == 1:
                    self.scene.clearScreen()

                    self.scene.displaybattle(self.enemy,self.player)
                
                    #20 percent chance for the enemy to evade attack
                    evadechance = random.randint(0,9)
                    if evadechance == 0 or evadechance == 1:
                        print(f'{self.enemy.currentenemy} evaded the attack !')
                        enemyturn = True
                    else:
                        self.player.punch(self.enemy)
                        enemyturn = True

                if option == 2:

                    if len(self.player.inventory) != 0:
                        self.scene.clearScreen()

                        self.scene.displaybattle(self.enemy,self.player)

                        for count,item in enumerate(self.player.inventory, start=1):
                            print(str(count)+")", item)

                        print("0) Back")
                        option = int(input())
                        if option == 0:
                            continue
                            
                        self.scene.clearScreen()

                        self.scene.displaybattle(self.enemy,self.player)

                        self.player.useItem(self.enemy,self.player.inventory[option-1])
                        enemyturn = True
                    else:
                        self.scene.clearScreen()
                        self.scene.displaybattle(self.enemy,self.player)

                        print("Your inventory is empty...")
                        print("Returning to battle")



            else:
                self.enemy.attack(self.player)
                enemyturn = False

            time.sleep(2.5)

        else:
            self.scene.clearScreen()
            self.player.inventory.clear()
            self.scene.displaydeath()
            self.menu()
            return "lose"

       
            
            
            
    def find(self):

        list = [Item("Damage Potion",random.randint(5,10),ToEnemy=True,desc="Deals 5 to 10 damage to enemy"),
                Item("Health Potion",random.randint(5,10),ToEnemy=False,desc="Heals 5 to 10 damage"),
                Item("Greater Health Potion",random.randint(10,20),ToEnemy=False,desc="Heals 10 to 20 damage")
                ]

        item = random.choice(list)

        self.player.inventory.append(item)

        self.scene.clearScreen()
        self.scene.displayfind(item)
        time.sleep(2.5)
        
        self.menu()

         

    def menu(self):

        self.scene.clearScreen()
        #displays menu
        self.scene.displaymenu()

        
        try:
            option = int(input())
        except:
            print("wrong value")
            self.menu()


        if option == 1:
            self.battle()

        if option == 2:
            self.find()
    
        if option == 0:
            exit()

        
    
        
        
            


    
    