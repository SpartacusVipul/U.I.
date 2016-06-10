import wx
import ser_comm

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title,size=(1000, 1000))

        self.panel1 = wx.Panel(self, -1,pos=(200,200),size=(250,220))

        async = wx.Button(self.panel1, 1, label="async",pos=(10,10))
        async.ide=1;
        sync = wx.Button(self.panel1, -1, label="sync",pos=(120,10))
        sync.ide=2
        Hex = wx.Button(self.panel1, -1, label="Hex",pos=(10,50))
        Hex.ide=3
        decim = wx.Button(self.panel1, -1, label="Decim",pos=(120,50))
        decim.ide=4
        save = wx.Button(self.panel1, -1, label="Save",pos=(10,130))
        save.ide=5
        sizer0=wx.BoxSizer(wx.VERTICAL)
        self.panel1.SetSizer(sizer0)
        sizer0.Fit(self.panel1)
        self.panel1.Layout()
        #panel1sizer=wx.BoxSizer(wx.VERTICAL)
        
        #########################################################
        #########           Button Bind             #############
        async.Bind(wx.EVT_BUTTON, self.bclick)
        sync.Bind(wx.EVT_BUTTON, self.bclick)
        Hex.Bind(wx.EVT_BUTTON, self.bclick)
        decim.Bind(wx.EVT_BUTTON, self.bclick)
        save.Bind(wx.EVT_BUTTON, self.bclick)
    def  bclick(self,event):
        i= event.GetEventObject().ide               
        if i== 1:
            ser_comm.ip='a'
            ser_comm.cal()
        elif i==2:
            ser_comm.ip='s'
            ser_comm.cal()
        elif i==3:
            ser_comm.ip='x'
            ser_comm.cal()
        elif i==4:
            ser_comm.ip='d'
            ser_comm.cal()
        elif i==5:
            print 'Save'
        elif i==6:
            ser_comm.ip='t'
            ser_comm.cal()
        ########################################################
        
        panel2 = wx.Panel(self, -1,pos=(0,200))
        wddown=wx.ComboBox(panel2,-1,value="",choices=["/dev/ttyUSB0","/dev/ttyUSB1","/dev/ttyUSB2"])
        twiddle = wx.Button(panel2, -1, label="Twiddle",pos=(0,30))
        twiddle.ide=6
        #twiddle.Bind(wx.EVT_BUTTON, self.bclick)
        sizer12=wx.BoxSizer(wx.VERTICAL)
        panel2.SetSizer(sizer12)
        sizer12.Fit(panel2)
        panel2.Layout()

        self.panel3 = wx.Panel(self,-1,pos=(0,250))

        self.rb1 = wx.RadioButton( self.panel3, -1, " Butter 1 ", style = wx.RB_GROUP )
        self.rb2 = wx.RadioButton( self.panel3, -1, " Kaisurf 2 " )
        self.rb3 = wx.RadioButton( self.panel3, -1, " Raw " )


        """
        vs = wx.BoxSizer(wx.VERTICAL)

        box1_title = wx.StaticBox(panel3,-1,"Frequency")
        box1 = wx.StaticBoxSizer(box1_title,wx.VERTICAL)
        grid1 = wx.FlexGridSizer(cols=5)

        # Frequency control box1

        self.group1_ctrls = []
        radio1 = wx.RadioButton( panel3, -1, " Buffer 1 ", style = wx.RB_GROUP )
        radio2 = wx.RadioButton( panel3, -1, " Kaisurf 2 " )
        radio3 = wx.RadioButton( panel3, -1, " Raw " )
        text1 = wx.TextCtrl( panel3, -1, "BW" )
        text2 = wx.TextCtrl( panel3, -1, "" )
        text3 = wx.TextCtrl( panel3, -1, "" )
        self.group1_ctrls.append((radio1, text1))
        self.group1_ctrls.append((radio2, text2))
        self.group1_ctrls.append((radio3, text3))

        sizer = wx.GridBagSizer(5,5)
        sizer.Add(radio1,(0,0)
        sizer.Add(radio2,(1,0)
        sizer.Add(radio3,(2,0)
        sizer.Add(text1,(0,1)
        sizer.Add(text2,(1,1)
        sizer.Add(text3,(2,1)


        for radio, text in self.group1_ctrls:
            grid1.Add( radio, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
            grid1.Add( text, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

        box1.Add( grid1, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )
        vs.Add( box1, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )

        """

        # self.rb1.Bind(wx.EVT_RADIOBUTTON,self.SetVal)

        self.rb1upl=wx.TextCtrl(self.panel3,size=(100,-1))
        self.rb1lol=wx.TextCtrl(self.panel3,size=(100,-1))
        self.rb2upl=wx.TextCtrl(self.panel3,size=(100,-1))
        self.rb2lol=wx.TextCtrl(self.panel3,size=(100,-1))
        self.rb3txt=wx.TextCtrl(self.panel3,size=(100,-1))

        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel3, 1, wx.ALL | wx.EXPAND)


        self.sizer1 = wx.GridBagSizer(3, 3)
        self.sizer1.Add(self.rb1, (0, 0))
        self.sizer1.Add(self.rb1upl, (0, 1))
        self.sizer1.Add(self.rb1lol, (0, 2))
        self.sizer1.Add(self.rb2, (1, 0))
        self.sizer1.Add(self.rb2upl, (1, 1))
        self.sizer1.Add(self.rb2lol, (1, 2))
        self.sizer1.Add(self.rb3, (2,0))
        self.sizer1.Add(self.rb3txt, (2, 1), (2, 2), flag=wx.EXPAND)

        self.border = wx.BoxSizer()
        self.border.Add(self.sizer1, 1, wx.ALL | wx.EXPAND, 3)
        self.panel3.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(panel1,0,wx.EXPAND |wx.ALL,border=10)
        sizer.Add(panel2,0,wx.EXPAND |wx.ALL,border=10)
        sizer.Add(self.panel3,0,wx.EXPAND |wx.ALL,border=10)
    '''
        panel5 = wx.Panel(self, -1,pos=(0,0),size=(900,900))
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(panel5, 1, wx.ALL | wx.EXPAND)
        print 'donnnnnno'
        self.sizer3 = wx.GridBagSizer(6, 3)
        self.sizer3.Add(self.panel1, (1, 1))
        self.sizer3.Add(panel2, (1, 0))
        #self.sizer3.Add(self.panel3, (4, 0))
        #self.sizer3.Add(panel6, (2, 0))
        #self.sizer3.Add(panel8, (0, 1))
        #self.sizer3.Add(panel9, (5, 0))
        #self.sizer3.Add(self.rb3, (2,0))
        #self.sizer3.Add(self.rb3txt, (2, 1), (2, 2), flag=wx.EXPAND)

        self.border = wx.BoxSizer()
        self.border.Add(self.sizer3, 1, wx.ALL | wx.EXPAND, 3)
        panel5.SetSizer(self.border)
        self.border.Fit(panel5)
        self.SetSizerAndFit(self.windowSizer)'''

'''
    '''
'''
        # self.panel4 = wx.Panel(self,-1,pos=(0,300),size=(20,20))

        self.panel3 = wx.Panel(self,-1,pos=(0,250))

        self.rb1 = wx.RadioButton( self.panel3, -1, " Butter 1 ", style = wx.RB_GROUP )
        self.rb2 = wx.RadioButton( self.panel3, -1, " Kaisurf 2 " )
        self.rb3 = wx.RadioButton( self.panel3, -1, " Raw " )


        """
        vs = wx.BoxSizer(wx.VERTICAL)

        box1_title = wx.StaticBox(panel3,-1,"Frequency")
        box1 = wx.StaticBoxSizer(box1_title,wx.VERTICAL)
        grid1 = wx.FlexGridSizer(cols=5)

        # Frequency control box1

        self.group1_ctrls = []
        radio1 = wx.RadioButton( panel3, -1, " Buffer 1 ", style = wx.RB_GROUP )
        radio2 = wx.RadioButton( panel3, -1, " Kaisurf 2 " )
        radio3 = wx.RadioButton( panel3, -1, " Raw " )
        text1 = wx.TextCtrl( panel3, -1, "BW" )
        text2 = wx.TextCtrl( panel3, -1, "" )
        text3 = wx.TextCtrl( panel3, -1, "" )
        self.group1_ctrls.append((radio1, text1))
        self.group1_ctrls.append((radio2, text2))
        self.group1_ctrls.append((radio3, text3))

        sizer = wx.GridBagSizer(5,5)
        sizer.Add(radio1,(0,0)
        sizer.Add(radio2,(1,0)
        sizer.Add(radio3,(2,0)
        sizer.Add(text1,(0,1)
        sizer.Add(text2,(1,1)
        sizer.Add(text3,(2,1)


        for radio, text in self.group1_ctrls:
            grid1.Add( radio, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
            grid1.Add( text, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

        box1.Add( grid1, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )
        vs.Add( box1, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )

        """

        # self.rb1.Bind(wx.EVT_RADIOBUTTON,self.SetVal)

        self.rb1upl=wx.TextCtrl(self.panel3,size=(100,-1))
        self.rb1lol=wx.TextCtrl(self.panel3,size=(100,-1))
        self.rb2upl=wx.TextCtrl(self.panel3,size=(100,-1))
        self.rb2lol=wx.TextCtrl(self.panel3,size=(100,-1))
        self.rb3txt=wx.TextCtrl(self.panel3,size=(100,-1))

        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel3, 1, wx.ALL | wx.EXPAND)


        self.sizer1 = wx.GridBagSizer(3, 3)
        self.sizer1.Add(self.rb1, (0, 0))
        self.sizer1.Add(self.rb1upl, (0, 1))
        self.sizer1.Add(self.rb1lol, (0, 2))
        self.sizer1.Add(self.rb2, (1, 0))
        self.sizer1.Add(self.rb2upl, (1, 1))
        self.sizer1.Add(self.rb2lol, (1, 2))
        self.sizer1.Add(self.rb3, (2,0))
        self.sizer1.Add(self.rb3txt, (2, 1), (2, 2), flag=wx.EXPAND)

        self.border = wx.BoxSizer()
        self.border.Add(self.sizer1, 1, wx.ALL | wx.EXPAND, 3)
        self.panel3.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)
        ######################################################################
        panel6 = wx.Panel(self,-1,pos=(90,90),size=(100 ,80))
        now = wx.StaticText(panel6, -1, "now")
        buf = wx.StaticText(panel6, -1, "Buf")
        setb=wx.Button(panel6,-1,label="SET")
        setb.Bind(wx.EVT_BUTTON,self.setbutton)
        wddown=wx.ComboBox(panel6,-1,value="",choices=["100","200","3000"])
        bddown=wx.ComboBox(panel6,-1,value="",choices=["100","700","3000"])
        wddown.Bind(wx.EVT_COMBOBOX,self.dropnb)
        bddown.Bind(wx.EVT_COMBOBOX,self.dropnb)
        wddown.ide=1
        bddown.ide=2


        #self.wint=wx.TextCtrl(panel6,size=(140,-1))
        #self.buft=wx.TextCtrl(panel6,size=(140,-1))

        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(panel6,1,wx.ALL | wx.EXPAND)

        self.sizer2= wx.GridBagSizer(3, 3)
        self.sizer2.Add(now,(0,0))
        self.sizer2.Add(buf,(1,0))
        self.sizer2.Add(wddown,(0,1))
        self.sizer2.Add(bddown,(1,1))
        self.sizer2.Add(setb,(2,1))
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer2,1,wx.ALL|wx.EXPAND,3)
        panel6.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)



        panel8 = wx.Panel(self,-1,pos=(0,0),size=(210,30))
        connectb=wx.Button(panel8,-1,label="Connect")
        dconnectb=wx.Button(panel8,-1,label="Disconnect",pos=(120,0))
        sizer18=wx.BoxSizer(wx.VERTICAL)
        panel8.SetSizer(sizer18)
        sizer18.Fit(panel8)
        panel8.Layout()

        panel9 = wx.Panel(self,-1,pos=(0,0),size=(300,40))
        message = wx.StaticText(panel9, -1, "Message")
        self.messagetext=wx.TextCtrl(panel9,size=(200,-1),style=wx.TE_MULTILINE|wx.TE_READONLY,pos=(100,0))
        sizer19=wx.BoxSizer(wx.VERTICAL)
        panel9.SetSizer(sizer19)
        sizer19.Fit(panel9)
        panel9.Layout()
        #####################################################################

        ######################################################################'''
       
'''
        ######################################################################

        sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(panel1,0,wx.EXPAND |wx.ALL,border=10)
        #sizer.Add(panel2,0,wx.EXPAND |wx.ALL,border=10)
       # sizer.Add(self.panel3,0,wx.EXPAND |wx.ALL,border=10)
        sizer.Add(panel5,0,wx.EXPAND |wx.ALL,border=0)
        #panel5.SetSizer(sizer)
        #sizer.Fit(panel5)
        #panel5.Layout()

        self.SetAutoLayout(True)
        #self.paenl5.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()



    def SetVal(self, e):
        state1 = str(self.rb1.GetValue())
        self.sb.SetStatusText(state1, 0)'''
    

'''
    def dropnb(self,event):
        i=event.GetEventObject().ide
        if i ==1:
            global n
            n=event.GetEventObject().GetValue()
            print n
        elif i ==2:
            global b
            b=event.GetEventObject().GetValue()
            print b
        #return (n,b)

    def setbutton(self,event):
        #m=dropnb()
        ser_comm.now = n
        ser_comm.buf =  b
        print ser_comm.buf,ser_comm.now
        ser_comm.cal()'''
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'frame')
        frame.Show(True)
        return True



app = MyApp(0)
app.MainLoop()
