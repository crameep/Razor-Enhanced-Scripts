while True:
    Player.UseSkill("Animal Taming")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(0x81AD)