To make plots with wxPython:

1. create a `wxPanel` using wxFormBuilder (assuming the name of the panel is `m_panel1`)

2. call the `addFigAx2Panel` function to add axes to this panel, e.g. 
`self.fig, self.ax, self.canvas = addFigAx2Panel(self.m_panel1)`

3. do your magic to make plots with `self.ax` e.g. `self.ax.plot(1, 2, 3)` or `df.plot(ax=self.ax)`

4. call the `drawPlot` function to refresh the app to show the plot e.g. `drawPlot(self.fig, self.canvas)`

### Codes for your project:

```python
def drawPlot(fig, canvas):
    # refresh the canvas to make plot
    fig.tight_layout()
    canvas.draw()

def addFigAx2Panel(panel, *args, **kw_args):    
    # add a figure and axes to a wxPanel
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg 
    sizer = wx.BoxSizer(wx.VERTICAL)
    fig, ax = plt.subplots(*args, **kw_args)
    canvas = FigureCanvasWxAgg(panel, -1, fig)
    sizer.Add(canvas, 1, wx.EXPAND)
    panel.SetSizer(sizer)
    return fig, ax, canvas
```
    
    


### Example:

wxFormBuilder: https://github.com/ougx/python2020summer/raw/master/example/wxPythonMatplotlib.fbp

Scripts: https://github.com/ougx/python2020summer/blob/master/example/wxPythonMatplotlib.py
    
