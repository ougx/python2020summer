# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 09:37:47 2020

@author: Michael Ou
"""


# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

###########################################################################
## Class MyFrame1
###########################################################################

plt.style.use('ggplot')

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 767,537 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.wxPnl = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1.Add( self.wxPnl, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.wxPnl.figure = matplotlib.figure.Figure()
        self.axes = self.wxPnl.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.wxPnl, -1, self.wxPnl.figure)
        
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.makePlot )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def makePlot( self, event ):
        ser1 = pd.Series([1, 2, 3, 4, 3, 2, 1])
        ser2 = pd.Series([0.01, 0.02, 0.03, 0.01] )
        
        ser1.plot(ax=self.axes)
        self.axes.set_ylabel('Discharge')
        
        ax1 = self.axes.twinx()
        ser2.plot.bar(ax=ax1, color='C1', alpha=0.5)
        ax1.invert_yaxis()
        ax1.set_ylabel('Precip')
        
        self.wxPnl.figure.tight_layout()
        
        self.canvas.draw()


if __name__ == '__main__':
    app = wx.App(redirect=True)
    frm = MyFrame1(None)
    frm.Show()
    app.MainLoop()
