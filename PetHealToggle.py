if Misc.CheckSharedValue("HealPet2"):
    Misc.SetSharedValue("HealPet2", not(Misc.ReadSharedValue("HealPet2")))
    Misc.SendMessage("Heal Pet 2: {}".format(Misc.ReadSharedValue("HealPet2")),222)
else:    
    Misc.SetSharedValue("HealPet2", False)
    Misc.SendMessage("Heal Pet 2: {}".format(Misc.ReadSharedValue("HealPet2")),222)
Items.UseItem(0x401BE8B4)
Target.WaitForTarget(10000, False)
Target.Cancel( )
Target.WaitForTarget(10000, False)
Target.TargetExecute(0xDE80)