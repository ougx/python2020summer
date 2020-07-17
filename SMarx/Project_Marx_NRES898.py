
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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Rate Error Display", pos = wx.DefaultPosition, size = wx.Size( 1800,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText71.Wrap( -1 )

        bSizer12.Add( self.m_staticText71, 0, wx.ALL, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL, 5 )


        bSizer2.Add( bSizer12, 1, wx.EXPAND, 5 )

        bSizer20 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Average Rater Error (%)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer20.Add( self.m_staticText5, 0, wx.ALL, 5 )

        bSizer21 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer21.Add( self.m_textCtrl1, 0, wx.ALL, 5 )


        bSizer20.Add( bSizer21, 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer20, 1, wx.EXPAND, 5 )

        bSizer23 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Max Rate Error (%)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        bSizer23.Add( self.m_staticText7, 0, wx.ALL, 5 )

        bSizer24 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer24.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


        bSizer23.Add( bSizer24, 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer23, 1, wx.EXPAND, 5 )


        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

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
        Q1=self.ShapeData[choice2].quantile(0.05)
        Q3=self.ShapeData[choice2].quantile(0.95)
        IQR=Q3-Q1
        self.ShapeData=self.ShapeData[~(self.ShapeData[choice2]>(Q3+1.5*IQR))]#Removes only upper outliers
        #ShapeData=ShapeData[~((ShapeData.Rt_Apd_Ct_<(Q1-1.5*IQR))|(ShapeData.Rt_Apd_Ct_>(Q3+1.5*IQR)))]##Removes lower and upper outliers

        
        #print(max(ShapeData['Rt_Apd_Ct_']))
        self.ShapeData['RateError']=((self.ShapeData[choice2] - self.ShapeData[choice1])/self.ShapeData[choice1])*100
        avg_RateError1=(self.ShapeData['RateError']).mean()
        avg_RateError='{0:.3f}'.format(avg_RateError1)
        print("The avergae rate error is", avg_RateError,'%')
        Max_Error='{0:.3f}'.format(max(self.ShapeData['RateError']))
        print(Max_Error)
        Max_Applied=max(self.ShapeData['Rt_Apd_Ct_'])
        
        self.m_textCtrl1.ChangeValue(str(avg_RateError))
        self.m_textCtrl2.ChangeValue(str(Max_Error))
        
        self.figure, self.ax = plt.subplots(1, 4, figsize=(27,15))
        self.canvas=FigureCanvasWxAgg(self.m_panel5, -1, self.figure)
        sizer=wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(sizer)
        
        #fig.tight_layout()
        #canvas.draw()
         
        # canvas=FigureCanvasWxAgg(self.m_panel5, -1, self.figure)
        # sizer.Add(canvas, 1, wx.EXPAND)
        # self.m_panel5.SetSizer(sizer)
       
        #Target Rate
        cmap_1=plt.get_cmap('jet',10)
        self.ShapeData.plot(ax=self.ax[0],column=choice1, cmap=cmap_1, vmin=0, vmax=Max_Applied, markersize=2, legend=True, legend_kwds={'label':"Target Rate", 'orientation':"horizontal"});
        self.ax[0].set_title('Target Rate', fontsize=15)
        self.ax[0].set_xlabel('Longitude', fontsize=10)
        self.ax[0].set_ylabel('Latitude', fontsize=10)
        #self.ax[0].tick_params(labelsize=5)
        
        #Applied Rate
        cmap_2=plt.get_cmap('jet',10)
        self.ShapeData.plot(column=choice2, ax=self.ax[1],cmap=cmap_2, vmin=0, vmax=Max_Applied, markersize=2, legend=True, legend_kwds={'label':"Applied Rate", 'orientation':"horizontal"});#for some reason fontsize won't work as in this example: https://dmnfarrell.github.io/plotting/categorical-geopandas-maps
        self.ax[1].set_title('Applied Rate', fontsize=15)
        self.ax[1].set_xlabel('Longitude', fontsize=10)
        self.ax[1].set_ylabel('Latitude', fontsize=10)
        
        #Rate Error
        cmap_3=plt.get_cmap('jet',10)#where number after 'jet' is the number of values to be in the legend
        self.ShapeData.plot(ax=self.ax[2], column='RateError', cmap=cmap_3, vmin=-10, vmax=10, markersize=2, legend=True, legend_kwds={'label':"Rate Percent Error", 'orientation':"horizontal"});#Vmin and Vmax set bounds for legend values.  
        self.ax[2].set_title('Rate Percent Error', fontsize=15)
        self.ax[2].set_xlabel('Longitude', fontsize=10)
        self.ax[2].set_ylabel('Latitude', fontsize=10)

        #Speed
        cmap4=mpl.colors.ListedColormap(['green', 'yellow', 'orange', 'red', 'purple'])
        self.ShapeData.plot(column=choice3, ax=self.ax[3], cmap=cmap4, markersize=2, legend=True, legend_kwds={'label':"Speed (mph)", 'orientation':"horizontal"});
        self.ax[3].set_title('Application Speed', fontsize=15)
        self.ax[3].set_xlabel('Longitude', fontsize=10)
        self.ax[3].set_ylabel('Latitude', fontsize=10)


app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = MyFrame1(None) # A Frame is a top-level window.
frame.Show(True)
app.MainLoop()



