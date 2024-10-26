# chromatose
<hr>
A package for storing and visualizing palettes, and constructing new ones via polynomial interpolation and image extraction. Now pippable!
<br><br>
*This package borrows inspiration from @jmaasch's scatterplots in her package [`sanzo`](https://github.com/jmaasch/sanzo), and uses extraction algorithms from @qTipTip's package [`Pylette`](https://github.com/qTipTip/Pylette).*


## `palettes` :art:

|          |          |         |           |          |
|----------|----------|----------|----------|----------|
frieda | plath | selah | blonde | honeycombe
crepuscule | leather | gucci | sandbar | fiestaware
chilaquiles | eleven | splenda | gremlin | pollen
medium | juniper | polya | ostrich | fraiche
cheshire | carmine | joan\* | pinot | addams
minuit | fugazi | clementine | leda | pugsley
bellhooks | wes | lysergic | pepo |  reese
lufte | oolong | pitaya | alice | neko
belle | spiff | yoshi | phoebe | pam
menthol | dwight | riley | mona | eeyore
rory  | pudding | marmalade | polaris | trefoil
harmon | abed | shirley | surely |  annie
pierce | britta | strogatz | lutz | writhe
perl\* | roosh  | seafare | heliotrope | moonbow
peanuts | naval | indomie  |  maggie | rainbow
??? | quinone | quinoline  | diverging | orb\*
warble\* | waitomo\*  | vylette\*  |  pom\*  |  lava\*
pumpkin\*  | pinctada\*  | nacre\* | moxxi\* | salvia\*
bluefish | BuPu\* | holst | joker\* | rach\*
blink\*  |  betan\* | rue\*  | otterpop\*  |  gummi\*
emporium | paired  | category20a  | category20b  | category20c

\* *available as xxx256*

\[[discrete](https://github.com/atisor73/chromatose#discrete)\] \[[monochrome continuous](https://github.com/atisor73/chromatose#monochrome-continuous)\] \[[polychromatic continuous](https://github.com/atisor73/chromatose#polychromatic-continuous)] \[[bokeh](https://github.com/atisor73/chromatose#bokeh)\]


# Viz :eyes:

### ct.palplot( )
Visualizations include swatches, pies, points, lines, scatters. Somewhat helpful for seeing how colors behave on a plot, in dense or scattered visuals. Sometimes colors look great together on a swatch, but not so great in their pointillistic forms.
<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/2palplot.jpg" width="110%" height="105%">
- **`palette`** : list or iterable
    any combination of hex strings or rgb tuples or HTML
- `bg_color` : HTML or hex string
    *background fill color*
- `alpha` : fraction between 0.0 and 1.0
    *alpha transparency of entire palette*
- `shuffle` : boolean
    *shuffles palette*

### ct.palpicker( )
Testing out panel's new colorpicker widget! Useful for adjusting palettes to personal taste.
- **`n`** : list or integer

<!--
### ct.swatch( )
watch me swatch...
 <img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/1swatch.jpg" width="100%" height="100%">

- **`palette`** : list or iterable
    any combination of hex strings or rgb tuples or HTML names
- `alpha` : fraction between 0.0 and 1.0
    *alpha transparency of entire palette*
     -->

<!--
### ct.heatmap( )
Volcano data lifted from R. Hot stuff.
<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/5heatmap.png" width="56%" height="56%">

Default interpolation (below) but can also turn this off (above).

- **`palette`** : list or iterable
    any combination of hex strings or rgb tuples or HTML
- `interpolate` : boolean
    *if True, interpolates palette*
    *if False, generates heatmap with input directly*
- `n_colors` : integer
    *approximate desired length of final palette*
- `interpolation_method` : string 'rgb' or 'hsv' or 'hsl'
    *interpolation metric*
- `curve` : boolean
    *if True, fit to 2ndº polynomial*
    *if False, simple linear interpolation*
- `directions` : list of 3 strings, 'up' or 'down'
    *each entry corresponds to r, g, b*
    *'up' pushes intermediate values higher (lighter)*
    *'down' pushes intermediate values lower (darker)*
- `return_palette` : boolean
    *if True, returns interpolated palette as list*
    *if False, no returns*

 -->



# Interpolation 

### ct.palpolate( )
 `palpolate` (<em>pal</em>-(ette inter)-<em>polate</em>):
    input lists of any size and user can control output size.

There are a multitude of beautiful gradients in packages like bokeh and colorcet that are, for the most part, static. The interpolation scheme here can be used to create entirely new ones given only a few endpoints. This part is still in development, but currently uses linear or polynomial fits in color space metrics RGB, HSL, or HSV. Heatmaps are a good way to visualize the results!
<!--
<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/3interpolate1.png" width="60%" height="60%"> -->

On the left are the input palettes, and on the right are the output palettes all approximately of size 256.
<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/3interpolate2.png" width="100%" height="91%">


- **`palette`** : list or iterable
    any combination of hex strings or rgb tuples or HTML
- **`n_colors`** : integer
    approximate desired length of final palette
- `method` : string 'rgb' or 'hsv' or 'hsl'
    *interpolation metric, default 'rgb'*
- `curve` : boolean
    *if True, fit t 2ndº polynomial*
    *if False, simple linear interpolation*
- `directions` : list of 3 strings, 'up' or 'down'
    *each entry corresponds to r, g, b*
    *'up' pushes intermediate values higher (lighter)*
    *'down' pushes intermediate values lower (darker)*


# Extraction :camera:
Extract palette of size `n_colors` from image given image path using k-means or median cut algorithms.

### ct.extract( )
 - **`path`** : string of image path
 - **`n_colors`** : integer number of colors to extract
 - **`method`** : 'kmeans' or 'median' or 'both'
   algorithm of extraction either k-means clustering or median cut, default k-means
 - `resize` : boolean, default True
 resizing samples a smaller image, speeds up extraction
  - `sort` : boolean, default False
    amateur sort by luminance
  - `show` : boolean, default True
    prints palette and returns panel object


# `Color mapping` 

### map_palette( )
Given palette and 1D quantitative axis, returns list of mapped colors. Uses min and max to first and last of palette
 - **`q`** : 1D quantitative axis, numpy array
 - **`palette`** : color palette to map to
 - Returns `colors`: list of mapped colors

### map_palette_thresh( )
Given palette and 1D quantitative axis, returns list of mapped colors. Instead of min and max of dataset, uses customized end points. 

For example, a dataset may range from (-1, 1), and you want extreme colors to reflect those bounds, not necessarily your dataset's range. 

 - **`q`** : 1D quantitative axis, numpy array
 - **`palette`** : color palette to map to
 - **`q_min_thresh`** : minimum threshold, default -infinity
 - **`q_max_thresh`** : maximum threshold, default +infinity
 - **`min_color`** : color to map minimum threshold to (otherwise set to first color in palette)
 - **`max_color`** : color to map maximum threshold to (otherwise set to last color in palette)
 - **`nan_color`** : color to map nan values to
 - Returns **`colors`**: list of mapped colors


### map_palette_diverging( )
For customizing diverging palettes with variable breakpoints and thresholds.

For example, a dataset may range from (-x, +y), and you want zero to be the color/point at which the colors diverge.

This function assumes you pass in a balanced palette, but 'midpoint' can approximately adjust this.

 - **`q`** : 1D quantitative axis, numpy array
 - **`palette`** : color palette to map to
 - **`q_dividing`** : dividing numeric value corresponding to divergence in palette
 - **`q_min_thresh`** : minimum threshold, default -infinity
 - **`q_max_thresh`** : maximum threshold, default -infinity
 - **`nan_color`** : color to map nan values to, default black
 - **`midpoint`** : fraction, where to set midpoint of colorbar to, default 0.5

 - Returns **`colors`**: list of mapped colors


# Command line tools
Palettes can be retrieved from command line:
 ```sh
 >>> chromatose leda
 >>> ['#2c2f30', '#8fa7d7', '#afd7d6', '#aa3731', '#f5b3b8']
 ```

Palettes can be extracted from command line:
 ```sh
 >>> extract egg.png
 >>> K-Means:    ['#050002', '#0c1c7b', '#013adc', '#1b143a', '#294254']
 >>> Median Cut: ['#040000', '#080006', '#1e1b3c', '#1e2d61', '#0330bd']

Palette extraction from image path using both k-means and median cut
algorithms. Defaults to 5 colors, resized, unsorted, and not displayed.

  path             path to image

  -n , --ncolors   length of palette (int, default 5)
  -r , --resize    resize for efficiency (bool, default True)
  -s , --show      display pillow swatches (bool, default False)
 ```

# Gallery :rainbow:

## [`discrete`](https://github.com/atisor73/chromatose#palettes-art)

**frieda**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/frieda.png" width="73%" height="73%">


**plath**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/plath.png" width="73%" height="73%">

**selah**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/selah.png" width="73%" height="73%">

**blonde**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/blonde.png" width="73%" height="73%">

**honeycombe**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/honeycombe.png" width="73%" height="73%">

**lysergic**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/lysergic.png" width="73%" height="73%">

**pepo**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pepo.png" width="73%" height="73%">

**reese**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/reese.png" width="73%" height="73%">

**rainbow**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/rainbow.png" width="73%" height="73%">

**lufte**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/lufte.png" width="73%" height="73%">

**pitaya**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pitaya.png" width="73%" height="73%">

**spiff**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/spiff.png" width="73%" height="73%">

**leather**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/leather.png" width="73%" height="73%">

**medium**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/medium.png" width="73%" height="73%">

**addams**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/addams.png" width="73%" height="73%">

**mona**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/mona.png" width="73%" height="73%">

**leda**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/leda.png" width="73%" height="73%">

**rory**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/rory.png" width="73%" height="73%">

**pudding**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pudding.png" width="73%" height="73%">

**polaris**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/polaris.png" width="73%" height="73%">

**trefoil**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/trefoil.png" width="73%" height="73%">

**writhe**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/writhe.png" width="73%" height="73%">

**perl\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/perl.png" width="73%" height="73%">

**roosh**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/roosh.png" width="73%" height="73%">

**heliotrope**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/heliotrope.png" width="73%" height="73%">

**indomie**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/indomie.png" width="73%" height="73%">

**strogatz**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/strogatz.png" width="73%" height="73%">

**juniper**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/juniper.png" width="73%" height="73%">

**quinone**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/quinone.png" width="73%" height="73%">


**minuit**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/minuit.png" width="73%" height="73%">

**alice**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/alice.png" width="73%" height="73%">

**wes**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/wes.png" width="73%" height="73%">

**pam**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pam.png" width="73%" height="73%">

**dwight**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/dwight.png" width="73%" height="73%">

**marmalade**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/marmalade.png" width="73%" height="73%">

**harmon**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/harmon.png" width="73%" height="73%">

**shirley**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/shirley.png" width="73%" height="73%">

**annie**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/annie.png" width="73%" height="73%">

**pierce**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pierce.png" width="73%" height="73%">

**britta**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/britta.png" width="73%" height="73%">

**abed**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/abed.png" width="73%" height="73%">

**eeyore**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/eeyore.png" width="73%" height="73%">

**neko**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/neko.png" width="73%" height="73%">

**maggie**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/maggie.png" width="73%" height="73%">

**quinoline**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/quinoline.png" width="73%" height="73%">

**peanuts**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/peanuts.png" width="73%" height="73%">

**eleven**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/eleven.png" width="73%" height="73%">

**naval**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/naval.png" width="73%" height="73%">

**fugazi**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/fugazi.png" width="73%" height="73%">

**clementine**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/clementine.png" width="73%" height="73%">

**diverging**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/diverging.png" width="73%" height="73%">

**lutz**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/lutz.png" width="73%" height="73%">

**moonbow**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/moonbow.png" width="73%" height="73%">


**chilaquiles**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/chilaquiles.png" width="73%" height="73%">

**fiestaware**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/fiestaware.png" width="73%" height="73%">

**polya**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/polya.png" width="73%" height="73%">

**splenda**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/splenda.png" width="73%" height="73%">

<!-- **riley**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/riley.png" width="73%" height="73%"> -->

**pollen**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pollen.png" width="73%" height="73%">

**fraiche**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/fraiche.png" width="73%" height="73%">

**cheshire**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/cheshire.png" width="73%" height="73%">
<!--
**pugsley**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pugsley.png" width="73%" height="73%"> -->

<!-- **oolong**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/oolong.png" width="73%" height="73%"> -->

**bellhooks**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/bellhooks.png" width="73%" height="73%">

**belle**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/belle.png" width="73%" height="73%">

**phoebe**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/phoebe.png" width="73%" height="73%">

**ostrich**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/ostrich.png" width="73%" height="73%">

**yoshi**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/yoshi.png" width="73%" height="73%">

<!-- **carmine**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/carmine.png" width="73%" height="73%"> -->





## [`monochrome continuous`](https://github.com/atisor73/chromatose#palettes-art)

**salvia\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/salvia.png" width="73%" height="73%">

**pom\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pom.png" width="73%" height="73%">

**lava\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/lava.png" width="73%" height="73%">

**moxxi\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/moxxi.png" width="73%" height="73%">

**joan\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/joan.png" width="73%" height="73%">

**waitomo\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/waitomo.png" width="73%" height="73%">

**warble\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/warble.png" width="73%" height="73%">


**vylette\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/vylette.png" width="73%" height="73%">

**pumpkin\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pumpkin.png" width="73%" height="73%">

**crest\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/crest.png" width="73%" height="73%">

**nacre\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/nacre.png" width="73%" height="73%">

**salvia256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/salvia256.png" width="73%" height="73%">

**warble256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/warble256.png" width="73%" height="73%">

**waitomo256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/waitomo256.png" width="73%" height="73%">

**vylette256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/vylette256.png" width="73%" height="73%">

**pom256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pom256.png" width="73%" height="73%">

**moxxi256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/moxxi256.png" width="73%" height="73%">


**lava256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/lava256.png" width="73%" height="73%">

**pumpkin256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pumpkin256.png" width="73%" height="73%">

**joan256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/joan256.png" width="73%" height="73%">

**nacre256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/nacre256.png" width="73%" height="73%">

**crest256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/crest256.png" width="73%" height="73%">

## [`polychromatic continuous`](https://github.com/atisor73/chromatose#palettes-art)

**joker\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/joker.png" width="73%" height="73%">

**rach\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/rach.png" width="73%" height="73%">

**orb\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/orb.png" width="73%" height="73%">

**blink\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/blink.png" width="73%" height="73%">

**rue\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/rue.png" width="73%" height="73%">

**betan\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/betan.png" width="73%" height="73%">

**bluefish**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/bluefish.png" width="73%" height="73%">

**otterpop\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/otterpop.png" width="73%" height="73%">

**gummi\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/gummi.png" width="73%" height="73%">

**emporium\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/emporium.png" width="73%" height="73%">

**perl256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/perl256.png" width="73%" height="73%">

**orb256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/orb256.png" width="73%" height="73%">

**blink256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/blink256.png" width="73%" height="73%">

**otterpop256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/otterpop256.png" width="73%" height="73%">

**gummi256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/gummi256.png" width="73%" height="73%">

**emporium256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/emporium256.png" width="73%" height="73%">

**betan256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/betan256.png" width="73%" height="73%">

**rue256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/rue256.png" width="73%" height="73%">

**rach256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/rach256.png" width="73%" height="73%">

**joker256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/joker256.png" width="73%" height="73%">

## [`bokeh`](https://github.com/atisor73/chromatose#palettes-art)

**paired**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/paired.png" width="73%" height="73%">

**category20a**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/category20a.png" width="73%" height="73%">

**category20b**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/category20b.png" width="73%" height="73%">

**category20c**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/category20c.png" width="73%" height="73%">

<br>

*"The last color she remembered was the indigo chips in the headstone. After that she became as color conscious as a hen."*