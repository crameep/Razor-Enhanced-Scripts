
SandID = 0x11EA
GoldID = 0x0EEF

BolaID = 0x0000 #Find ID of Bolas

for gold in Player.Backpack.Contains:
    if gold.ItemID == GoldID:
        Items.MoveOnGround(gold.Serial,0,Player.Position.X+1,Player.Position.Y+1,Player.Position.Z+1)
        Misc.SendMessage("Moving Gold", 222)
        Misc.Pause(1000)
        
for sand in Player.Backpack.Contains:
    if sand.ItemID == SandID:
        Items.MoveOnGround(sand.Serial,0,Player.Position.X+1,Player.Position.Y+1,Player.Position.Z+1)
        Misc.SendMessage("Moving Sand", 222)
        Misc.Pause(1000)

    
