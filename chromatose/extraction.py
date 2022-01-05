"""
The following code was written by Ivar Stangeby (@qTipTip) in his package `Pylette`,
and modified by Rosita Fu (@atisor73).

Date: 25 March 2021
"""

import warnings
import numpy as np
import panel as pn
from PIL import Image
from sklearn.cluster import KMeans
from .utils import *
from .viz import *

class _ColorBox(object):
    """
    Represents a box in the RGB color space w/ associated attributes
    used in Median Cut algorithm
    """

    def __init__(self, colors):
        """
        Initialize with a numpy array of RGB colors.
        colors: np.ndarray (width * height, 3)
        """
        self.colors = colors
        self._get_min_max()

    def _get_min_max(self):
        min_channel = np.min(self.colors, axis=0)
        max_channel = np.max(self.colors, axis=0)

        self.min_channel = min_channel
        self.max_channel = max_channel

    def __lt__(self, other):
        return self.size < other.size            # compare cubes by volumes

    @property
    def size(self):
        return self.volume

    def _get_dominant_channel(self):
        dominant_channel = np.argmax(self.max_channel - self.min_channel)
        return dominant_channel

    @property
    def average(self):
        return np.mean(self.colors, axis=0)      # avg color contained in _ColorBox

    @property
    def volume(self):
        return np.prod(self.max_channel - self.min_channel)

    def split(self):
        """
        Splits _ColorBox in to two _ColorBoxes at median of dominant color channel.
        Return: [_ColorBox1, _ColorBox2]
        """
        dominant_channel = self._get_dominant_channel()                       # dominant
        self.colors = self.colors[self.colors[:, dominant_channel].argsort()] # sorting...
        median_index = len(self.colors) // 2                                  # median

        return [ _ColorBox(self.colors[:median_index]),
                 _ColorBox(self.colors[median_index:])  ]

def _median_cut(arr, height, width, n_colors):
    arr = arr.reshape((width * height, -1))
    c = [_ColorBox(arr)]
    full_box_size = c[0].size

    # Each iteration:
    # 1. find largest box
    # 2. split it
    # 3. remove original box from list of boxes
    # 4. add two new boxes

    while len(c) < n_colors:
        largest_c_idx = np.argmax(c)
        c = c[:largest_c_idx] + c[largest_c_idx].split() + c[largest_c_idx + 1:]

    colors = [tuple([int(x) for x in box.average]) for box in c]
    return colors

def _k_means(arr, height, width, n_colors):
    arr = np.reshape(arr, (width * height, -1))
    model = KMeans(n_clusters=n_colors)
    labels = model.fit_predict(arr)

    palette = np.array(model.cluster_centers_, dtype=np.int)
    color_count = np.bincount(labels)
    color_frequency = color_count / float(np.sum(color_count))
    palette = [tuple(c) for c in palette]
    return palette

def extract(path,
            n_colors=5,
            method='kmeans',
            resize=True,
            sort=False,
            show=True
            ):
    '''
    Arguments:
    ----------
    path : image path                                (str)
    n_colors : desired length                        (int)
    method : either K-means or median-cut algorithm  (str)
        'kmeans', 'median', 'both'
    resize : shrink image for quicker return         (bool)
    sort : amateur sort by luminance                 (bool)
    show : prints hex and returns panel object       (bool)

    Returns:
    --------
    palette : list of hex values                     (list)
        if method == "both", list of palettes: [kmeans, median]
    '''

    img = Image.open(path).convert('RGB')
    if resize: img = img.resize((256, 256))
    width, height = img.size
    arr = np.asarray(img)

    if (method in ["MC", "mc", "median", "median cut", "median-cut", "Median Cut"]):
        colors = _median_cut(arr, height, width, n_colors)
    elif (method in ["KM", "km", "kmeans", "KMEANS", "k-means", "K-means", "K-MEANS"]):
        colors = _k_means(arr, height, width, n_colors)
    elif (method in ["both", "BOTH", "Both"]):
        k = _k_means(arr, height, width, n_colors)
        m = _median_cut(arr, height, width, n_colors)
        if sort: k, m = luminance_sort(k), luminance_sort(m)
        k, m = rgb_to_hex(k), rgb_to_hex(m)
        palettes = {"kmeans": k, "median": m}
        if show:
            print("      ", k)
            print("      ", m)
            return pn.Column(palplot(k), palplot(m))
            # return pn.Column(pn.pane.Markdown(f"      {k}",
            #                     style={'font-family':'Open Sans', 'font-size':'17px'},
            #                     align="center"
            #                     ),
            #                  palplot(k),
            #                  pn.pane.Markdown(f"      {m}",
            #                     style={'font-family':'Open Sans', 'font-size':'17px'},
            #                     align='center'
            #                     ),
            #                  palplot(m))
        return [k, m]
    else:
        warnings.warn("\nWarning: Defaulting to K-means ...",stacklevel=2)
        colors = _k_means(arr, height, width, n_colors)

    if sort: colors = luminance_sort(colors)
    palette = rgb_to_hex(colors)

    if show:
        print("      ", palette, end="\n\n")
        return palplot(palette)
    return palette
