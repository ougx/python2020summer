import wx
import wx.xrc
import pandas as pd
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

import datetime

from sys import version
if version > '3':
    from urllib.request import urlopen

else:
    from urllib2 import urlopen


def read_usgs_rdb(filepath_or_link): 
    return pd.read_csv(filepath_or_link, comment='#', header=0, sep='\t')[1:].apply(lambda x: pd.to_numeric(x, errors='ignore') if x.name.endswith('_va') else x, axis=0)


def create_streamflow_url(gauge_list, begin_date='1900-01-01', end_date='2019-12-31', step='D'):
    if type(gauge_list) is not list:
        raise TypeError('The gagelist must be a list type.')

    if gauge_list == []:
        raise ValueError('The gagelist must not be an empty list.')
        
    if step == 'D':
        gages = ('&site_no={}' * len(gauge_list)).format(*gauge_list)
        period = '&period=&begin_date={}&end_date={}'.format(begin_date, end_date)
        url = 'https://waterdata.usgs.gov/nwis/dv?&cb_00060=on&format=rdb{}&referred_module=sw{}'.format(gages, period)
    elif step == 'M':
        gages = ''.join(['&site_no={0}&por_{0}_93535=594467,00060,93535,{1:.7},{2:.7}'.format(g, begin_date, end_date)  for g in gauge_list])
        url = 'https://waterdata.usgs.gov/nwis/monthly?referred_module=sw&format=rdb{}'.format(gages)  
    return url


def read_usgs_flow(gauge_list, begin_date='1900-01-01', end_date='2019-12-31', step='D'):
    
    print('Requested gauges: ', gauge_list)
    print('Requested period: ', begin_date, end_date)    

    try:
        bdate = datetime.datetime.strptime(begin_date, '%Y-%m-%d')
        edate = datetime.datetime.strptime(end_date,   '%Y-%m-%d')
    except:
        raise ValueError ("The input formats for the begin_date:{} and end_date:{} must be YYYY-MM-DD".format(begin_date, end_date))

    url = create_streamflow_url(gauge_list, begin_date, end_date, step)

    print('\nDownloading USGS observed streamflow data:')
    print(url, '\n')


    df = read_usgs_rdb(url).drop('agency_cd', axis=1)
    if step != 'D':
        df['datetime'] = df.apply(lambda x: datetime.datetime(int(x.year_nu), int(x.month_nu), 1), axis=1)
        df.drop(['year_nu', 'month_nu', 'parameter_cd', 'ts_id'], axis=1, inplace=True)
    df.set_index('datetime', inplace=True)
    
    f_url = urlopen(url)
    lines = [f_url.readline() for i in range(1000 + len(gauge_list))]
    f_url.close()
    gauge_names = dict()

    # read name of the gauge
    def find_site_name(gauge_no):
        for l in lines: 
            if gauge_no.encode() in l: 
                return l
        
    for g in gauge_list:
        l = find_site_name(g)
        gauge_names[g] = l.strip().lstrip(b'#').strip().decode()        

    return df, gauge_names


class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 672,423 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl1, 1, wx.ALL, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Download&Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button1, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel1.figure = matplotlib.figure.Figure()
        self.axes = self.m_panel1.figure.add_subplot(111)
          


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        self.Bind(wx.EVT_BUTTON, self.download_usgs, self.m_button1)

    def download_usgs(self, event):
            station_id = self.m_textCtrl1.GetValue()
            df, names = read_usgs_flow([station_id])
            pd.to_numeric(df.iloc[:, 1]).plot(ax=self.axes)
            print(df.head())
            self.canvas = FigureCanvas(self.m_panel1,-1,self.m_panel1.figure)
    def __del__( self ):
        pass

if __name__ == '__main__':
    app = wx.App(redirect=True)
    frm = MyFrame1(None)
    frm.Show()
    app.MainLoop()

