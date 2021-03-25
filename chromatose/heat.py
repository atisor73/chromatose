import os
import numpy as np
import pandas as pd

import bokeh.io
import bokeh.plotting
from bokeh.models import ColorBar, LinearColorMapper

from .utils import *
from .interpolate import *


# reading in volcanic data..........................................................
_path = os.path.join(os.path.dirname(__file__), 'volcanoes.csv')
_df = pd.read_csv(_path)
_df.reset_index(level=0, inplace=True)
_df = _df.drop(columns=' 1 ')
_df = _df.melt(id_vars='index')
_df = _df.rename(columns={'index':'row','variable':'col'})
_df = _df.astype('float')


def heatmap(
    palette,
    interpolate=True,
    n_colors=256,
    interpolation_method='rgb',
    curve=False,
    directions=['up','down','up'],
    return_palette=False,
    return_plot=False
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
        To set size of final interpolation, can modify 'n_colors'
    n_colors : integer
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
    return_palette : boolean
        if True, returns interpolated palette as list
        if False, no returns

    Returns
    --------
    outputs plot directly, no returns unless return_palette is set to True
    """
    palette = list(palette)
    palette = hex_palette(palette)

    if interpolate == True:
        colors = palpolate( palette,
                            n_colors,
                            method=interpolation_method,
                            curve=curve,
                            directions=directions )

    else: colors = palette

    mapper = LinearColorMapper( palette=colors,
                                low=_df.value.min(),
                                high=_df.value.max() )

    # formatting TOOLTIPS...............................................................
    hex_str_dict = {}
    for value in np.unique(_df.value):
        fraction = (value-_df.value.min())/(_df.value.max()-_df.value.min())
        index = int(np.round(fraction*len(mapper.palette)))
        hex_str = mapper.palette[index-1]
        hex_str_dict[value] = hex_str
    hex_strs = [hex_str_dict[value] for value in _df.value]
    _df['color'] = hex_strs
    _df['rgb'] = hex_to_rgb(hex_strs)
    TOOLTIPS = """
        <div>
            <div>
                <span style="font-size:15px; font-weight:bold; color:midnightblue;">color: @color</span> <br>
                <span style="font-size:12px; margin-left:3em; font-weight:bold; color:lapisblue;">(@rgb)</span> <br>
            </div>
        </div>
        """

    # PLOTTING...........................................................................
    p = bokeh.plotting.figure(width=600, height=300,
                          x_range=(_df.row.min()+1, _df.row.max()),
                          y_range=(_df.col.min()+1, _df.col.max()),
                          tooltips=TOOLTIPS
                         )
    p.rect(source=_df, x='row', y='col',
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

    if return_plot == True:
        return p
    else:
        bokeh.io.show(p)

    if return_palette == True:
        return colors
