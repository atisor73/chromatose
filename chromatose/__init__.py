"""
Chromatose is a package for storing and visualizing palettes, and constructing new ones via interpolation or extraction.

The stored palettes are for personal record, featuring diverging and continuous palettes.
Visualizations include swatches, pies, points, lines, scatters, and heatmaps.

The interpolation scheme here can be used to create entirely new ones given only a few intermediary points. The underlying algorithm uses a combination of linear and polynomial splines in adjustable color space metrics: RGB, HSL, or HSV. Heatmaps are a great way to visualize the results. To extract palettes from images, chromatose employs k-means clustering and median-cut algorithms."
"""

from .palettes import *
from .viz import *
from .interpolate import *
from .utils import *
from .heat import *
from .extraction import *
from .colorpicker import *
from .mapper import *

__author__ = "Rosita Fu"
__version__ = "2.0.0"
__license__ = "MIT"
__email__ = "rosita.fu99@gmail.com"
