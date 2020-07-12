import wx
import wx.xrc
import wx.adv
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 721,512 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Station ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		bSizer2.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Start Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_datePicker1 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer2.Add( self.m_datePicker1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		# self.m_datePicker1.Bind(wx.adv.EVT_DATE_CHANGED,self.printDate)

		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"End Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_datePicker2 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer2.Add( self.m_datePicker2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Import", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )
		self.m_button2.Bind(wx.EVT_BUTTON,self.onImport)


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

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
		bSizer3.Add( self.m_grid1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Select File Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer4.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_dirPicker2 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 450,-1 ), wx.DIRP_DEFAULT_STYLE )
		bSizer4.Add( self.m_dirPicker2, 0, wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Save File", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button1, 0, wx.ALL, 5 )
		self.m_button1.Bind(wx.EVT_BUTTON,self.onSaveFile)

		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass
	
	def printDate(self,event):
		import datetime
		print(self.m_datePicker1.GetValue())

		date = self.m_datePicker1.GetValue()
		print(date.Format('%Y-%m-%d'))

	def onImport(self,event):

		data_returned = getdata(self.m_textCtrl1.GetValue(),self.m_datePicker1.GetValue(),self.m_datePicker2.GetValue())
		# print(data_returned)

		self.data = data_returned
		showdata(self,self.data)

	def onSaveFile(self,event):
		import pandas as pd
		import string

		start_date = self.m_datePicker1.GetValue()
		start_date = start_date.Format('%Y-%m-%d')
		end_date = self.m_datePicker2.GetValue()
		end_date = end_date.Format('%Y-%m-%d')

		directory = self.m_dirPicker2.GetPath()
		filename = f'Station{self.m_textCtrl1.GetValue()}_RunoffData_{start_date}to{end_date}.csv'
		filepath = directory + '\\' + filename
		data = self.data
		data.to_csv(filepath,sep = ',')

def getdata(site_id,start_date,end_date):
	import string
	import pandas as pd
	import datetime

	url = 'https://waterdata.usgs.gov/nwis/dv?&cb_00060=on&format=rdb&'
	str1 = 'site_no={}&'.format(site_id)
	url = url + str1

	start_date = start_date.Format('%Y-%m-%d')
	end_date = end_date.Format('%Y-%m-%d')
	period = 'period=&begin_date={}&end_date={}'.format(start_date,end_date)
	url = url + period

	data = pd.read_csv(url,sep = '\t',names = ['Agency','Site_No','DateTime','Flow','Value'],comment = '#')
	data = data.drop(data[data['DateTime'] == '20d'].index)
	data = data.drop(data[data['DateTime'] == 'datetime'].index)

	return data

def showdata(self,input_data):
	import pandas as pd
	
	dimensions = input_data.shape
	# print(dimensions)

	current_rows = self.m_grid1.GetNumberRows()
	current_columns = self.m_grid1.GetNumberCols()
	new_rows = dimensions[0] - current_rows
	new_columns = dimensions[1] - current_columns
	self.m_grid1.AppendRows(new_rows)
	self.m_grid1.AppendCols(new_columns) 

	for i in range(dimensions[0]):
		for j in range(dimensions[1]):
			self.m_grid1.SetCellValue(i,j,str(input_data.iloc[i,j]))

if __name__ == '__main__':
	app = wx.App(redirect=True)
	frm = MyFrame1(None)
	frm.Show()
	app.MainLoop()