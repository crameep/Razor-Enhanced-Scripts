UnravelID = 0x573C
GrabBag = Items.FindBySerial(0x40F8CB7C)
GrabBagCount = 0
types = ["Jewellery", "Armor", "Shield", "Weapon", "Clothing"]

for unravel in Player.Backpack.Contains:
    if unravel.ItemID == UnravelID:
        
        Misc.SendMessage("Unraveling....", 222)
        Misc.Pause(0)
        for item in GrabBag.Contains:
            typeCount = len(item.Properties)
            index = typeCount - 2
            Misc.SendMessage(typeCount)
            Misc.SendMessage(item.Name)
            if typeCount > 5 and item.Properties[index]!= None:
                search = str(item.Properties[index])
                for x in types:
                    if search.find(x) != -1:
                        if Items.FindBySerial(unravel.Serial) != None:
                                Items.UseItem(unravel.Serial)
                                Misc.Pause(250)
                                Target.TargetExecute(item.Serial)
                                Misc.Pause(500)
                
            
            

