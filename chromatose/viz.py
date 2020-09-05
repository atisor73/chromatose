import numpy as np
import pandas as pd
import scipy.stats
import bokeh.io
import bokeh.plotting
bokeh.io.output_notebook()

# see if panel is installed 
try:
    import panel as pn
    pn.extension()
    panel = True
except:
    panel = False


# dictionary for html names -> hex conversion
html_colors = {'black': '#000000',
 'navy': '#000080',
 'darkblue': '#00008b',
 'mediumblue': '#0000cd',
 'blue': '#0000ff',
 'darkgreen': '#006400',
 'green': '#008000',
 'teal': '#008080',
 'darkcyan': '#008b8b',
 'deepskyblue': '#00bfff',
 'darkturquoise': '#00ced1',
 'mediumspringgreen': '#00fa9a',
 'lime': '#00ff00',
 'springgreen': '#00ff7f',
 'cyan': '#00ffff',
 'midnightblue': '#191970',
 'dodgerblue': '#1e90ff',
 'lightseagreen': '#20b2aa',
 'forestgreen': '#228b22',
 'seagreen': '#2e8b57',
 'darkslategrey': '#2f4f4f',
 'limegreen': '#32cd32',
 'mediumseagreen': '#3cb371',
 'turquoise': '#40e0d0',
 'royalblue': '#4169e1',
 'steelblue': '#4682b4',
 'darkslateblue': '#483d8b',
 'mediumturquoise': '#48d1cc',
 'indigo': '#4b0082',
 'darkolivegreen': '#556b2f',
 'cadetblue': '#5f9ea0',
 'cornflowerblue': '#6495ed',
 'rebeccapurple': '#663399',
 'mediumaquamarine': '#66cdaa',
 'dimgrey': '#696969',
 'slateblue': '#6a5acd',
 'olivedrab': '#6b8e23',
 'slategrey': '#708090',
 'lightslategrey': '#778899',
 'mediumslateblue': '#7b68ee',
 'lawngreen': '#7cfc00',
 'chartreuse': '#7fff00',
 'aquamarine': '#7fffd4',
 'maroon': '#800000',
 'purple': '#800080',
 'olive': '#808000',
 'grey': '#808080',
 'skyblue': '#87ceeb',
 'lightskyblue': '#87cefa',
 'blueviolet': '#8a2be2',
 'darkred': '#8b0000',
 'darkmagenta': '#8b008b',
 'saddlebrown': '#8b4513',
 'darkseagreen': '#8fbc8f',
 'lightgreen': '#90ee90',
 'mediumpurple': '#9370db',
 'darkviolet': '#9400d3',
 'palegreen': '#98fb98',
 'darkorchid': '#9932cc',
 'yellowgreen': '#9acd32',
 'sienna': '#a0522d',
 'brown': '#a52a2a',
 'darkgrey': '#a9a9a9',
 'lightblue': '#add8e6',
 'greenyellow': '#adff2f',
 'paleturquoise': '#afeeee',
 'lightsteelblue': '#b0c4de',
 'powderblue': '#b0e0e6',
 'firebrick': '#b22222',
 'darkgoldenrod': '#b8860b',
 'mediumorchid': '#ba55d3',
 'rosybrown': '#bc8f8f',
 'darkkhaki': '#bdb76b',
 'silver': '#c0c0c0',
 'mediumvioletred': '#c71585',
 'indianred': '#cd5c5c',
 'peru': '#cd853f',
 'chocolate': '#d2691e',
 'tan': '#d2b48c',
 'lightgrey': '#d3d3d3',
 'thistle': '#d8bfd8',
 'orchid': '#da70d6',
 'goldenrod': '#daa520',
 'palevioletred': '#db7093',
 'crimson': '#dc143c',
 'gainsboro': '#dcdcdc',
 'plum': '#dda0dd',
 'burlywood': '#deb887',
 'lightcyan': '#e0ffff',
 'lavender': '#e6e6fa',
 'darksalmon': '#e9967a',
 'violet': '#ee82ee',
 'palegoldenrod': '#eee8aa',
 'lightcoral': '#f08080',
 'khaki': '#f0e68c',
 'aliceblue': '#f0f8ff',
 'honeydew': '#f0fff0',
 'azure': '#f0ffff',
 'sandybrown': '#f4a460',
 'wheat': '#f5deb3',
 'beige': '#f5f5dc',
 'whitesmoke': '#f5f5f5',
 'mintcream': '#f5fffa',
 'ghostwhite': '#f8f8ff',
 'salmon': '#fa8072',
 'antiquewhite': '#faebd7',
 'linen': '#faf0e6',
 'lightgoldenrodyellow': '#fafad2',
 'oldlace': '#fdf5e6',
 'red': '#ff0000',
 'magenta': '#ff00ff',
 'deeppink': '#ff1493',
 'orangered': '#ff4500',
 'tomato': '#ff6347',
 'hotpink': '#ff69b4',
 'coral': '#ff7f50',
 'darkorange': '#ff8c00',
 'lightsalmon': '#ffa07a',
 'orange': '#ffa500',
 'lightpink': '#ffb6c1',
 'pink': '#ffc0cb',
 'gold': '#ffd700',
 'peachpuff': '#ffdab9',
 'navajowhite': '#ffdead',
 'moccasin': '#ffe4b5',
 'bisque': '#ffe4c4',
 'mistyrose': '#ffe4e1',
 'blanchedalmond': '#ffebcd',
 'papayawhip': '#ffefd5',
 'lavenderblush': '#fff0f5',
 'seashell': '#fff5ee',
 'cornsilk': '#fff8dc',
 'lemonchiffon': '#fffacd',
 'floralwhite': '#fffaf0',
 'snow': '#fffafa',
 'yellow': '#ffff00',
 'lightyellow': '#ffffe0',
 'ivory': '#fffff0',
 'white': '#ffffff'}


def hex_to_rgb(palette):
    return [tuple(int(h.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)) for h in palette]


def rgb_to_hex(palette):
    return ["#%02x%02x%02x" % (r,g,b) for (r,g,b) in palette]

def clean_plot(p, bg_color):
    p.background_fill_color=bg_color
    p.axis.visible=False
    p.grid.grid_line_color=None
    p.toolbar.autohide=True
    return p


def palplot(palette, plot='all',bg_color="white",alpha=1.0):
    """
    Displays palette via bokeh. Hover for hex/rgb value.
    Arguments
    ---------
    palette : list of hex strings or rgb tuples or HTML names (any combination)
    plot : 
        'swatch' for squares, 
        'pie' for wedges (adjacency comparison),
        'scatter' for some points,
        'line' for some lines,
        'all' for all (with dropdown menu for lines/points)
    bg_color : background fill color, 
        valid name hex or rgb 
    alpha : alpha of entire palette, 
        fraction btw 0.0 and 1.0
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
    _copy_palette = palette.copy() # copy so legend displays original inputs 
    
    if len(palette) > 7:
        raise RuntimeError("Palette too large! (< 7 colors preferred)")
    
    # REFORMATTING INPUT PALETTE ..........
    # convert RGB -> hex
    for _, p in enumerate(palette):
        if type(p) is not str:
            palette[_] = rgb_to_hex([p])[0]

    # convert HTML color names -> hex
    for _, p in enumerate(palette):
        if "#" not in p:
            palette[_] = html_colors[p.lower()]
            
            
    def swatch():
        df = pd.DataFrame(dict(palette=palette,
                           x=np.arange(len(palette)),
                           y=[0]*len(palette)  ))
        
        df['hex']=palette
        df['rgb']=hex_to_rgb(palette)
        
        height, width = 60, 325
        size = height/1.2
        p = bokeh.plotting.figure(width=width, height=height, 
                                       x_range=(-1,len(palette)),
                                       y_range=(-height,height),
                                       tooltips=TOOLTIPS)
        p.square(source=df, x='x',y='y', size=size, color='palette',alpha=alpha)
        p = clean_plot(p, bg_color)
        return p 
    
    def pie():
        width, height = 325,325
        angles = [0.216875, 0.1545, 0.127375, 0.1069, 0.103925,
                 0.055875, 0.04665,0.0355, 0.032275, 0.03, 0.018975, 
                 0.0131, 0.0128, 0.00925, 0.007075, 0.00635, 0.005125,
                 0.003825, 0.003525, 0.002925, 0.002, 0.0013, 0.001, 0.002875]
        df = pd.DataFrame(dict( angle=[a*2*np.pi for a in angles], 
                                palette=(palette*12)[:len(angles)], ))
        df['hex']=(palette*12)[:len(angles)]
        df['rgb']=hex_to_rgb((palette*12)[:len(angles)])
        
        p = bokeh.plotting.figure(width=width, height=height,
                                  x_range=(-1.1,1.1),tooltips=TOOLTIPS)
        p.wedge(x=0,y=0,radius=1,
                   start_angle=bokeh.transform.cumsum('angle',include_zero=True),
                   end_angle=bokeh.transform.cumsum('angle'),
                   line_color= bg_color, # "palette", # -> (no spaces btw wedges)
                   fill_color="palette",
                   fill_alpha=alpha,
                   source=df
               )
        p = clean_plot(p, bg_color)
        return p
    
    def scatter():
        n = 500
        x = np.linspace(0,8,n)
        ys, fits = np.empty((len(palette),n)), np.empty((len(palette),n))
        for i, _ in enumerate(palette):
            ys[i] = np.exp(np.power(x, i*0.1)) + np.random.uniform(-0.1*x, 0.1*x, size=len(x))
            fits[i] = np.exp(np.power(x, i*0.1)) + np.random.uniform(-0.01*x, 0.01*x, size=len(x))

        p = bokeh.plotting.figure(width=450,height=325)
        for i,y in enumerate(ys):
            p.circle(x,y,color=palette[i],size=3,
                     legend_label=f'{_copy_palette[i]}',alpha=alpha)
            p.line(x,fits[i],color=palette[i],line_width=3,
                   legend_label=f'{_copy_palette[i]}',line_alpha=alpha)
        
        p.legend.click_policy='hide'
        p.legend.location="top_left"
        p = clean_plot(p, bg_color)
        return p
    
    def line():
        n = 500
        x = np.linspace(0,4,n)
        ys = np.empty((len(palette),n))
        for i, _ in enumerate(palette):
            ys[i] = scipy.stats.gamma.pdf(x, a=3, loc=0, scale=1/(i+1.4))

        p = bokeh.plotting.figure(width=450,height=325)
        for i,y in enumerate(ys):
            p.line(x,ys[i],color=palette[i],line_width=3.5,
                   legend_label=f'{_copy_palette[i]}',line_alpha=alpha)

        p.legend.click_policy='hide'
        p.legend.location="top_right"
        p.background_fill_color=bg_color
        p.axis.visible=False
        p.toolbar.autohide=True
        return p
        
    if panel == True:
        glyph = pn.widgets.Select(options=['points','lines'],width=400,margin=[3,4])
        @pn.depends(glyph.param.value)
        def data(glyph="points"):
            if glyph == "points": return scatter()
            if glyph == "lines": return line()        
        
    #**********************************************************************
    if plot=="swatch":
        bokeh.io.show(swatch())
        
    if plot=="pie":
        bokeh.io.show(pie())
    
    if plot=="scatter":
        bokeh.io.show(scatter())
        
    if plot=="line":
        bokeh.io.show(line())
        
    if plot=="all":
        if panel == True:
            return pn.Row(pn.Column(pie(), swatch()), pn.Column(glyph,data))
        elif panel == False:
            bokeh.io.show(bokeh.layouts.layout([[pie(), scatter()], swatch()]))