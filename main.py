from game import Game

if __name__ == "__main__":    
    game = Game()

    option = game.menu()

    if option == 1:
        game.battle()

    if option == 0:
        exit()


