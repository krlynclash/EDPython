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

def craft(craftItem, craftQ):
    print(craftItem, craftQ)
    return



def startGame():
    #start
    print("##################")
    print("Game Started")
    print("##################")

    continueGame = "y"
    craftTimes = 0

    #main loop
    while (continueGame == "y"):
        craftTimes+=1
        item = str(input("What item do you want to craft? : "))
        q = int(input("How many do you want to craft? : "))
        craft(item, q)
        continueGame = input("Do you want to make another craft? (y/n) : ")
    
    # end game
    print("##################")
    print(f"You crafted {craftTimes} times!")
    print("Game Ended")
    print("##################")

startGame()
