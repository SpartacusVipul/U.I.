import wx
import ser_comm
global group1_ctrls
group1_ctrls=[]
global buf        #number of samples in one window
global now        #number of windows sampled
global err_flag
global data
global ip
buf = 1000;     #number of samples in one window
now = 128;      #number of windows sampled
err_flag = 0
data = ''
ip = ''
 
class ParentFrame (wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,-1)
 
        Boax = wx.BoxSizer(wx.VERTICAL)
        fframe = wx.BoxSizer(wx.HORIZONTAL)
 
        panel_0 = Panel0(self)
        panel_1 = Panel1(self)
        panel_2 = Panel2(self)
        panel_3 = Panel3(self)
        Boax.Add(panel_0,1,wx.EXPAND|wx.ALL)
        fframe.Add(panel_1,1,wx.EXPAND|wx.ALL)
        fframe.Add(panel_2,wx.EXPAND|wx.BOTTOM |wx.ALL)
        Boax.Add(fframe)
        Boax.Add(panel_3,wx.EXPAND|wx.ALL)
        self.SetSizer(Boax)
        self.SetAutoLayout(True)
class Panel0 (wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)

        panel0 = self
        boxp0 = wx.BoxSizer(wx.HORIZONTAL)
 
        wddown=wx.ComboBox(panel0,-1,value="",choices=["/dev/ttyUSB0","/dev/ttyUSB1","/dev/ttyUSB2"])
        boxp0.Add(wddown,0,wx.ALL,10)

        connect = wx.Button(panel0,-1,"Connect")
        disconnect = wx.Button(panel0,-1,"Disconnect")
        boxp0.Add(connect,0,wx.ALIGN_CENTRE,10)
        boxp0.Add(disconnect,0,wx.ALL,10)
 
        panel0.SetSizer(boxp0)
        panel0.SetAutoLayout(True)
 
 
class Panel1 (wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
 
         ####################################################################
         # Panel 1 for radio butoons and win
         ####################################################################
        mainboxp1 = wx.BoxSizer(wx.VERTICAL)
 
        panel1 = self
        twiddle = wx.Button(panel1,-1,"Twiddle")
        mainboxp1.Add(twiddle,0,wx.ALL,10)
 
        namesb1p1 = wx.StaticBox(panel1,-1,"Hash")
        sb1p1  = wx.StaticBoxSizer(namesb1p1,wx.VERTICAL)
        alignb1 = wx.FlexGridSizer(cols = 3)
 
        grp_buttons = []

        hwin = wx.StaticText(panel1,-1,"#Win :")
        # hwin_t = wx.TextCtrl(panel1,-1,size=(60,-1))
        hwin_t=wx.ComboBox(panel1,-1,value="",choices=["100","1000","10000","48000"])
        hwin_t.Bind(wx.EVT_COMBOBOX,self.dropnb)
        hwin_t.ide=1
        winemp = wx.StaticText(panel1,-1,"")
 
        buf = wx.StaticText(panel1,-1,"#Buf :")
         # buf_t = wx.TextCtrl(panel1,-1,size=(60,-1))
        buf_t=wx.ComboBox(panel1,-1,value="",choices=["16","64","128","256","512","1024"])
        buf_t.Bind(wx.EVT_COMBOBOX,self.dropnb)
        buf_t.ide=2
        setb=wx.Button(panel1,-1,label="SET")
        # setb.Bind(wx.EVT_BUTTON,self.setbutton)
        setb.Bind(wx.EVT_BUTTON,self.setbutton)

        grp_buttons.append((hwin,hwin_t,winemp))
        grp_buttons.append((buf,buf_t,setb))
 
        for col1,col2,col3 in grp_buttons:
            alignb1.Add(col1,0,wx.ALL,10)
            alignb1.Add(col2,0,wx.ALL,10)
            alignb1.Add(col3,0,wx.ALL,10)

 
        sb1p1.Add(alignb1)
        mainboxp1.Add(sb1p1,0,wx.ALL,10)
         ####################################################################
         # Radio butoons
         ####################################################################
 
        vs = wx.BoxSizer(wx.VERTICAL)

        box1_title = wx.StaticBox(panel1,-1,"Frequency")
        box1 = wx.StaticBoxSizer(box1_title,wx.VERTICAL)
        grid1 = wx.FlexGridSizer(cols=3)

         #Group of controls
 
 
        rb1 = wx.RadioButton( panel1, -1, " Buffer 1 ", style = wx.RB_GROUP )
        rb1upl=wx.TextCtrl(panel1,size=(80,-1))
        rb1lol=wx.TextCtrl(panel1,size=(80,-1))
         # self.rb1lotxt = wx.StaticText(self.panel3,label = 'range:')
         # self.rb1uptxt = wx.StaticText(self.panel3,label = 'WB:')
 
        rb2 = wx.RadioButton( panel1, -1, " Kaisurf 2 " )
        rb2upl=wx.TextCtrl(panel1,size=(80,-1))
        rb2lol=wx.TextCtrl(panel1,size=(80,-1))
         # self.rb2uptxt = wx.StaticText(self.panel3,label = 'WB:')
         # self.rb2lotxt = wx.StaticText(self.panel3,label = 'range:')
 
         # self.rb3 = wx.RadioButton( self.panel3, -1, " Raw " )
         # self.rb3upl=wx.TextCtrl(self.panel3,size=(80,-1))
 
        group1_ctrls.append((rb1,rb1upl,rb1lol))
        group1_ctrls.append((rb2,rb2upl,rb2lol))
         # self.group1_ctrls.append((self.rb3,self.rb3upl))
 
        for radio, text1 ,text2 in group1_ctrls:
            grid1.Add( radio, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
            grid1.Add( text1, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
            grid1.Add( text2, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
            # grid1.Add( text3, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
             # grid1.Add( text4, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
 
        box1.Add( grid1, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )
        vs.Add( box1, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )

         #FOr radio button 1
         # self.panel3.SetSizer( vs )
         # vs.Fit( self.panel3 )
 
 
         # Setup event handling and initial state for controls:
        for radio, text1,text2 in group1_ctrls:
            self.Bind(wx.EVT_RADIOBUTTON, self.OnGroup1Select, radio )
 
        for radio, text1, text2 in group1_ctrls:
            radio.SetValue(0)
            text1.Enable(False)
            text2.Enable(False)
 
 
        mainboxp1.Add(vs)
 
        panel1.SetSizer(mainboxp1)
 
    def OnGroup1Select( self, event ):
 
        for radio, text1, text2 in group1_ctrls:
            radio_selected = event.GetEventObject()
            if radio is radio_selected:
                text1.Enable(True)
                text2.Enable(True)
            else:
                text1.Enable(False)
                text2.Enable(False)
    def setbutton(self,event):
        #m=dropnb()
        ser_comm.now = n
        ser_comm.buf =  b
        print ser_comm.buf,ser_comm.now
        ser_comm.cal()
    def dropnb(self,event):
        i=event.GetEventObject().ide
        if i ==1:
            global n
            n=event.GetEventObject().GetValue()
            if n==100:
                n=1
            elif n==1000:
                n=2
            elif n==10000:
                n=3
            elif n==48000:
                n=4
            print n
        elif i ==2:
            global b
            b=event.GetEventObject().GetValue()
            if b<=16:
                b=1
            elif b==64:
                b=2
            elif b==128:
                b=3
            elif b==256:
                b=4
            elif b==512:
                b=5
            elif b==1024:
                b=6
            print b
 
class Panel2(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)

 
         ####################################################################
         # Panel 2 for sampling and Value ( Rightside )
         ####################################################################
 
        panel2 = self
        rightbox = wx.BoxSizer(wx.VERTICAL)
 
        sbox1 = wx.StaticBox(panel2,-1,"Sampling")
        box1 = wx.StaticBoxSizer(sbox1,wx.HORIZONTAL)
 
        b1 = wx.Button(panel2,-1,"async")
        box1.Add(b1,0,wx.ALL,10)
        b1.ide=1
        b2 = wx.Button(panel2,-1,"sync")
        box1.Add(b2,0,wx.ALL,10)
        b2.ide=2
        rightbox.Add(box1,0)
 
        sbox2 = wx.StaticBox(panel2,-1,"Value Transfer")
        box2 = wx.StaticBoxSizer(sbox2,wx.HORIZONTAL)

        b4 = wx.Button(panel2,-1,"Hexadecimal")
        box2.Add(b4,0,wx.ALL,10)
        b4.ide=4
        b5= wx.Button(panel2,-1,"Decimal")
        box2.Add(b5,2,wx.ALL,10)
        b5.ide=5
        rightbox.Add(box2,0)
 
        sbox3 = wx.StaticBox(panel2,-1)
        box3 = wx.StaticBoxSizer(sbox3,wx.VERTICAL)
        box3a = wx.BoxSizer(wx.HORIZONTAL)
 
        lastwin = wx.Button(panel2,-1,"Last Window")
        box3a.Add(lastwin,0,wx.ALL,10)
        resto = wx.Button(panel2,-1,"Restore")
        box3a.Add(resto,0,wx.ALL,10)
        box3b = wx.BoxSizer(wx.HORIZONTAL)
 
        save = wx.Button(panel2,-1,"Save")
        box3b.Add(save,0,wx.ALL,10)
 
        t1 = wx.TextCtrl(self, -1, "  .txt")
        wx.CallAfter(t1.SetInsertionPoint, 0)
        box3b.Add(t1,0,wx.ALL,10)

 
        box3.Add(box3a,0)
        box3.Add(box3b,0)
 
        rightbox.Add(box3,0)
 
        panel2.SetSizer(rightbox)
        b1.Bind(wx.EVT_BUTTON, self.bclick)
        b2.Bind(wx.EVT_BUTTON, self.bclick)
        b4.Bind(wx.EVT_BUTTON, self.bclick)
        b5.Bind(wx.EVT_BUTTON, self.bclick)
    def bclick(self,event):
        i=event.GetEventObject().ide
        if i==1:
            ip='a'
            ser_comm.ser_comm_main(ser_comm_ser,buf,now,data,ip)
        elif i==2:
            ip='s'
            ser_comm.ser_comm_main(ser_comm_ser,buf,now,data,ip)
        elif i==4:
            ip='x'
            ser_comm.ser_comm_main(ser_comm_ser,buf,now,data,ip)
        elif i==5:
            ip='d'
            ser_comm.ser_comm_main(ser_comm_ser,buf,now,data,ip)



 
class Panel3(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
 
        panel3 = self
        boxp3 = wx.BoxSizer(wx.HORIZONTAL)
 
        msg = wx.StaticText(panel3,-1,"Message:")
        msg_txt = wx.TextCtrl(panel3,-1,"      ")
 
        boxp3.Add(msg,0,wx.ALL,10)
        boxp3.Add(msg_txt,0,wx.ALL,10)
 
        panel3.SetSizer(boxp3)
 
 
 
 
app = wx.App()
frame = ParentFrame(None,-1)
frame.Show()
app.MainLoop()