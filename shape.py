#!/usr/bin/python

# shapes.py

import wx

class Shapes(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(350, 300))

        self.panel = wx.Panel(self, wx.ID_ANY)
        #buttonOne = wx.Button(panel, label="One", name="one",pos=(10,10))
        self.panel.Bind(wx.EVT_PAINT,self.OnPaint)

        self.Centre()
        self.Show(True)

    def OnPaint(self, event):
        dc = wx.PaintDC(self.panel)

        dc.DrawEllipse(20, 20, 90, 60)
        dc.DrawRoundedRectangle(130, 20, 90, 60, 10)
        dc.DrawArc(240, 40, 340, 40, 290, 20)

        dc.DrawPolygon(((130, 140), (180, 170), (180, 140), (220, 110), (140, 100)))
        dc.DrawRectangle(20, 120, 80, 50)
        dc.DrawSpline(((240, 170), (280, 170), (285, 110), (325, 110)))

        dc.DrawLines(((20, 260), (100, 260), (20, 210), (100, 210)))
        dc.DrawCircle(170, 230, 35)
        dc.DrawRectangle(250, 200, 60, 60)

app = wx.App()
Shapes(None, -1, 'Shapes')

app.MainLoop()