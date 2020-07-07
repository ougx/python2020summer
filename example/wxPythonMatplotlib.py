# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:46:22 2020

@author: Michael Ou
"""


###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700, 900 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.btnPlot = wx.Button( self, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.btnPlot, 1, wx.ALL, 5 )


        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
        ### added line after exFormBuilder ###
        self.fig1, self.ax1, self.canvas1 = addFigAx2Panel(self.m_panel1)

        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
        ### added line after exFormBuilder ###
        self.fig2, self.ax2, self.canvas2 = addFigAx2Panel(self.m_panel2, 1, 2, sharey=True, sharex=True)


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnPlot.Bind( wx.EVT_BUTTON, self.PlotEx )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def PlotEx( self, event ):
        import pandas as pd
        
        ### plot in one axes
        ser = pd.Series([1, 3, 2, 1, 2, 3, 4, 5, 2])
        ser.plot(ax=self.ax1, legend=True)
        self.ax1.set(xlabel='X axis label', ylabel='Y axis')
        drawPlot(self.fig1, self.canvas1)
        
        
        ### plot in two axes
        ser1 = -ser
        ser2 = ser1.diff()
        ser1.plot(ax=self.ax2[0])
        ser2.plot(ax=self.ax2[1])
        self.ax2[0].set_title('subplot1')
        self.ax2[1].set_title('subplot2')
        drawPlot(self.fig2, self.canvas2)
        
        
def drawPlot(fig, canvas):
    # refresh the canvas to make plot
    fig.tight_layout()
    canvas.draw()

def addFigAx2Panel(panel, *args, **kw_args):    
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg 
    # add a figure and axes to a wxPanel
    sizer = wx.BoxSizer(wx.VERTICAL)
    fig, ax = plt.subplots(*args, **kw_args)
    canvas = FigureCanvasWxAgg(panel, -1, fig)
    sizer.Add(canvas, 1, wx.EXPAND)
    panel.SetSizer(sizer)
    return fig, ax, canvas


if __name__ == '__main__':
    app = wx.App(redirect=True)
    frm = MyFrame1(None)
    frm.Show()
    app.MainLoop()
