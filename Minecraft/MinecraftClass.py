
#this is a class
class MineCraftGame:
    #constructor
    def __init__(self, name):
        self.WOOD = "wood"
        self.PLANK = "plank"
        self.TABLE = "table"
        self.STICK = "stick"
        self.FENCE = "fence"

        self.SWORD = "sword"
        self.SHOVEL = "shovel"
        self.HOE = "hoe"
        self.AXE = "axe"
        self.BOWL = "bowl"

        self.VALIDITEMS = [self.WOOD, self.PLANK, self.TABLE, self.STICK, self.SWORD, self.SHOVEL, self.HOE, self.AXE, self.FENCE, self.BOWL]

        self.inventory = [self.WOOD]*32

        self.name = name

    # print cheat cheat
    def printrecipe(self):
        print(
            """
            1 wood = 4 planks
            1 plank = 2 sticks
            4 planks = 1 crafting table

            1 stick + 2 plank = 1 sword
            2 sticks + 1 plank = 1 shovel
            2 sticks + 2 planks = 1 hoe
            2 sticks + 3 planks = axe

            2 sticks + 4 planks = fence
            3 planks = 4 bowl
            """
        )

    def craft(self, craftItem, craftQ):
        if (craftItem in self.VALIDITEMS):
            if (craftItem == self.WOOD):
                pass        

            elif (craftItem == self.PLANK):
                print(f"You need {craftQ/4} wood")
                #what if craftQ = 6?????????
                #6/4 = 1.5
                materialneededQ = craftQ//4
                newCraftedItemQ = materialneededQ*4
                self.updateInventory(newCraftedItemQ, craftItem, materialneededQ, self.WOOD)

            elif (craftItem == self.STICK):
                print(f"You need {craftQ/2} plank")
                #what if craftQ = 3?
                # 3/2 = 1.5
                materialneededQ = craftQ//2
                newCraftedItemQ = materialneededQ*2
                self.updateInventory(newCraftedItemQ, craftItem, materialneededQ, self.PLANK)

            elif (craftItem == self.TABLE):
                print(f"You need {craftQ*4} plank")
                self.updateInventory(craftQ, craftItem, craftQ*4, self.PLANK)


            elif (craftItem == self.SWORD):
                print(f"You need {craftQ} stick {craftQ*2} plank")
                self.updateInventory(craftQ, craftItem, craftQ, self.STICK, craftQ*2, self.PLANK)

            elif (craftItem == self.SHOVEL):
                print(f"You need {craftQ*2} stick {craftQ} plank")
                self.updateInventory(craftQ, craftItem, craftQ*2, self.STICK, craftQ, self.PLANK)

            elif (craftItem == self.HOE):
                print(f"You need {craftQ*2} stick {craftQ*2} plank")
                self.updateInventory(craftQ, craftItem, craftQ*2, self.STICK, craftQ*2, self.PLANK)
            
            elif (craftItem == self.AXE):
                print(f"You need {craftQ*2} stick {craftQ*3} plank")
                self.updateInventory(craftQ, craftItem, craftQ*2, self.STICK, craftQ*3, self.PLANK)
            
            elif (craftItem == self.FENCE):
                print(f"You need {craftQ*2} stick {craftQ*4} plank")
                self.updateInventory(craftQ, craftItem, craftQ*2, self.STICK, craftQ*4, self.PLANK)
            elif (craftItem == self.BOWL):
                print(f"You need {craftQ/4} plank")
                self.updateInventory(craftQ, craftItem, craftQ/4, self.BOWL)
        else:
            print("This is NOT a valid item")
        return


    def updateInventory(newCraftedItemQ, newCraftedItem, materialNeededQ1, materialNeeded1, materialNeededQ2, materialNeeded2):
        """
        craftQIn : this is referring to the item quantity that you want to craft
        craftQOut : this is referring to the item quantity that you will use to craft
        itemRemove : this is the item name that you need to use to craft
        itemAppend : this is the item name that you want to craft
        """
        #thid while loop handles the newly crafted item
        count = 0
        while count < newCraftedItemQ:
            inventory.append(newCraftedItem)
            count+= 1

        # this while loop handles the first set of materials needed 
        count = 0
        while count < materialNeededQ1:
            inventory.remove(materialNeeded1)
            count += 1

        #this while loop handles the SECOND set of material needed
        count = 0
        while count < materialNeededQ2:
            inventory.remove(materialNeeded2)
            count+= 1


    def checkInventory():
        result = {}
        for item in inventory:
            if item in result:
                result[item] += 1
            else:
                result[item] = 1
        return result


    def startGame():
        #start
        print("##################")
        print("welcome " + self.name)
        print("Game Started")
        print(f"Current inventory: {checkInventory()}")
        print("##################")

        continueGame = "y"
        craftTimes = 0

        #main loop
        while (continueGame == "y"):
            craftTimes+=1
            item = str(input(f"What item do you want to craft? {VALIDITEMS} : "))
            q = int(input("How many do you want to craft? : "))
            craft(item, q)
            print(f"Current inventory: {checkInventory()}")
            continueGame = input("Do you want to make another craft? (y/n) : ")
        
        # end game
        print("##################")
        print(f"You crafted {craftTimes} times!")
        print(f"Current inventory: {checkInventory()}")
        print("Game Ended")
        print("##################")

