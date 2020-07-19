import wx
import wx.xrc
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg 

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 713,489 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Select Flow Data:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer6.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_filePicker2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 400,-1 ), wx.FLP_DEFAULT_STYLE )
		bSizer6.Add( self.m_filePicker2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Import and Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		self.m_button2.Bind(wx.EVT_BUTTON,self.onImport)

		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( bSizer6, 0, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		self.fig1 = plt.figure(figsize = (6,4))
		self.canvas1 = FigureCanvasWxAgg(self.m_panel1,-1,self.fig1)
		self.ax1 = self.fig1.add_subplot()
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.canvas1, 1, wx.EXPAND |wx.ALL)
		self.m_panel1.SetSizer(sizer)

		bSizer9.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )


		bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		m_radioBox1Choices = [ u"Monthly", u"Annual" ]
		self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, u"Aggregation Interval", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer8.Add( self.m_radioBox1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		self.m_radioBox1.Bind(wx.EVT_RADIOBOX,self.addPlot)

		bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		m_radioBox2Choices = [ u"Minimum", u"Maximum", u"Mean", u"Median", u"10th Percentile", u"90th Percentile" ]
		self.m_radioBox2 = wx.RadioBox( self, wx.ID_ANY, u"Statistic Plotted", wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox2.SetSelection( 2 )
		bSizer8.Add( self.m_radioBox2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		self.m_radioBox2.Bind(wx.EVT_RADIOBOX,self.addPlot)


		bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer8, 0, wx.EXPAND, 5 )


		bSizer5.Add( bSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

	def onImport(self,event):
		import pandas as pd

		data = pd.read_csv(self.m_filePicker2.GetPath(), sep = ',')
		data['DateTime'] = pd.to_datetime(data['DateTime'])
		time_index_data = data.set_index('DateTime')
		self.data = time_index_data

		print(self.data)
		print(self.data['Flow'])

		self.annual_stats, self.monthly_stats = getstats(self.data)
		print(self.annual_stats)
		print(self.monthly_stats)

		aggplotdata(self,self.annual_stats,self.monthly_stats,self.m_radioBox1.GetItemLabel(self.m_radioBox1.GetSelection()),self.m_radioBox2.GetItemLabel(self.m_radioBox2.GetSelection()))
	
	def addPlot(self,event):
		
		aggregation_selection = self.m_radioBox1.GetSelection()
		aggregation_method = self.m_radioBox1.GetItemLabel(aggregation_selection)

		stat_selection = self.m_radioBox2.GetSelection()
		stat_method = self.m_radioBox2.GetItemLabel(stat_selection)

		aggplotdata(self,self.annual_stats,self.monthly_stats,aggregation_method,stat_method)

def getstats(data):
	
	import pandas as pd
	import numpy as np

	flow_series = data['Flow'].apply(pd.to_numeric,errors = 'coerce')
	print(flow_series)

	annualstats = flow_series.resample('A').agg([np.nanmin,np.nanmax,np.nanmean,np.nanmedian,percentile(10),percentile(90)])
	monthlystats = flow_series.resample('M').agg([np.nanmin,np.nanmax,np.nanmean,np.nanmedian,percentile(10),percentile(90)])

	return annualstats, monthlystats

def percentile(n):
	def percentile_(x):
		import numpy as np
		return np.nanpercentile(x, n)
	percentile_.__name__ = f'percentile_{n}'
	return percentile_

def aggplotdata(self,annual_stats,monthly_stats,agg_method,stat_method):
		
	import pandas as pd
	import matplotlib.pyplot as plt

	plt.cla()

	if agg_method == 'Annual':
		if stat_method == 'Mean':
			annual_stats.reset_index().plot(x = 'DateTime', y = 'nanmean',ax = self.ax1)
			self.ax1.set_xlabel('Date (Year Changes Indicated)')
			self.ax1.set_ylabel('Discharge (ft^3/s)')
			self.ax1.legend(['Mean'])
		elif stat_method == 'Minimum':
			annual_stats.reset_index().plot(x = 'DateTime', y = 'nanmin', ax = self.ax1)
			self.ax1.set_xlabel('Date (Year Changes Indicated)')
			self.ax1.set_ylabel('Discharge (ft^3/s)')
			self.ax1.legend(['Minimum'])
		elif stat_method == 'Maximum':
			annual_stats.reset_index().plot(x = 'DateTime', y = 'nanmax', ax = self.ax1)
			self.ax1.set_xlabel('Date (Year Changes Indicated)')
			self.ax1.set_ylabel('Discharge (ft^3/s)')
			self.ax1.legend(['Maximum'])
		elif stat_method == 'Median':
			annual_stats.reset_index().plot(x = 'DateTime', y = 'nanmedian', ax = self.ax1)
			self.ax1.set_xlabel('Date (Year Changes Indicated)')
			self.ax1.set_ylabel('Discharge (ft^3/s)')
			self.ax1.legend(['Median'])
		elif stat_method == '10th Percentile':
			annual_stats.reset_index().plot(x = 'DateTime', y = 'percentile_10', ax = self.ax1)
			self.ax1.set_xlabel('Date (Year Changes Indicated)')
			self.ax1.set_ylabel('Discharge (ft^3/s)')
			self.ax1.legend(['10th Percentile'])
		elif stat_method == '90th Percentile':
			annual_stats.reset_index().plot(x = 'DateTime', y = 'percentile_90', ax = self.ax1)
			self.ax1.set_xlabel('Date (Year Changes Indicated)')
			self.ax1.set_ylabel('Discharge (ft^3/s)')
			self.ax1.legend(['90th Percentile'])
	elif agg_method == 'Monthly':
		if stat_method == 'Mean':
			monthly_stats.reset_index().plot(x = 'DateTime', y = 'nanmean',ax = self.ax1)
			self.ax1.set_xlabel('Date (Year Changes Indicated)')
			self.ax1.set_ylabel('Discharge (ft^3/s)')
			self.ax1.legend(['Mean'])
		elif stat_method == 'Minimum':
			monthly_stats.reset_index().plot(x = 'DateTime', y = 'nanmin', ax = self.ax1)
			self.ax1.set_xlabel('Date (Year Changes Indicated)')
			self.ax1.set_ylabel('Discharge (ft^3/s)')
			self.ax1.legend(['Minimum'])
		elif stat_method == 'Maximum':
			monthly_stats.reset_index().plot(x = 'DateTime', y = 'nanmax', ax = self.ax1)
			self.ax1.set_xlabel('Date (Year Changes Indicated)')
			self.ax1.set_ylabel('Discharge (ft^3/s)')
			self.ax1.legend(['Maximum'])
		elif stat_method == 'Median':
			monthly_stats.reset_index().plot(x = 'DateTime', y = 'nanmedian', ax = self.ax1)
			self.ax1.set_xlabel('Date (Year Changes Indicated)')
			self.ax1.set_ylabel('Discharge (ft^3/s)')
			self.ax1.legend(['Median'])
		elif stat_method == '10th Percentile':
			monthly_stats.reset_index().plot(x = 'DateTime', y = 'percentile_10', ax = self.ax1)
			self.ax1.set_xlabel('Date (Year Changes Indicated)')
			self.ax1.set_ylabel('Discharge (ft^3/s)')
			self.ax1.legend(['10th Percentile'])
		elif stat_method == '90th Percentile':
			monthly_stats.reset_index().plot(x = 'DateTime', y = 'percentile_90', ax = self.ax1)
			self.ax1.set_xlabel('Date (Year Changes Indicated)')
			self.ax1.set_ylabel('Discharge (ft^3/s)')
			self.ax1.legend(['90th Percentile'])
	
	drawPlot(self.fig1,self.canvas1)

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
	sizer.Add(canvas, 1, wx.EXPAND |wx.ALL)
	panel.SetSizer(sizer)
	return fig, ax, canvas

if __name__ == '__main__':
	app = wx.App(redirect=True)
	frm = MyFrame2(None)
	frm.Show()
	app.MainLoop()
