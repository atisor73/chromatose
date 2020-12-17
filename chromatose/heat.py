import numpy as np
import pandas as pd

import bokeh.io
import bokeh.plotting
from bokeh.models import ColorBar, LinearColorMapper, BasicTicker, PrintfTickFormatter

from .utils import *
from .interpolate import *



# reading in volcanic data..........................................................
df = pd.read_csv('volcanoes.csv')
df.reset_index(level=0, inplace=True)
df = df.melt(id_vars='index')
df = df.rename(columns={'index':'row','variable':'col'})
df = df.astype('float')


def heatmap(
    palette,
    interpolate=True,
    desired_length=256,
    interpolation_method='rgb',
    curve=False,
    directions=['up','down','up'],
    ):
    """
    Displays heatmap via bokeh. Hover for hex/rgb value.
    
    Arguments
    ---------
    palette : list
        list of hex strings or rgb tuples or HTML names (any combination)
    interpolate : boolean
        If True, will interpolate the palette using palpolate
        If False, will generate heatmap with input palette
        To set size of final interpolation, can modify 'desired_length'
    desired_length : integer
         approximate desired length of final palette
    interpolation_method : string 'rgb' or 'hsv' or 'hsl'
         interpolation metric, default 'rgb'
    curve : boolean
        if True: fit to 2ndº polynomial
        if False: simple linear interpolation, default False
    directions : list of 3 strings, 'up' or 'down'
        each entry corresponds to r, g, b
        'up' pushes intermediate values higher (lighter)
        'down' pushes intermediate values lower (darker)
        
    Returns
    --------
    No returns, outputs plot directly.
    """
    
    if interpolate == True: colors = palpolate(palette,
                                               desired_length,
                                               method=interpolation_method,
                                               curve=curve,
                                               directions=directions
                                              )
    else: colors = palette
        
    mapper = LinearColorMapper(palette=colors, low=df.value.min(), high=df.value.max())
    
    # formatting TOOLTIPS...............................................................
    hex_str_dict = {}
    for value in np.unique(df.value):
        fraction = (value-df.value.min())/(df.value.max()-df.value.min())
        index = int(np.round(fraction*len(mapper.palette)))
        hex_str = mapper.palette[index-1]
        hex_str_dict[value] = hex_str
    hex_strs = [hex_str_dict[value] for value in df.value]
    df['color'] = hex_strs
    df['rgb'] = hex_to_rgb(hex_strs)
    TOOLTIPS = """
        <div>
            <div>
                <span style="font-size:15px; font-weight:bold; color:midnightblue;">color: @color</span> <br>
                <span style="font-size:12px; margin-left:3em; font-weight:bold; color:lapisblue;">(@rgb)</span> <br>
            </div>
        </div>
        """
    
    # PLOTTING...........................................................................
    p = bokeh.plotting.figure(width=720, height=350,
                          x_range=(df.row.min(), df.row.max()),
                          y_range=(df.col.min(), df.col.max()),
                          tooltips=TOOLTIPS
                         )
    p.rect(source=df, x='row', y='col',
           width=1, height=1,
           fill_color={'field': 'value', 'transform': mapper},
           line_color=None,
          )

    color_bar = ColorBar(color_mapper=mapper,
                         major_label_text_font_size="10px",
                         border_line_color=None,
                         location=(0, 0)
                        )
    p.add_layout(color_bar, 'right')
    p.grid.grid_line_color, p.axis.axis_line_color = None, None
    p.axis.major_tick_line_color = None
    p.xaxis.visible, p.yaxis.visible = False, False
    p.toolbar.autohide=True
    
    bokeh.io.show(p)
