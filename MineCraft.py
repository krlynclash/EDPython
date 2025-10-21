#Cheat Cheat
"""
1 wood = 4 planks
1 plank = 2 sticks
4 planks = 1 crafting table

1 stick + 2 plank = 1 sword
2 sticks + 1 plank = 1 shovel
2 sticks + 2 planks = 1 hoe
2 sticks + 3 planks = axe
"""

#global
WOOD = "wood"
PLANK = "plank"
TABLE = "table"
STICK = "stick"

SWORD = "sword"
SHOVEL = "shovel"
HOE = "hoe"
AXE = "axe"

VALIDITEMS = [WOOD, PLANK, TABLE, STICK, SWORD, SHOVEL, HOE, AXE]



def craft(craftItem, craftQ):
    if (craftItem in VALIDITEMS):
        if (craftItem == WOOD):
            pass
        elif (craftItem == PLANK):
            print(f"You need {craftQ/4} wood")
        elif (craftItem == STICK):
            print(f"You need {craftQ/2} plank")
        elif (craftItem == TABLE):
            print(f"You need {craftQ*4} plank")
        elif (craftItem == SWORD):
            print(f"You need {craftQ} stick {craftQ*2} plank")
        elif (craftItem == SHOVEL):
            print(f"You need {craftQ*2} stick {craftQ} plank")
        elif (craftItem == HOE):
            print(f"You need {craftQ*2} stick {craftQ*2} plank")
        elif (craftItem == AXE):
            print(f"You need {craftQ*2} stick {craftQ*3} plank")
    else:
        print("This is NOT a valid item")
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
        item = str(input(f"What item do you want to craft? {VALIDITEMS} : "))
        q = int(input("How many do you want to craft? : "))
        craft(item, q)
        continueGame = input("Do you want to make another craft? (y/n) : ")
    
    # end game
    print("##################")
    print(f"You crafted {craftTimes} times!")
    print("Game Ended")
    print("##################")

startGame()