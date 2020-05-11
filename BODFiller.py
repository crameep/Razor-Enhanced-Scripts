import re
BOD = Items.FindByID(0x2258,-1,-1)
Hammer = Items.FindByID(0x13E3,0x0000,-1)

i = 0
amountToMake = 0
amountMade = 0
size = "small"
type = 0

craftables = {
  "longsword" : {
    "category" : 4,
    "selection" : 35,
    "id" : 0x0F61
  },
  "viking sword" : {
    "category" : 4,
    "selection" : 39,
    "id" : 0
  },
  "katana" : {
    "category" : 4,
    "selection" : 31,
    "id" : 0x13FF
  },
  "cutlass" : {
    "category" : 4,
    "selection" : 27,
    "id" : 0x1441
  },
  "broadsword" : {
    "category" : 4,
    "selection" : 23,
    "id" : 0x0F5E
  }
}

def moveToBod():
    global typeID
    global amountToMake
    Items.UseItem(BOD)
    Gumps.WaitForGump(1526454082, 10000)
    Gumps.SendAction(1526454082, 2)
    Misc.Pause(1000)
    for x in range(amountToMake):
        Misc.SendMessage("Starting to Add {} to BOD".format(type), 99)
        Misc.SendMessage(typeID)
        itemToMove = Items.FindByID(typeID, -1,-1)
        if itemToMove != None:
            Target.TargetExecute(itemToMove.Serial)
            Misc.Pause(2000)
            amountToMake = amountToMake -1
        else:
            Misc.SendMessage("Start Crafting", 222)
            Craft()
            break
        
    
    
def getBodInfo(BOD):
    global amountToMake
    global amountMade
    global size
    global type
    for x in BOD.Properties:
        #Misc.SendMessage("Propertie: {}".format(x),71)
        line = re.split("([^:]+)",str(x))
        if "amount" in line[1]:
            Misc.SendMessage("Setting the Amount to :{}".format(line[3]),222)
            amountToMake = int(line[3])
        if "small" in str(x):
            size = "small"
            Misc.SendMessage("Size is: {}".format(size), 222)
        if type in str(x):
            Misc.SendMessage("I alread made: {}".format(line[3]),222)
            amountMade = int(line[3])
            amountToMake = amountToMake - amountMade

def findType(BOD):
    global type
    for x in craftables:
        if x in str(BOD.Properties[6]):
            Misc.SendMessage("Type is : {}".format(x),222)
            type = str(x)
            return craftables[x]["id"]

def Craft():
    global typeID
    global type
    global amountToMake
    Misc.SendMessage("Making {} {}".format(amountToMake,type),222)
    for x in range(amountToMake):
        if type in craftables:
            Misc.SendMessage("Crafting {} number {}".format(craftables[type],x),333)
            Items.UseItemByID(Hammer.ItemID)
            Misc.Pause(500)
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, craftables[type]["category"])
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, craftables[type]["selection"])
            Misc.Pause(3000)
        

            
typeID = findType(Items.FindByID(0x2258,-1,-1))           
getBodInfo(BOD)
Misc.SendMessage("I Need to make: {}".format(amountToMake),222)
moveToBod()
Misc.SendMessage(findType(BOD),99)



#if "small" in str(BOD.Properties[3]):
#    name = re.split("([^:]+)",str(BOD.Properties[6]))
#    name = name[1]
#    Misc.SendMessage("I Found a Small Bulk Order Deed: {}".format(name[1]),98)
#    if name in craftables:
#        Misc.SendMessage("I know how to make a {}".format(craftables[name]["selection"]),38)
#        Items.UseItemByID(Hammer.ItemID)
#        Misc.Pause(500)
#        Gumps.WaitForGump(949095101, 10000)
#        Gumps.SendAction(949095101, craftables[name]["category"])
#        Gumps.WaitForGump(949095101, 10000)
#        Gumps.SendAction(949095101, craftables[name]["selection"])
#        



        




