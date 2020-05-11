#By Mourn#8182 discord contact


############### GUI INTERFACE FOR DEXXER OR SAMP
# please DM me with ideas
# Requires additional script DexxerGUIreceive loaded into ur razor THEN RUN ME FOR BOTH 


import clr, time, thread
from System.Threading import ThreadStart, Thread
clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Data')

import System
from System.Collections.Generic import List
from System import Byte
from System.Drawing import Point, Color, Size
from System.Windows.Forms import (Application, Button, Form, BorderStyle, 
    Label, FlatStyle, DataGridView, DataGridViewAutoSizeColumnsMode,
    DataGridViewSelectionMode, DataGridViewEditMode, RadioButton, GroupBox, TextBox, CheckBox)
from System.Data import DataTable
contents = []
Misc.SetSharedValue('run',False)

class dexxer(Form):
    CurVer = '1.1'
    ScriptName = 'Mourns Dexxer Assistant'
    
    
    def __init__(self, contents):
        self.Contents = contents       
        self.BackColor = Color.FromArgb(25,25,25)
        self.ForeColor = Color.FromArgb(231,231,231)
        self.Size = Size(200, 425)
        self.Text = '{0} - v{1}'.format(self.ScriptName, self.CurVer)
        self.TopMost = True
        
        self.box = GroupBox()
        self.box.BackColor = Color.FromArgb(25,25,25)
        self.box.ForeColor = Color.FromArgb(23,221,23)
        self.box.Size = Size(180, 140)
        self.box.Location = Point(2, 2)
        self.box.Text = 'Options'
        
        self.box2 = GroupBox()
        self.box2.BackColor = Color.FromArgb(25,25,25)
        self.box2.ForeColor = Color.FromArgb(23,221,23)
        self.box2.Size = Size(180, 40)
        self.box2.Location = Point(02, 275)
        self.box2.Text = 'Weapon Type'
        
        self.box3 = GroupBox()
        self.box3.BackColor = Color.FromArgb(25,25,25)
        self.box3.ForeColor = Color.FromArgb(23,221,23)
        self.box3.Size = Size(180, 130)
        self.box3.Location = Point(02, 144)
        self.box3.Text = 'Dress/Arm'
        
        self.box4 = GroupBox()
        self.box4.BackColor = Color.FromArgb(25,25,25)
        self.box4.ForeColor = Color.FromArgb(23,221,23)
        self.box4.Size = Size(180, 60)
        self.box4.Location = Point(02, 315)
        
        self.cbA = CheckBox()
        self.cbA.Text = 'Conf/Evade'
        self.cbA.Checked = False
        self.cbA.BackColor = Color.FromArgb(25,25,25)
        self.cbA.Location = Point(10, 15)
        self.cbA.Size = Size(85, 20)
        
        self.cbB = CheckBox()
        self.cbB.Text = 'EoO'
        self.cbB.Checked = False
        self.cbB.BackColor = Color.FromArgb(25,25,25)
        self.cbB.Location = Point(95, 15)
        self.cbB.Size = Size(85, 20)
        
        self.cbC = CheckBox()
        self.cbC.Text = 'Band Heal'
        self.cbC.Checked = False
        self.cbC.BackColor = Color.FromArgb(25,25,25)
        self.cbC.Location = Point(10, 35)
        self.cbC.Size = Size(85, 20)
        
        self.cbD = CheckBox()
        self.cbD.Text = 'Cons Wep'
        self.cbD.Checked = False
        self.cbD.BackColor = Color.FromArgb(25,25,25)
        self.cbD.Location = Point(95, 35)
        self.cbD.Size = Size(85, 20)
        
        self.cbE = CheckBox()
        self.cbE.Text = 'Honor'
        self.cbE.Checked = False
        self.cbE.BackColor = Color.FromArgb(25,25,25)
        self.cbE.Location = Point(10, 55)
        self.cbE.Size = Size(85, 20)
        
        self.cbF = CheckBox()
        self.cbF.Text = 'Div Fury'
        self.cbF.Checked = False
        self.cbF.BackColor = Color.FromArgb(25,25,25)
        self.cbF.Location = Point(95, 55)
        self.cbF.Size = Size(85, 20)
        
        self.cbG = CheckBox()
        self.cbG.Text = 'Onslaught'
        self.cbG.Checked = False
        self.cbG.BackColor = Color.FromArgb(25,25,25)
        self.cbG.Location = Point(10, 75)
        self.cbG.Size = Size(85, 20)
        
        self.cbH = CheckBox()
        self.cbH.Text = 'Cntr Atk'
        self.cbH.Checked = False
        self.cbH.BackColor = Color.FromArgb(25,25,25)
        self.cbH.Location = Point(95, 75)
        self.cbH.Size = Size(85, 20)
        
        self.cbI = CheckBox()
        self.cbI.Text = 'OJ Petal'
        self.cbI.Checked = False
        self.cbI.BackColor = Color.FromArgb(25,25,25)
        self.cbI.Location = Point(10, 95)
        self.cbI.Size = Size(85, 20)
        
        self.rbD = RadioButton()
        self.rbD.Text = 'D Axe'
        self.rbD.Location = Point(25, 290)
        self.rbD.BackColor = Color.FromArgb(25,25,25)
        self.rbD.ForeColor = Color.FromArgb(231,231,231)
        self.rbD.Size = Size(65, 20)
        
        self.rbE = RadioButton()
        self.rbE.Text = 'B Staff'
        self.rbE.Location = Point(105, 290)
        self.rbE.BackColor = Color.FromArgb(25,25,25)
        self.rbE.ForeColor = Color.FromArgb(231,231,231)
        self.rbE.Size = Size(65, 20)
        
        self.btnA = Button()
        self.btnA.Text = 'Demon'
        self.btnA.BackColor = Color.FromArgb(50,24,25)
        self.btnA.Location = Point(10, 242)
        self.btnA.Size = Size(55, 25)
        self.btnA.FlatStyle = FlatStyle.Flat
        self.btnA.FlatAppearance.BorderSize = 1
        self.btnA.Click += self.btnDemonPressed
        
        self.btnB = Button()
        self.btnB.Text = 'Reptile'
        self.btnB.BackColor = Color.FromArgb(25,50,25)
        self.btnB.Location = Point(65, 242)
        self.btnB.Size = Size(55, 25)
        self.btnB.FlatStyle = FlatStyle.Flat
        self.btnB.FlatAppearance.BorderSize = 1 
        self.btnB.Click += self.btnReptilePressed
        
        self.btnC = Button()
        self.btnC.Text = 'Undead'
        self.btnC.BackColor = Color.FromArgb(50,25,25)
        self.btnC.Location = Point(120, 242)
        self.btnC.Size = Size(55, 25)
        self.btnC.FlatStyle = FlatStyle.Flat
        self.btnC.FlatAppearance.BorderSize = 1 
        self.btnC.Click += self.btnUndeadPressed
        
        self.btnD = Button()
        self.btnD.Text = 'Elemen'
        self.btnD.BackColor = Color.FromArgb(25,50,25)
        self.btnD.Location = Point(10, 217)
        self.btnD.Size = Size(55, 25)
        self.btnD.FlatStyle = FlatStyle.Flat
        self.btnD.FlatAppearance.BorderSize = 1 
        self.btnD.Click += self.btnElemenPressed
        
        self.btnE = Button()
        self.btnE.Text = 'Arach'
        self.btnE.BackColor = Color.FromArgb(50,25,25)
        self.btnE.Location = Point(65, 217)
        self.btnE.Size = Size(55, 25)
        self.btnE.FlatStyle = FlatStyle.Flat
        self.btnE.FlatAppearance.BorderSize = 1 
        self.btnE.Click += self.btnArachPressed
        
        self.btnF = Button()
        self.btnF.Text = 'Repond'
        self.btnF.BackColor = Color.FromArgb(25,50,25)
        self.btnF.Location = Point(120, 217)
        self.btnF.Size = Size(55, 25)
        self.btnF.FlatStyle = FlatStyle.Flat
        self.btnF.FlatAppearance.BorderSize = 1 
        self.btnF.Click += self.btnRepondPressed
        
        self.btnG = Button()
        self.btnG.Text = 'Main Dress'
        self.btnG.BackColor = Color.FromArgb(25,50,25)
        self.btnG.Location = Point(10, 160)
        self.btnG.Size = Size(165, 25)
        self.btnG.FlatStyle = FlatStyle.Flat
        self.btnG.FlatAppearance.BorderSize = 1 
        self.btnG.Click += self.btnDressPressed
        
        self.btnH = Button()
        self.btnH.Text = 'Luck Suit'
        self.btnH.BackColor = Color.FromArgb(50,50,10)
        self.btnH.Location = Point(10, 185)
        self.btnH.Size = Size(165, 25)
        self.btnH.FlatStyle = FlatStyle.Flat
        self.btnH.FlatAppearance.BorderSize = 1 
        self.btnH.Click += self.btnLuckPressed
        
        self.btnGet = Button()
        self.btnGet.Text = 'Stop'
        self.btnGet.BackColor = Color.FromArgb(100,10,10)
        self.btnGet.Location = Point(95, 330)
        self.btnGet.Size = Size(80, 35)
        self.btnGet.FlatStyle = FlatStyle.Flat
        self.btnGet.FlatAppearance.BorderSize = 1
        self.btnGet.Click += self.btnStopPressed
        
        self.startGet = Button()
        self.startGet.Text = 'Start'
        self.startGet.BackColor = Color.FromArgb(10,100,10)
        self.startGet.Location = Point(10, 330)
        self.startGet.Size = Size(80, 35)
        self.startGet.FlatStyle = FlatStyle.Flat
        self.startGet.FlatAppearance.BorderSize = 1
        self.startGet.Click += self.btnStartPressed
        
        
        self.Controls.Add(self.cbA)
        self.Controls.Add(self.cbB)
        self.Controls.Add(self.cbC)
        self.Controls.Add(self.cbD)
        self.Controls.Add(self.cbE)
        self.Controls.Add(self.cbF)
        self.Controls.Add(self.cbG)
        self.Controls.Add(self.cbH)
        self.Controls.Add(self.cbI)
        self.Controls.Add(self.btnA)
        self.Controls.Add(self.btnB)
        self.Controls.Add(self.btnC)
        self.Controls.Add(self.btnD)
        self.Controls.Add(self.btnE)
        self.Controls.Add(self.btnF)
        self.Controls.Add(self.btnG)
        self.Controls.Add(self.btnH)
        self.Controls.Add(self.btnGet)
        self.Controls.Add(self.startGet)
        self.Controls.Add(self.rbD)   
        self.Controls.Add(self.rbE)
        self.Controls.Add(self.box)
        self.Controls.Add(self.box2)
        self.Controls.Add(self.box3)
        self.Controls.Add(self.box4)
        
    def btnStartPressed(self, sender, args):
        Misc.SetSharedValue('run','True')
        Misc.SendMessage('Starting',80)
        def attack():
            while Misc.ReadSharedValue('run') == 'True':
                eNumber = 0
                fil = Mobiles.Filter()
                fil.Enabled = True
                fil.RangeMax = 1
                fil.Notorieties = List[Byte](bytes([3,4,5,6]))
                if Misc.ReadSharedValue('dAxe') == 'True':
                    enemies = Mobiles.ApplyFilter(fil)
                    Mobiles.Select(enemies,'Nearest')
                    for enemy in enemies:
                        eNumber += 1
                    if eNumber == 1:
                        eNumber = 0
                        if not Player.HasSpecial:
                            Player.WeaponPrimarySA()
                        Player.Attack(enemy)
                    if eNumber == 2:
                        eNumber = 0
                        if not Player.SpellIsEnabled('Momentum Strike'):
                            Spells.CastBushido('Momentum Strike')
                        Player.Attack(enemy) 
                    if eNumber > 2 :
                        eNumber = 0
                        if not Player.HasSpecial:
                            Player.WeaponSecondarySA()
                        Player.Attack(enemy)
                    Misc.Pause(250) 
                if Misc.ReadSharedValue('bStaff') == 'True':
                    enemies = Mobiles.ApplyFilter(fil)
                    Mobiles.Select(enemies,'Nearest')
                    for enemy in enemies:
                        eNumber += 1
                    if eNumber == 1:
                        eNumber = 0
                        if not Player.HasSpecial:
                            Player.WeaponPrimarySA()
                        Player.Attack(enemy)
                    if eNumber >= 2:
                        eNumber = 0
                        if not Player.SpellIsEnabled('Momentum Strike'):
                            Spells.CastBushido('Momentum Strike')
                        Player.Attack(enemy)
                Misc.Pause(500)
                
        def cast():
            while Misc.ReadSharedValue('run') == 'True':
                if Misc.ReadSharedValue('bush') == 'True':
                    bush()
                if Misc.ReadSharedValue('eoo') == 'True':
                    enemyOfOne()
                if Misc.ReadSharedValue('consec') == 'True':  
                    consecrateWep()
                if Misc.ReadSharedValue('honor') == 'True':
                    honorNearest()
                if Misc.ReadSharedValue('devFury') == 'True':
                    divineFury()
                if Misc.ReadSharedValue('onslaught') == 'True':
                    onslaughtMastery()
                if Misc.ReadSharedValue('cAttack') == 'True':
                    counterAttack()
                if Misc.ReadSharedValue('ojPetal') == 'True':
                    orangePetal()
                Misc.Pause(500)
                
        c = Thread(ThreadStart(cast))
        c.Start()
        t = Thread(ThreadStart(attack))
        t.Start()
        Misc.SetSharedValue('bush','False')
        Misc.SetSharedValue('eoo','False')
        Misc.SetSharedValue('consec','False')
        Misc.SetSharedValue('honor','False')
        Misc.SetSharedValue('devFury','False')
        Misc.SetSharedValue('onslaught','False')
        Misc.SetSharedValue('cAttack','False')
        Misc.SetSharedValue('ojPetal','False')
        Misc.SetSharedValue('dAxe','False')
        Misc.SetSharedValue('bStaff','False')
        if self.cbC.Checked:
            Misc.Pause(300)  
            if BandageHeal.Status() == False:
                BandageHeal.Start()
        if self.cbA.Checked:
            Misc.Pause(300)
            Misc.SetSharedValue('bush','True')
        if self.cbB.Checked:
            Misc.Pause(300)
            Misc.SetSharedValue('eoo','True')       
        if self.cbD.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('consec','True')
        if self.cbE.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('honor','True')
        if self.cbF.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('devFury','True') 
        if self.cbG.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('onslaught','True')
        if self.cbH.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('cAttack','True')
        if self.cbI.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('ojPetal','True')
        if self.rbD.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('dAxe','True')
        if self.rbE.Checked:
            Misc.Pause(300)  
            Misc.SetSharedValue('bStaff','True')    
        
        
    def btnStopPressed(self, sender, args): 
        Misc.Pause(300)
        Misc.SendMessage('Stopping',45)
        Misc.SetSharedValue('run', 'False')
           
    def btnDemonPressed(self, sender, args):
        Dress.ChangeList('demon')
        Dress.DressFStart()
    def btnUndeadPressed(self, sender, args):
        Dress.ChangeList('undead')
        Dress.DressFStart()
    def btnReptilePressed(self, sender, args):
        Dress.ChangeList('reptile')
        Dress.DressFStart()
    def btnRepondPressed(self, sender, args):
        Dress.ChangeList('repond')
        Dress.DressFStart()
    def btnElemenPressed(self, sender, args):
        Dress.ChangeList('elemen')
        Dress.DressFStart()
    def btnArachPressed(self, sender, args):
        Dress.ChangeList('arach')
        Dress.DressFStart()
    def btnDressPressed(self, sender, args):
        Dress.ChangeList('dress')
        Dress.DressFStart()
    def btnLuckPressed(self, sender, args):
        Dress.ChangeList('luck')
        Dress.DressFStart()
        

      
def bush():
    healhits = 90
    evadehits = 100
    if Player.Hits < (healhits) and not Player.BuffsExist('Confidence'):
        Misc.Pause (400)
        Spells.CastBushido("Confidence")
        Misc.Pause (500)
        
    if Player.Hits < (evadehits) and not Player.BuffsExist('Evasion'):
        Misc.Pause (400)
        Spells.CastBushido("Evasion")
        Misc.Pause (500)
        
def enemyOfOne():
    if not Player.BuffsExist('Enemy Of One'):
        Spells.CastChivalry('Enemy Of One')
        Misc.Pause(500)
        
def consecrateWep():
    if not Player.BuffsExist('Consecrate Weapon'):
        Spells.CastChivalry('Consecrate Weapon')
        Misc.Pause(500)
        
def honorNearest():
    if not Player.BuffsExist('Honored'):
        honfil = Mobiles.Filter()
        honfil.Enabled = True
        honfil.RangeMax = 8
        honfil.Notorieties = List[Byte](bytes([3,4,5,6]))
        enemies = Mobiles.ApplyFilter(honfil)
        Misc.Pause(200)
        enemy = Mobiles.Select(enemies,'Nearest')
        if enemy:
            Player.InvokeVirtue("Honor")
            Target.WaitForTarget(1000, False)
            Target.TargetExecute(enemy.Serial)
        
def divineFury():
    if Player.Stam < Player.Stam - 20:   
        Spells.CastChivalry("Divine Fury")
        Misc.Pause(500)
        
def onslaughtMastery():
    if Timer.Check('mastery') == False:
        Spells.CastMastery('Onslaught')
        Timer.Create('mastery',10000)
    
def counterAttack():
    if not Player.BuffsExist('Counter Attack'):
        Spells.CastBushido('Counter Attack')
        Misc.Pause(500)
        
def orangePetal():
    ojpetals = Items.FindByID(0x1021,0x002B,Player.Backpack.Serial)
    if not ojpetals:
        if Timer.Check('oj') == False:
            Misc.SendMessage('No Orange Petals',33)
        Timer.Create('oj',10000)
        pass
    if Player.BuffsExist('Poison'):
        if not Player.BuffsExist('Orange Petals'):
            Items.UseItem(ojpetals.Serial)
            Misc.Pause(200)
                       
form = dexxer(contents)
Application.Run(form)




