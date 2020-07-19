# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid
import pandas as pd
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
###########################################################################
## Class UNLWx
###########################################################################

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid

###########################################################################
## Class UNLWx
###########################################################################

class UNLWx ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 893,524 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.dateBegin = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer2.Add( self.dateBegin, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Ending Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.dateEnd = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer2.Add( self.dateEnd, 0, wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"USGS Station ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txtID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.txtID, 0, wx.ALL, 5 )

		self.btnDownload = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnDownload, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		m_radioBox1Choices = [ u"Daily", u"Monthly", u"Annual" ]
		self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer3.Add( self.m_radioBox1, 0, wx.ALL, 5 )


		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		self.m_panel1.figure = matplotlib.figure.Figure()
		self.axes = self.m_panel1.figure.add_subplot(111)


		bSizer3.Add( self.m_panel1, 2, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer3, 2, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer5.Add( self.m_grid1, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnDownload.Bind( wx.EVT_BUTTON, self.downloadData )
		self.m_radioBox1.Bind( wx.EVT_RADIOBOX, self.changeFreq )
	def __del__( self ):
		pass


    # Virtual event handlers, overide them in your derived class
	def downloadData( self, event ):
        #print('USGS ID {}'.format(self.txtID.GetValue()))
		gages = '&site_no={}'.format(self.txtID.GetValue())
		period = '&period=&begin_date={}&end_date={}'.format('2000-01-01', '2019-12-31')
		url = "https://waterdata.usgs.gov/nwis/dv?&cb_00060=on&format=rdb{}&referred_module=sw{}".format(gages, period)
        
		self.dataflow = pd.read_csv(url, comment='#', header=0, sep='\t')[1:].apply(lambda x: pd.to_numeric(x, errors='ignore') if x.name.endswith('_va') else x, axis=0)
		print(self.dataflow)
		
		pd.to_numeric(self.dataflow.set_index('datetime').loc[:, 2]).plot(ax=self.axes)
        
		self.canvas = FigureCanvas(self.m_panel1, -1, self.m_panel1.figure)

	def changeFreq( self, event ):
		self.axes.clear()
		rID = event.GetInt()
		df = pd.to_numeric(self.dataflow.set_index('datetime').iloc[:, 2])
		df.index = pd.DatetimeIndex(df.index)
		if rID == 0:
		  df.plot(ax=self.axes)
		elif rID == 1:
		  df.resample('M').mean().plot(ax=self.axes)
		else:
		  df.resample('A').mean().plot(ax=self.axes)
		self.canvas = FigureCanvas(self.m_panel1, -1, self.m_panel1.figure)

		print('ratio is {}'.format(event.GetInt()))

if __name__ == '__main__':
    app = wx.App(redirect=True)
    frame = UNLWx(None)
    frame.Show()
    app.MainLoop()

# app = wx.App(redirect=True)
# frame = frameUNLWx(None)
# frame.Show()
# app.MainLoop()
