import numpy as np

from .palettes import *
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


palette_dict = {
    "selah":selah,
    "frieda":frieda,
    "honeycombe":honeycombe,
    "crepuscule":crepuscule,
    "juniper":juniper,
    "plath":plath,
    "blonde":blonde,
    "leather":leather,
    "gucci":gucci,
    "sandbar":sandbar,
    "fiestaware":fiestaware,
    "chilaquiles":chilaquiles,
    "eleven": eleven,
    "splenda": splenda,
    "gremlin": gremlin,
    "pollen": pollen,
    "medium": medium,
    "juniper": juniper,
    "polya": polya,
    "ostrich": ostrich,
    "fraiche": fraiche,
    "cheshire": cheshire,
    "carmine": carmine,
    "joan": joan,
    "pinot": pinot,
    "addams": addams,
    "minuit": minuit,
    "fugazi": fugazi,
    "clementine": clementine,
    "leda": leda,
    "pugsley": pugsley,
    "bellhooks": bellhooks,
    "wes": wes,
    "lysergic": lysergic,
    "pepo": pepo,
    "reese": reese,
    "lufte": lufte,
    "oolong": oolong,
    "pitaya": pitaya,
    "alice": alice,
    "neko": neko,
    "belle": belle,
    "spiff": spiff,
    "yoshi": yoshi,
    "phoebe": phoebe,
    "pam": pam,
    "menthol": menthol,
    "dwight": dwight,
    "riley": riley,
    "mona": mona,
    "eeyore": eeyore,
    "rainbow":rainbow,
    "rory":rory,
    "pudding":pudding,
    "marmalade":marmalade,
    "polaris":polaris,
    "trefoil":trefoil,
    "harmon":harmon,
    "abed":abed,
    "shirley":shirley,
    "surely":surely,
    "annie":annie,
    "pierce":pierce,
    "britta":britta,
    "strogatz":strogatz,
    "lutz":lutz,
    "writhe":writhe,
    "perl":perl,
    "roosh": roosh,
    "seafare": seafare,
    "heliotrope": heliotrope,
    "moonbow": moonbow,
    "peanuts": peanuts,
    "naval": naval,
    "quinone":quinone,
    "quinoline":quinoline,
    "indomie": indomie,
    "maggie": maggie,
    "orb": orb,
    "diverging":diverging,
    "warble":warble,
    "waitomo":waitomo,
    "vylette":vylette,
    "pom":pom,
    "lava":lava,
    "pumpkin":pumpkin,
    "pinctada":pinctada,
    "nacre":nacre,
    "crest":crest,
    "blink":blink,
    "betan":betan,
    "rue":rue,
    "otterpop":otterpop,
    "gummi":gummi,
    "emporium":emporium,
    "paired":paired,
    "category20a":category20a,
    "category20b":category20b,
    "category20c":category20c,
}

def hex_to_rgb(palette):
    if type(palette)==str: return tuple([int(palette.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)])
    return [tuple(int(h.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)) for h in palette]

def rgb_to_hex(palette):
    if type(palette[0])==int: return "#%02x%02x%02x" % palette
    return ["#%02x%02x%02x" % (r,g,b) for (r,g,b) in palette]

def _rgb_hue_sat_light_chroma_val(tupple):
    '''retrieves hue, saturation, lightness, chroma and value from single color'''
    r, g, b = tupple
    r, g, b = r/256, g/256, b/256

    # rgb to hsl
    value = max(r,g,b)
    chroma = value-min(r,g,b)
    lightness = value-chroma/2

    if chroma==0: hue = 0
    elif value==r: hue = 60*((g-b)/chroma)
    elif value==g: hue = 60*(2+(b-r)/chroma)
    elif value==b: hue = 60*(4+(r-g)/chroma)

    if value==0: saturationV = 0
    else: saturationV = chroma/value

    if lightness==0 or lightness==1: saturationL = 0
    else: saturationL = (value-lightness)/min(lightness, 1-lightness)
    return hue%360, saturationL, saturationV, lightness, chroma, value

def _rgb_to_hsv(tupple):
    h, sL, sV, l, c, v = _rgb_hue_sat_light_chroma_val(tupple)
    return (h, sV, v)

def _rgb_to_hsl(tupple):
    h, sL, sV, l, c, v = _rgb_hue_sat_light_chroma_val(tupple)
    return (h, sL, l)


def _hcxm_rgb(h, c, x, m):
    if    0 <= h%360 < 60:   _r, _g, _b = (c, x, 0)
    elif 60 <= h%360 < 120:  _r, _g, _b = (x, c, 0)
    elif 120 <= h%360 < 180: _r, _g, _b = (0, c, x)
    elif 180 <= h%360 < 240: _r, _g, _b = (0, x, c)
    elif 240 <= h%360 < 300: _r, _g, _b = (x, 0, c)
    elif 300 <= h%360 < 360: _r, _g, _b = (c, 0, x)

    scale = lambda _ : int(np.round((_+m)*255,0))
    r, g, b = scale(_r), scale(_g), scale(_b)
    return r, g, b

def _hsv_to_rgb(tupple):
    h, s, v = tupple
    c = s*v
    x = c*(1-np.abs((h/60)%2 -1))
    m = v-c
    r, g, b = _hcxm_rgb(h, c, x, m)
    return (r, g, b)

def _hsl_to_rgb(tupple):
    h, s, l = tupple
    c = s*(1-np.abs(2*l-1))
    x = c*(1-np.abs((h/60)%2 -1))
    m = l-c/2
    r, g, b = _hcxm_rgb(h, c, x, m)
    return (r,g,b)


def rgb_to_hsv(palette):
    if type(palette[0])==int: return _rgb_to_hsv(palette)
    return [_rgb_to_hsv(color) for color in palette]

def rgb_to_hsl(palette):
    if type(palette[0])==int: return _rgb_to_hsl(palette)
    return [_rgb_to_hsl(color) for color in palette]

def hsv_to_rgb(palette):
    if type(palette[0])==float: return _hsv_to_rgb(palette)
    return [_hsv_to_rgb(color) for color in palette]

def hsl_to_rgb(palette):
    if type(palette[0])==float: return _hsl_to_rgb(palette)
    return [_hsl_to_rgb(color) for color in palette]

def luminance_sort(rgb):
    weights = np.array([0.2126, 0.7152, 0.0722])
    lum = [sum(np.array(list(c)) * weights) for c in rgb]
    rgb_sort = [x for _, x in sorted(zip(lum, rgb))]
    return rgb_sort

def hex_palette(palette):
    ''' REFORMATTING INPUT PALETTE ..........'''
    # convert RGB -> hex
    for _, p in enumerate(palette):
        if type(p) is not str: palette[_] = rgb_to_hex([p])[0]
    # convert HTML color names -> hex
    for _, p in enumerate(palette):
        if "#" not in p: palette[_] = html_colors[p.lower()]
    return palette
