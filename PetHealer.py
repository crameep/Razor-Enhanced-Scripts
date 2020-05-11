while True:
    if Misc.ReadSharedValue("HealPet2") == True:
        Misc.SendMessage(Misc.CheckSharedValue("HealPet2"))
        Misc.SendMessage("Healing Piglet",222)
        Items.UseItem(0x401BE8B4)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(0x1051A3)
        Misc.Pause(11000)
    else:
        Misc.SendMessage("Healing Kanga",222)
        Items.UseItem(0x401BE8B4)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(0x00DE80)
        Misc.Pause(11000)

