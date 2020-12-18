"""
Chromatose is a package for storing and visualizing palettes and constructing new ones via interpolation.

The stored palettes are typically diverging, and mostly for personal record.
Visualizations include swatches, pies, points, lines, scatters, and heatmaps.
There are a multitude of beautiful gradients in packages like bokeh and colorcet that are,  for the most part, static. The interpolation scheme here can be used to create entirely new ones given only a few endpoints. This part is still in development, but currently uses linear or polynomial fits in color space metrics RGB, HSL, or HSV. Heatmaps are a great way to visualize the results.
"""

from .palettes import *
from .viz import *
from .interpolate import *
from .heat import *
from .utils import *


__author__ = "Rosita Fu"
__version__ = "0.0.3"
__license__ = "MIT"
__email__ = "rfu@caltech.edu"
