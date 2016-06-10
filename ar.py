import wx
global pos
pos=[]
########################################################################
class MyForm(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Button Tutorial")
        self.panel = wx.Panel(self, wx.ID_ANY)
 
        #sizer = wx.BoxSizer(wx.VERTICAL)
        buttonOne = wx.Button(self.panel, label="One", name="one",pos=(10,10))
        buttonTwo = wx.Button(self.panel, label="Two", name="two",pos=(100,50))
        buttonThree = wx.Button(self.panel, label="Three", name="three",pos=(0,100))
        buttonfour = wx.Button(self.panel, label="Four", name="four",pos=(100,100))
        buttonfive = wx.Button(self.panel, label="Five", name="five",pos=(200,200))
        buttondraw = wx.Button(self.panel, label="Draw", name="draw",pos=(300,100))
        buttons = [buttonOne, buttonTwo, buttonThree,buttonfour,buttonfive]
        buttondraw.Bind(wx.EVT_BUTTON,self.onDraw)
        self.panel.Bind(wx.EVT_PAINT, self.onDraw)
        for button in buttons:
            self.buildButtons(button)
 
        #panel.SetSizer(sizer)
        
    #----------------------------------------------------------------------
    def buildButtons(self, btn):
        """"""
        btn.Bind(wx.EVT_BUTTON, self.onButton)
        #sizer.Add(btn, 0, wx.ALL, 5)
    
    #----------------------------------------------------------------------
    def onButton(self, event):
        """
        This method is fired when its corresponding button is pressed
        """
        
        button = event.GetEventObject()
        print  button.GetScreenPosition()
        
        
        pos.append(self.ScreenToClient(button.GetScreenPosition()))
        
        print "The button's name is " + button.GetName()
 
        button_id = event.GetId()
        button_by_id = self.FindWindowById(button_id)
        print "The button you pressed was labeled: " + button_by_id.GetLabel()
        print "The button's name is " + button_by_id.GetName()
        print pos
    def onDraw(self,event):
        dc = wx.PaintDC(self.panel)
        dc.DrawPolygon((pos))
        #dc.DrawLines(((20, 260), (100, 260), (20, 210), (100, 210)))
        #print pos  
 
#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    
    frame.Show()
    app.MainLoop()