ChainmailBook = 0x41B9DEC6
WeaponBook = 0x41B9DA66
RingmailBook = 0x41B9DEC6
PlateBook = 0x41B9DA5B

index = 6

filters = {
  "chainmail" : ChainmailBook,
  "ringmail" : RingmailBook,
  "norse" : PlateBook,
  "katana": WeaponBook,
  "maul": WeaponBook,
  "axe": WeaponBook,
  "scimitar" : WeaponBook,
  "plate" : PlateBook,
  "sword" : WeaponBook,
  "halberd" : WeaponBook,
  "bardiche" : WeaponBook,
  "hammer" : WeaponBook,
  "buckler" : WeaponBook,
  "kryss" : WeaponBook,
  "shield" : WeaponBook,
  "mace" : WeaponBook,
  "spear" : WeaponBook,
  "helmet" : PlateBook,
  "cutlass" : WeaponBook,
  "dagger" : WeaponBook,
  "bascinet" : WeaponBook,
  "fork" : WeaponBook,
}
while Items.FindByID(0x2258,-1,-1) != None:
    find = Items.FindByID(0x2258,-1,-1)
    type = find.Properties[index]
    
    for x,y in filters.items():
        if "amount" in str(type):
            index = index+1
            Misc.SendMessage("Amount Found in String next index is {}".format(index))
            break
        elif x in str(type):
            Misc.SendMessage("Sending {} to {} Book".format(str(type), y))
            Items.Move(find.Serial, y, 0)
            index = 6
            break
        else:
            Misc.SendMessage(type)
            Misc.Pause(0)
            
      
    Misc.Pause(1000)

#Misc.SendMessage(find.Properties[6])
#if "chainmail" in type:
#    Misc.SendMessage("Send to Chainmail Book")
#    Items.Move(find.Serial, ChainmailBook, 0)
#    
    
 