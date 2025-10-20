#Cheat Chear
"""
1 wood = 4 planks
1 plank = 2 sticks
4 planks = 1 crafting table

1 stick + 2 plank = 1 sword
2 sticks + 1 plank = 1 shovel
2 sticks + 2 planks = 1 hoe
2 sticks + 3 planks = axe
"""

def startGame():
    #start
    print("##################")
    print("Game Started")
    print("##################")

    continueGame = "y"

    #main loop
    while (continueGame == "y"):
        print("Game continued")
        continueGame = input("Continue another game? (y/n) : ")
    
    # end game
    print("##################")
    print("Game Ended")
    print("##################")

startGame()
