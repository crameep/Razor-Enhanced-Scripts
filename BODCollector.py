
while True:
    Misc.WaitForContext(0x00029963, 10000)
    Misc.Pause(1000)
    Misc.ContextReply(0x00029963, 0)
    Misc.Pause(1000)
    GumpTxt = Gumps.CurrentGump()
    Misc.SendMessage(GumpTxt)
    if GumpTxt == 3666206949:
        Gumps.SendAction(3666206949, 1)
    elif GumpTxt == 2611865322:
        Gumps.SendAction(2611865322, 1)
    Gumps.SendAction(3188567326, 1)
    Gumps.SendAction(2611865322, 1)
    Misc.Pause(15000)

