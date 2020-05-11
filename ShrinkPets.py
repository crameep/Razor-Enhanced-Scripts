
friends = Friend.GetList("pets")
for x in friends:
    petout =  Mobiles.FindBySerial(x)
    if (petout != None):
        Misc.SendMessage("Shrinking...")
        Items.UseItem(0x429C065A)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(x)
        Misc.Pause(500)
        continue
