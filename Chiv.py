
if not(Timer.Check("Divine")):
    Spells.CastChivalry("Divine Fury")
    Misc.Pause(1000)
    Timer.Create("Divine", 10000 )
if not(Timer.Check("Consecrate")):
    Spells.CastChivalry("Consecrate Weapon")
    Misc.Pause(1000)
    Timer.Create("Consecrate", 10000 )
if not(Timer.Check("EOO")):
    Spells.CastChivalry("Enemy Of One")
    Misc.Pause(1000)
    Timer.Create("EOO", 30000 )
    
    
