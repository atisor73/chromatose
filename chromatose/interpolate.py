import numpy as np
from .utils import *

def curver(xs, direction):
    Δ = max(xs) - min(xs)
    a, b, c = Δ/25, Δ/2, 1000
    up = (xs-a) + (xs-b)**2/c
    down = (xs+a) - (xs-b)**2/c
    if direction=="up": return up
    if direction=="down": return down

def _pair_interpolate(start, end, num,
                       method='hsv',
                       redundant=True,
                       curve=False,                  # rgb interpolate only
                       directions=["up","down","up"] # rgb interpolate only
                      ):
    # assume start and end are in hex
    start, end = hex_to_rgb(start), hex_to_rgb(end)
    if method=='rgb' or method=="RGB":
        start_x, start_y, start_z = start[0], start[1], start[2],
        end_x, end_y, end_z = end[0], end[1], end[2],
        xs = np.linspace(start_x, end_x, num)
        ys = np.linspace(start_y, end_y, num)
        zs = np.linspace(start_z, end_z, num)

        if curve==True:
            xs = curver(xs-start_x, directions[0]) + start_x  # curve r up
            ys = curver(ys-start_y, directions[1]) + start_y  # curve g down
            zs = curver(zs-start_z, directions[2]) + start_z  # curve b down
        palette = rgb_to_hex([(np.abs(int(x)), np.abs(int(y)), np.abs(int(z)))
                              for x, y, z in zip(xs, ys, zs)])
        if redundant==False: return palette
        return palette[:-1]
    dict_function = {'hsl':[rgb_to_hsl, hsl_to_rgb],
                     'HSL':[rgb_to_hsl, hsl_to_rgb],
                     'hsv':[rgb_to_hsv, hsv_to_rgb],
                     'HSV':[rgb_to_hsv, hsv_to_rgb],}
    function = dict_function[method][0]
    start_x, start_y, start_z = function(start)
    end_x, end_y, end_z = function(end)
    xs = np.linspace(start_x, end_x, num)
    ys = np.linspace(start_y, end_y, num)
    zs = np.linspace(start_z, end_z, num)
    _ = [(x, y, z)for x, y, z in zip(xs, ys, zs)]

    function = dict_function[method][1]
    palette = rgb_to_hex(function(_))

    if redundant==False: return palette
    return palette[:-1] # don't include last one


def palpolate(
    palette,
    n_colors=256,
    method='rgb',
    curve=False,
    directions=['up','down','up']
    ):
    """
    Interpolation of input palette to a longer palette of desired length.
    Can do linear or polynomial interpolation for RGB.

    Arguments
    ---------
    palette : list
         iterable of any combination of hex strings, rgb tuples, HTML names
    n_colors : integer
         approximate desired length of final palette
    method : string 'rgb' or 'hsv' or 'hsl'
         interpolation metric, default 'rgb'
    curve : boolean
        if True, fit to 2ndº polynomial
        if False, simple linear interpolation
        default False
    directions : list of 3 strings, 'up' or 'down'
        each entry corresponds to r, g, b
        'up' pushes intermediate values higher (lighter)
        'down' pushes intermediate values lower (darker)

    Returns
    ---------
    output : list of interpolated palette
    """

    if n_colors <= len(palette)*1.5:
        return palette

    palette = list(palette)
    palette = hex_palette(palette)

    # BEGIN INTERPOLATION........................................
    interpolated_palette = []
    num = int(n_colors / (len(palette)-1))
    redundant = True
    if len(palette)==2: redundant=False        # no need to exclude last one

    for i in range(len(palette[:-1])):
        if i == len(palette)-2: redundant=False
        lst = _pair_interpolate(palette[i], palette[i+1], num,
                                 method=method,
                                 curve=curve,
                                 directions=directions,
                                 redundant=redundant)
        interpolated_palette.extend(lst)
    return interpolated_palette
