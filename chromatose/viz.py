import warnings

import numpy as np
import pandas as pd
import scipy.stats
import bokeh.io
import bokeh.plotting

from .utils import *
from . import heat
from . import palettes

try:
    import panel as pn     # see if panel is installed
#    pn.extension()
    _panel = True
except:
    _panel = False


def _clean_plot(p, bg_color):
    p.background_fill_color=bg_color
    p.axis.visible=False
    p.grid.grid_line_color=None
    p.toolbar.autohide=True
    return p

def _generate_scatter(x_range, size, slope=1, glyph="circle"):
    x = np.random.uniform(low=x_range[0],high=x_range[1],size=size)
    y = slope*x

    if glyph == "circle":
        x_error = np.random.choice([-1,1])*np.random.random(size=size)
        mu, sigma = 0, np.random.random(size)
        y_error = mu + sigma * np.random.standard_cauchy(size=size)

    elif glyph == "triangle":
        x_error = np.random.choice([-1,1],size=size)*np.random.lognormal(-0.5,1,size=size)
        c = np.random.choice([-1,1],size=size)*np.random.random(size)
        y_error = np.random.exponential(0.7,size=size)
    x += x_error
    y += y_error
    return np.abs(x), np.abs(y)

def _rug(x, y, p, color):
    rug_range_x, rug_range_y = (-0.6,-0.3), (-0.6,-0.2)
    rug_thick = 1.4
    rug_alpha = 0.8
    xx, yy = [(_x,_x) for _x in x], [rug_range_y for _ in x]        # along x-axis
    p.multi_line(xx, yy, color=color, line_width=rug_thick, alpha=rug_alpha)
    xx, yy = [rug_range_x for _ in x], [(_y,_y) for _y in y]        # along y-axis
    p.multi_line(xx, yy, color=color, line_width=rug_thick, alpha=rug_alpha)
    pass



def swatch(
    palette,
    alpha=1.0,
    ):
    """
    Displays palette via bokeh. Hover for hex/rgb value.

    Arguments
    ---------
    palette : list or iterable
         list of hex strings or rgb tuples or HTML names, any combination
    alpha : fraction between 0.0 and 1.0
        alpha transparency of entire palette
    Returns
    ---------
    output : displays plot, no return
    """
    TOOLTIPS = """
            <div>
                <div>
                    <span style="font-size:15px; font-weight:bold; color:midnightblue;">@palette</span> <br>
                    <span style="font-size:12px; font-weight:bold; color:lapisblue;">(@rgb)</span> <br>
                </div>
            </div>
            """
    palette = hex_palette(palette)
    df = pd.DataFrame(dict(palette=palette,
                       x=np.arange(len(palette)),
                       y=[0]*len(palette)  ))

    df['hex']=palette
    df['rgb']=hex_to_rgb(palette)

    height = 62
    width = height*len(palette)+60
    if len(palette) > 5: width = 62*len(palette)
    if len(palette) > 10: width=650

    size = height/1.2
    p = bokeh.plotting.figure(width=width, height=height,
                                   x_range=(-1,len(palette)),
                                   y_range=(-height,height),
                                   tooltips=TOOLTIPS)
    p.square(source=df, x='x',y='y', size=size, color='palette',alpha=alpha)
    p = _clean_plot(p, 'white')
    bokeh.io.show(p)



def palplot(
    palette,
    plot='all',
    bg_color="white",
    alpha=1.0,
    shuffle=False,
    scatter_kwargs=None,
    ):
    """
    Displays palette via bokeh.
    Hover for hex/rgb value.

    Arguments
    ---------
    palette : list or iterable
         list of hex strings or rgb tuples or HTML names, any combination
    plot :
        'swatch' for squares,
        'pie' for wedges (adjacency comparison),
        'points' for some points,
        'line' for some lines,
        'scatter' for a scatterplot,
        'all' for all (with dropdown menu for lines/points/scatter)
    bg_color : valid HTML string name or hex string, default "white"
        background fill color
    alpha : fraciton between 0.0 and 1.0, default 1.0
        alpha transparency of entire palette,
    shuffle : boolean, default False
        shuffles palette
    scatter_kwargs : dictionary,
        'click_policy' : boolean, default False
            if True, legend is on plot and can click/hide
            if False, legend is offside, no overlap

    Returns
    --------
    output : if panel is installed, returns panel layout
             if panel is not installed, displays plot, no returns
    """
    # HOVER FORMAT STRING (for swatch and pie plots)
    TOOLTIPS = """
            <div>
                <div>
                    <span style="font-size:15px; font-weight:bold; color:midnightblue;">@palette</span> <br>
                    <span style="font-size:12px; font-weight:bold; color:lapisblue;">(@rgb)</span> <br>
                </div>
            </div>
            """

    palette = list(palette)
    if shuffle == True: np.random.shuffle(palette)

    try: _copy_palette = palette.copy()       # copy so legend displays original inputs
    except: raise TypeError("Palette should be a list or something")

    palette = hex_palette(palette)
    length = len(palette)

    # determining light-dark background for legend text
    bg_avg = (np.sum(hex_to_rgb(hex_palette([bg_color])[0]))/3)
    switch = False
    if bg_avg <= 100: switch = True

    def _swatch():
        df = pd.DataFrame(dict(palette=palette,
                           x=np.arange(len(palette)),
                           y=[0]*len(palette)  ))

        df['hex']=palette
        df['rgb']=hex_to_rgb(palette)

        height, width = 60, 300
        size = height/1.2
        p = bokeh.plotting.figure(width=width, height=height,
                                       x_range=(-1,len(palette)),
                                       y_range=(-height,height),
                                       tooltips=TOOLTIPS)
        p.square(source=df, x='x',y='y', size=size, color='palette',alpha=alpha)
        p = _clean_plot(p, 'white')
        return p

    def _pie():
        if len(palette) < 9:
            line_color = bg_color
            line_width = 0.5
        else:
            line_color = None
            line_width = 0.01


        width, height = 300, 300
        angles = [0.216875, 0.1545, 0.127375, 0.1069, 0.103925,
                 0.055875, 0.04665,0.0355, 0.032275, 0.03, 0.018975,
                 0.0131, 0.0128, 0.00925, 0.007075, 0.00635, 0.005125,
                 0.003825, 0.003525, 0.002925, 0.002, 0.0013, 0.001, 0.002875]

        df = pd.DataFrame(dict( angle=[a*2*np.pi for a in angles],
                                palette=(palette*12)[:len(angles)], ))

        if length > 8:
            wedges = np.array([1/length]*length*2)
            angles = wedges /np.sum(wedges)

            top = pd.DataFrame({'angle':[a*2*np.pi for a in angles[:int(len(angles)/2)]],
                                'palette':palette})
            bot = pd.DataFrame({'angle':[a*2*np.pi for a in angles[:int(len(angles)/2)]],
                                    'palette':palette[::-1]})
            df = pd.concat([top, bot])
        df['hex']=(palette*12)[:len(angles)]
        df['rgb']=hex_to_rgb((palette*12)[:len(angles)])

        p = bokeh.plotting.figure(width=width, height=height,
                                  x_range=(-1.1,1.1),tooltips=TOOLTIPS)
        p.wedge(x=0,y=0,radius=1,
                   start_angle=bokeh.transform.cumsum('angle',include_zero=True),
                   end_angle=bokeh.transform.cumsum('angle'),
                   line_color=line_color, # "palette", # -> (no spaces btw wedges)
                   line_width=line_width,
                   fill_color="palette",
                   fill_alpha=alpha,
                   source=df
               )
        p = _clean_plot(p, bg_color)
        return p

    def _points():

        n = 500
        x = np.linspace(0,8,n)
        ys, fits = np.empty((len(palette),n)), np.empty((len(palette),n))
        for i, _ in enumerate(palette):
            ys[i] = np.exp(np.power(x, i*0.1)) + np.random.uniform(-0.1*x, 0.1*x, size=len(x))
            fits[i] = np.exp(np.power(x, i*0.1)) + np.random.uniform(-0.01*x, 0.01*x, size=len(x))

        p = bokeh.plotting.figure(width=400,height=300)
        for i,y in enumerate(ys):
            p.circle(x,y,color=palette[i],size=3,
                     legend_label=f'{_copy_palette[i]}',alpha=alpha)
            p.line(x,fits[i],color=palette[i],line_width=3,
                   legend_label=f'{_copy_palette[i]}',line_alpha=alpha)

        p.legend.click_policy='hide'
        p.legend.location="top_left"
        p.legend.background_fill_color = bg_color
        if switch:
            p.legend.label_text_color = "lightgray"
        p = _clean_plot(p, bg_color)
        return p

    def _line():
        n = 500
        x = np.linspace(0,4,n)
        ys = np.empty((len(palette),n))
        for i, _ in enumerate(palette):
            ys[i] = scipy.stats.gamma.pdf(x, a=3, loc=0, scale=1/(i+1.4))

        p = bokeh.plotting.figure(width=400,height=300)

        if len(palette) < 11:
            for i,y in enumerate(ys):
                p.line(x,ys[i],color=palette[::-1][i],line_width=3.5,
                       legend_label=f'{_copy_palette[i]}',line_alpha=alpha)

            p.legend.click_policy='hide'
            p.legend.location="top_right"
            p.width=400

        else:
            for i,y in enumerate(ys):
                p.line(x,ys[i],color=palette[::-1][i],line_width=3.5,)

            legend = bokeh.models.Legend(
                    items=[(palette[i], [p.line(color=palette[i],
                                                line_width=3.5,
                                                line_alpha=alpha)])
                           for i in range(len(palette))],
                    location='center')
            p.add_layout(legend, 'right')
            p.width=525

        p = _clean_plot(p, bg_color)

        if bg_color!="white":
            p.xgrid.grid_line_color, p.ygrid.grid_line_color = None, None
            p.xaxis.visible, p.yaxis.visible = False,False
            p.xaxis.major_tick_line_color, p.yaxis.major_tick_line_color = None, None
            p.xaxis.minor_tick_line_color, p.yaxis.minor_tick_line_color = None, None
            p.legend.background_fill_color = bg_color
            if switch: p.legend.label_text_color = "lightgray"
        return p

    click_policy, fit_line = False, True
    try:
        if scatter_kwargs['click_policy'] == True: click_policy = True
        if scatter_kwargs['line'] == False:        fit_line = False
    except: pass

    # inspired by @jmaasch's scatter plots in R

    def _scatter():
        x_ranges = []                         # manually constructing ranges
        for _ in range(len(palette)):
            low = _*2.3
            high = low + 2
            x_ranges.append((low, high))
        x_ranges_flat = [_ for x_range in x_ranges for _ in x_range]
        xmin, xmax = min(x_ranges_flat), max(x_ranges_flat)

        p = bokeh.plotting.figure(x_range=(-0.6, 1.01*xmax),     # make plot
                                  y_range=(-0.6, 1.01*xmax),
                                  height=300,width=400,
                                 )
        size = 30
        # begin scattering and rugging
        for i, x_range in enumerate(x_ranges):
            x, y = _generate_scatter(x_range,size,glyph="circle")
            if click_policy == True:
                p.circle(x=x,y=y,color=palette[i],size=6,fill_alpha=0.8,legend_label=f"{palette[i]}")
            else: p.circle(x=x,y=y,color=palette[i],size=6,fill_alpha=0.8)
            _rug(x, y, p, palette[i])

            x,y = _generate_scatter(x_range,size,glyph="triangle")
            if click_policy == True:
                p.triangle(x=x,y=y,color=palette[i],size=6,alpha=1,legend_label=f"{palette[i]}")
            else: p.triangle(x=x,y=y,color=palette[i],size=6,alpha=1)
            _rug(x, y, p, palette[i])

        if fit_line: p.line(x=(0,500),y=(0,500),color='black')     # line_fit

        # cleaning
        p.xgrid.grid_line_color, p.ygrid.grid_line_color = None, None
        p.xaxis.visible, p.yaxis.visible = False,False
        p.xaxis.major_tick_line_color, p.yaxis.major_tick_line_color = None, None
        p.xaxis.minor_tick_line_color, p.yaxis.minor_tick_line_color = None, None
        p.toolbar.autohide=True
        p.background_fill_color=bg_color
        p.legend.background_fill_color=bg_color
        if switch:
            p.legend.label_text_color="lightgray"

        # fitting legend
        if click_policy == True:
            p.legend.click_policy='hide'
            p.legend.location="bottom_right"
            p.width=415
        else:
            legend = bokeh.models.Legend(
                    items=[(palette[i], [p.circle(color=palette[i])]) for i in range(len(palette))],
                    location='center')
            p.add_layout(legend, 'right')
            p.width=525
        return p

    if _panel == True:
        if len(palette) > 7:
            glyph = pn.widgets.Select(
                options=['lines','scatter','map'],
                width=375, margin=[3,4], value='lines')
        else:
            glyph = pn.widgets.Select(
                        options=['points','lines','scatter'],
                        width=375, margin=[3,4], value='points')
        @pn.depends(glyph.param.value)
        def data(glyph="points"):
            if glyph == "points": return _points()
            if glyph == "lines": return _line()
            if glyph == "scatter": return _scatter()
            map = heat.heatmap(palette, interpolate=False, return_plot=True)
            if glyph == "map": return map

    #**********************************************************************
    if len(palette) > 30:
        map = heat.heatmap(palette, interpolate=False, return_plot=True)
        spacer = bokeh.layouts.Spacer(height=20)
        bokeh.io.show(bokeh.layouts.layout([[[_pie(), _swatch()], [spacer, map]]]))
        return

    if plot=="swatch": return _swatch()
    if plot=="pie": return _pie()
    if plot=="points": return _points()
    if plot=="scatter": return _scatter()
    if plot=="line": return _line()

    if plot=="all":
        if _panel == True:
            return pn.Row(pn.Column(_pie(), _swatch()), pn.Column(glyph, data))
        elif _panel == False:
            bokeh.io.show(bokeh.layouts.layout([[_pie(), _points()], _swatch()]))
