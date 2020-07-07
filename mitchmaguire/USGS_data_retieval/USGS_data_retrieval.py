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
import os
import datetime

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar

###########################################################################
## Class MainFrame
###########################################################################


class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"USGS Data Retrieval", pos = wx.DefaultPosition, size = wx.Size( 1373,731 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"USGS: Station ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer9.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.station_ID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.station_ID, 0, wx.ALL, 5 )

        self.download = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.download, 0, wx.ALL, 5 )

        self.StartDate = wx.StaticText( self, wx.ID_ANY, u"Starting Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.StartDate.Wrap( -1 )

        bSizer9.Add( self.StartDate, 0, wx.ALL, 5 )

        self.startDate = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        bSizer9.Add( self.startDate, 0, wx.ALL, 5 )

        self.EndDate = wx.StaticText( self, wx.ID_ANY, u"Ending Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.EndDate.Wrap( -1 )

        bSizer9.Add( self.EndDate, 0, wx.ALL, 5 )

        self.endDate = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        bSizer9.Add( self.endDate, 0, wx.ALL, 5 )

        self.OutFolder = wx.StaticText( self, wx.ID_ANY, u"Out Folder", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.OutFolder.Wrap( -1 )

        bSizer9.Add( self.OutFolder, 0, wx.ALL, 5 )

        self.outdir = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        bSizer9.Add( self.outdir, 0, wx.ALL, 5 )


        bSizer8.Add( bSizer9, 0, 0, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        m_radioBox1Choices = [ u"Daily", u"Monthly", u"Annual" ]
        self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
        self.m_radioBox1.SetSelection( 0 )
        bSizer10.Add( self.m_radioBox1, 0, wx.ALL, 5 )

        m_radioBox2Choices = [ u"Min", u"Max", u"Mean", u"Median", u"10th percentile", u"90th percentile" ]
        self.m_radioBox2 = wx.RadioBox( self, wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices, 1, wx.RA_SPECIFY_COLS )
        self.m_radioBox2.SetSelection( 2 )
        bSizer10.Add( self.m_radioBox2, 0, wx.ALL, 5 )

        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

        bSizer10.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer8.Add( bSizer10, 1, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid1.CreateGrid( 5, 5 )
        self.m_grid1.EnableEditing( True )
        self.m_grid1.EnableGridLines( True )
        self.m_grid1.EnableDragGridSize( False )
        self.m_grid1.SetMargins( 0, 0 )

        # Columns
        self.m_grid1.SetColSize( 0, 80 )
        self.m_grid1.SetColSize( 1, 120 )
        self.m_grid1.SetColSize( 2, 80 )
        self.m_grid1.SetColSize( 3, 80 )
        self.m_grid1.SetColSize( 4, 80 )
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
        bSizer11.Add( self.m_grid1, 0, wx.ALL, 5 )


        bSizer8.Add( bSizer11, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer8 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.download.Bind( wx.EVT_BUTTON, self.download_data )
        self.m_radioBox1.Bind( wx.EVT_RADIOBOX, self.changeFreq )
        self.m_radioBox2.Bind( wx.EVT_RADIOBOX, self.changeStat )
        
        #### keep linese below for graph
        self.m_panel2.figure = matplotlib.figure.Figure()
        self.axes = self.m_panel2.figure.add_subplot(111)
        
    

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def download_data( self, event ):
       
        
        print('USGS station ID:{}'.format(self.station_ID.GetValue()))
        
        gauge=self.station_ID.GetValue()
        #gauge= '06803495'
        begin_date= self.startDate.GetValue()
        end_date=self.endDate.GetValue()
        
        print(type(end_date))
        
        end_date=datetime.datetime.strptime(str(end_date).split(' ')[0], '%m/%d/%Y').strftime('%Y-%m-%d')
        begin_date=datetime.datetime.strptime(str(begin_date).split(' ')[0], '%m/%d/%Y').strftime('%Y-%m-%d')
        print(begin_date)
        print(end_date)
                
        gauge = '&site_no={}'.format(gauge)
        #period = '&period=&begin_date={}&end_date={}'.format('2000-01-01','2019-12-31')
        period = '&period=&begin_date={}&end_date={}'.format(begin_date, end_date)
        url = 'https://waterdata.usgs.gov/nwis/dv?&cb_00060=on&format=rdb{}&referred_module=sw{}'.format(gauge, period)
        
        print(url)
        
        self.dataflow = pd.read_csv(url, comment='#', header = 0, sep='\t')[1:].apply(lambda x: pd.to_numeric(x, errors='ignore') if x.name.endswith('_va') else x, axis=0)
        print(self.dataflow)
        self.dataflow.to_csv(os.path.join(self.outdir.GetPath(), self.station_ID.GetValue()), float_format='%.2f')

        pd.to_numeric(self.dataflow.set_index('datetime').iloc[:, 2]).plot(ax=self.axes)
        self.canvas = FigureCanvas(self.m_panel2, -1, self.m_panel2.figure)
        self.toolbar = NavigationToolbar(self.canvas)
            

    def newplot( self, rID, sID):
        df = pd.to_numeric(self.dataflow.set_index('datetime').iloc[:, 2])
        df.index = pd.DatetimeIndex(df.index)
        if rID ==0:
            df.plot(ax=self.axes)
        elif rID ==1:
            if sID==0:
                df.resample('M').min().plot(ax=self.axes)
            if sID==1:
                df.resample('M').max().plot(ax=self.axes)
            if sID==2:
                df.resample('M').mean().plot(ax=self.axes)
            if sID==3:
                df.resample('M').median().plot(ax=self.axes)
            if sID==4:
                df.resample('M').quantile(q=.1).plot(ax=self.axes)
            if sID==5:
                df.resample('M').quantile(q=.9).plot(ax=self.axes)

        else:
            if sID==0:
                df.resample('A').min().plot(ax=self.axes)
            if sID==1:
                df.resample('A').max().plot(ax=self.axes)
            if sID==2:
                df.resample('A').mean().plot(ax=self.axes)
            if sID==3:
                df.resample('A').median().plot(ax=self.axes)
            if sID==4:
                df.resample('A').quantile(q=.1).plot(ax=self.axes)
            if sID==5:
                df.resample('A').quantile(q=.9).plot(ax=self.axes)
        #print('ratio {},{}'.format(rID, sID))
        self.canvas = FigureCanvas(self.m_panel2, -1, self.m_panel2.figure)
        
    def changeFreq( self, event):
        self.axes.clear()
        global rID
        rID=event.GetInt()
        #print(rID)
        self.newplot(rID,sID)
        return rID

    def changeStat( self, event):
        self.axes.clear()
        global sID
        sID = event.GetInt()
        #print(sID)
        self.newplot(rID,sID)
        return sID
        
rID=0
sID=0
app = wx.App(redirect=True)
frame = MainFrame(parent=None)
frame.Show()
app.MainLoop()


