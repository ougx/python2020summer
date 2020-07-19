# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 10:37:09 2020

@author: smarx2
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
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib as mpl

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 879,510 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Select File", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText41.Wrap( -1 )

        bSizer9.Add( self.m_staticText41, 0, wx.ALL, 5 )

        self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer9.Add( self.m_filePicker1, 0, wx.ALL, 5 )


        bSizer2.Add( bSizer9, 1, wx.EXPAND, 5 )

        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Select Target Rate", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer15.Add( self.m_staticText2, 0, wx.ALL, 5 )

        m_choice1Choices = []
        self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        bSizer15.Add( self.m_choice1, 0, wx.ALL, 5 )


        bSizer2.Add( bSizer15, 1, wx.EXPAND, 5 )

        bSizer16 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Select Applied Rate", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer16.Add( self.m_staticText3, 0, wx.ALL, 5 )

        m_choice2Choices = []
        self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 0 )
        bSizer16.Add( self.m_choice2, 0, wx.ALL, 5 )


        bSizer2.Add( bSizer16, 1, wx.EXPAND, 5 )

        bSizer17 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Select Speed", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer17.Add( self.m_staticText4, 0, wx.ALL, 5 )

        m_choice3Choices = []
        self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
        self.m_choice3.SetSelection( 0 )
        bSizer17.Add( self.m_choice3, 0, wx.ALL, 5 )


        bSizer2.Add( bSizer17, 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button1, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

        bSizer19 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer19.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer1.Add( bSizer19, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.m_filePicker1OnFileChanged )
        self.m_button1.Bind( wx.EVT_BUTTON, self.Plot )
        
        self.figure, self.ax = plt.subplots(1, 4)
        FigureCanvasWxAgg(self.m_panel5, -1, self.figure)

    # Virtual event handlers, overide them in your derived class
    def m_filePicker1OnFileChanged( self, event ):
        shapefile = self.m_filePicker1.GetPath() 
        self.ShapeData = gpd.read_file(shapefile)
        
        #print(ShapeData)
        headers=self.ShapeData.columns.values
        self.m_choice1.Clear()
        self.m_choice1.Append(headers)
        self.m_choice2.Clear()
        self.m_choice2.Append(headers)
        self.m_choice3.Clear()
        self.m_choice3.Append(headers)
        print(headers)

        
    def Plot( self, event ):
        #Target Rate     
        choice1 = self.m_choice1.GetStringSelection()
        print(choice1)
        #Max_Applied=max(choice1)
        #Applied Rate
        choice2 = self.m_choice2.GetStringSelection()
        print(choice2)
        #User Selected
        choice3 = self.m_choice3.GetStringSelection()
        print(choice3)
        
        #Remove outliers on Applied Rate
        # Q1=choice2.quantile(0.05)
        # Q3=choice2.quantile(0.95)
        # IQR=Q3-Q1
        # choice2=choice2[~(choice2>(Q3+1.5*IQR))]
        
        #print(max(ShapeData['Rt_Apd_Ct_']))
        # self.ShapeData['RateError']=((self.ShapeData(column=choice2) - self.ShapeData(column=choice1))/self.ShapeData(column=choice1))*100
        # avg_RateError=(self.ShapeData['RateError']).mean()
        # print("The avergae rate error is", avg_RateError,'%')
        #Max_Applied=max(ShapeData['Rt_Apd_Ct_'])
        
        #Target Rate
        cmap_1=plt.get_cmap('jet',10)
        self.ShapeData.plot(ax=self.ax[0],column=choice1, cmap=cmap_1, vmin=0, vmax=180, markersize=2, legend=True, legend_kwds={'label':"Target Rate", 'orientation':"horizontal"});
        self.ax[0].set_title('Target Rate', fontsize=30)
        self.ax[0].set_xlabel('Longitude', fontsize=20)
        self.ax[0].set_ylabel('Latitude', fontsize=20)
        self.ax[0].tick_params(labelsize=10)
        
        #Applied Rate
        cmap_2=plt.get_cmap('jet',10)
        self.ShapeData.plot(column=choice2, ax=self.ax[1],cmap=cmap_2, vmin=0, vmax=200, markersize=2, legend=True, legend_kwds={'label':"Applied Rate", 'orientation':"horizontal"});#for some reason fontsize won't work as in this example: https://dmnfarrell.github.io/plotting/categorical-geopandas-maps
        self.ax[1].set_title('Applied Rate', fontsize=30)
        self.ax[1].set_xlabel('Longitude', fontsize=20)
        self.ax[1].set_ylabel('Latitude', fontsize=20)
        
        # #Rate Error
        #cmap_3=plt.get_cmap('jet',10)#where number after 'jet' is the number of values to be in the legend
        # self.ShapeData.plot(ax=self.ax[2], column='RateError', cmap=cmap_3, vmin=-10, vmax=10, markersize=2, legend=True, legend_kwds={'label':"Rate Percent Error", 'orientation':"horizontal"});#Vmin and Vmax set bounds for legend values.  
        # self.ax[2].set_title('Rate Percent Error', fontsize=30)
        # self.ax[2].set_xlabel('Longitude', fontsize=20)
        # self.ax[2].set_ylabel('Latitude', fontsize=20)

        #Speed
        cmap4=mpl.colors.ListedColormap(['green', 'yellow', 'orange', 'red', 'purple'])
        self.ShapeData.plot(column=choice3, ax=self.ax[3], cmap=cmap4, markersize=2, legend=True, legend_kwds={'label':"Speed (mph)", 'orientation':"horizontal"});
        self.ax[3].set_title('Application Speed', fontsize=30)
        self.ax[3].set_xlabel('Longitude', fontsize=20)
        self.ax[3].set_ylabel('Latitude', fontsize=20)


app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = MyFrame1(None) # A Frame is a top-level window.
frame.Show(True)
app.MainLoop()



