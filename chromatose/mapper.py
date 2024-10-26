import numpy as np

def map_palette(q, palette, nan_color='#000000'):
    """
    Arguments
    ---------------
    q: 1D quantitative axis, numpy array
    palette: color palette to map to
    
    Returns
    ---------------
    colors: list of mapped colors
    """
    if type(q) is list:
        q = np.array(q)
        
    q_min = np.nanmin(q)
    q_max = np.nanmax(q)
    
    indices = ((q - q_min)/(q_max - q_min) \
               * (len(palette)-1)).astype(int)
    
    colors = []
    for i in indices:
        try:
            color = palette[i]
        except:
            color = nan_color
        colors.append(color)
        
    
    return colors




def map_palette_thresh(q, palette, q_max_thresh='inf', max_color=None,
                       q_min_thresh='-inf', min_color=None, nan_color='#000000'):
    """
    Useful for creating legends.
    
    Arguments
    ---------------
    q: 1D quantitative axis, numpy array
    palette: color palette to map to
    q_max_thresh: maximum threshold
    q_min_thresh: minimum threshold
    max_color: color to map maximum threshold to (otherwise set to last color in palette)
    min_color: color to map minimum threshold to (otherwise set to first color in palette)
    nan_color: color to map nan values to

    Returns
    ---------------
    colors: list of mapped colors
    """
    
    if max_color is None:
        max_color = palette[-1]
    if min_color is None:
        min_color = palette[0]
        
    if type(q) is list:
        q = np.array(q)
        
    if q_max_thresh == 'inf':
        q_max_thresh = np.nanmax(q)
    if q_min_thresh == '-inf':
        q_min_thresh = np.nanmin(q)
    
    colors = []
    for v in q:
        if np.isnan(v):
            c = nan_color
        elif v >= q_max_thresh: c = max_color
        elif v <= q_min_thresh: c = min_color
        else:
            i = ((v - q_min_thresh)/(q_max_thresh - q_min_thresh) \
               * (len(palette)-1))
            c = palette[int(i)]
            
        colors.append(c)
    return colors


def map_palette_diverging(q, palette, q_dividing, q_min_thresh=None, q_max_thresh=None, nan_color='#000000', midpoint=0.5):
    """
    For customizing diverging palettes with variable breakpoints and thresholds.
    This function assumes you pass in a balanced palette

    Arguments
    ---------------
    q: 1D quantitative axis, numpy array
    palette: color palette to map to
    q_dividing: dividing numeric value corresponding to divergence in palette
    q_min_thresh: minimum threshold
    q_max_thresh: amximum threshold
    nan_color: color to map nan values to
    midpoint: fraction, where to set midpoint of colorbar to, default 0.5
    
    Returns
    ---------------
    colors: list of mapped colors
    """
    if type(q) is list:
        q = np.array(q)
    if q_min_thresh is None:
        q_min_thresh = np.nanmin(q)
    if q_max_thresh is None:
        q_max_thresh = np.nanmax(q)
        
    i_center = int(len(palette) * midpoint)
    # slight bias towards positive values (given even-lengthed palette)
    palette_neg = palette[0:i_center]
    palette_pos = palette[i_center:]
    
    colors_neg = map_palette_thresh(q, palette_neg,
        q_min_thresh=q_min_thresh,
        q_max_thresh=q_dividing,
        nan_color=nan_color
    )
    colors_pos = map_palette_thresh(q, palette_pos,
        q_min_thresh=q_dividing,
        q_max_thresh=q_max_thresh,
        nan_color=nan_color
    )
    
    colors = []
    for v, neg, pos in zip(q, colors_neg, colors_pos):
        if np.isnan(v):
            c = nan_color
        elif v < q_dividing:
            c = neg
        else:
            c = pos
        colors.append(c)
    
    return colors
