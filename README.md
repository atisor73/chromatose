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
diverging | ??? | ???  | ??? | orb\*
warble\* | waitomo\*  | vylette\*  |  pom\*  |  lava\*
pumpkin\*  | pinctada\*  | nacre\* | moxxi\* | salvia\*
bluefish | BuPu\* | holst | joker\* | rach\*
blink\*  |  betan\* | rue\*  | otterpop\*  |  gummi\*
emporium | paired  | category20a  | category20b  | category20c

\* *available as xxx256*

\[[discrete](https://github.com/atisor73/chromatose#discrete)\] \[[monochrome continuous](https://github.com/atisor73/chromatose#monochrome-continuous)\] \[[polychromatic continuous](https://github.com/atisor73/chromatose#polychromatic-continuous)] \[[bokeh](https://github.com/atisor73/chromatose#bokeh)\]


## `viz` :eyes:

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



## `interpolation` :scissors:

### ct.palpolate( )
 `palpolate` (<em>pal</em>-(ette inter)-<em>polate</em>):
    input lists of any size and user can control output size.

There are a multitude of beautiful gradients in packages like bokeh and colorcet that are, for the most part, static. The interpolation scheme here can be used to create entirely new ones given only a few endpoints. This part is still in development, but currently uses linear or polynomial fits in color space metrics RGB, HSL, or HSV. Heatmaps are a good way to visualize the results!

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/3interpolate1.png" width="85%" height="85%">

On the left are the input palettes, and on the right are the output palettes all approximately of size 256.
<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/3interpolate2.png" width="110%" height="100%">


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


## `extraction` :camera:
### ct.extract( )
 - **`path`** : string of image path
 - **`n_colors`** : integer desired length
 - **`method`** : 'kmeans' or 'median' or 'both'
   algorithm of extraction either k-means clustering or median cut, default k-means
 - `resize` : boolean, default True
 resizing samples a smaller image, speeds up extraction
  - `sort` : boolean, default False
  amateur sort by luminance

## `command line tools` :pick:
Palettes can be retrieved from command line:
 ```sh
 >>> chromatrieve leda
 >>> ... 
 >>> ['#2c2f30', '#8fa7d7', '#afd7d6', '#aa3751', '#f5b3b8']

 usage: chromatrieve [-h] palette

palette retriever

positional arguments:
  palette     name of chromatose palette (str)

optional arguments:
  -h, --help  show this help message and exit
```

Palettes can be extracted from command line:
 ```sh
 >>> chromextract egg.png
 >>> ...
 >>> K-Means:    ['#050002', '#0c1c7b', '#013adc', '#1b143a', '#294254']
 >>> Median Cut: ['#040000', '#080006', '#1e1b3c', '#1e2d61', '#0330bd']

usage: chromextract [-h] [-n] [-r] [-s] [-d] path

Palette extraction from image path. Defaults to 5 colors.

positional arguments:
  path             path to image

optional arguments:
  -h, --help       show this help message and exit
  -n , --ncolors   length of palette
  -r , --resize    resize for efficiency
  -s , --sort      sort by luminance
  -d , --display   serve panel object

 ```



# gallery :rainbow:

## `discrete`

**frieda**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/frieda.png" width="85%" height="85%">


**plath**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/plath.png" width="85%" height="85%">

**selah**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/selah.png" width="85%" height="85%">

**blonde**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/blonde.png" width="85%" height="85%">

**honeycombe**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/honeycombe.png" width="85%" height="85%">

**lysergic**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/lysergic.png" width="85%" height="85%">

**pepo**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pepo.png" width="85%" height="85%">

**reese**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/reese.png" width="85%" height="85%">

**rainbow**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/rainbow.png" width="85%" height="85%">

**lufte**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/lufte.png" width="85%" height="85%">

**pitaya**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pitaya.png" width="85%" height="85%">

**spiff**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/spiff.png" width="85%" height="85%">

**leather**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/leather.png" width="85%" height="85%">

**medium**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/medium.png" width="85%" height="85%">

**addams**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/addams.png" width="85%" height="85%">

**mona**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/mona.png" width="85%" height="85%">

**leda**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/leda.png" width="85%" height="85%">

**rory**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/rory.png" width="85%" height="85%">

**pudding**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pudding.png" width="85%" height="85%">

**polaris**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/polaris.png" width="85%" height="85%">

**trefoil**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/trefoil.png" width="85%" height="85%">

**writhe**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/writhe.png" width="85%" height="85%">

**perl**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/perl.png" width="85%" height="85%">

**roosh**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/roosh.png" width="85%" height="85%">

**heliotrope**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/heliotrope.png" width="85%" height="85%">

**indomie**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/indomie.png" width="85%" height="85%">

**strogatz**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/strogatz.png" width="85%" height="85%">

**juniper**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/juniper.png" width="85%" height="85%">

**minuit**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/minuit.png" width="85%" height="85%">

**alice**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/alice.png" width="85%" height="85%">

**wes**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/wes.png" width="85%" height="85%">

**pam**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pam.png" width="85%" height="85%">

**dwight**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/dwight.png" width="85%" height="85%">

**marmalade**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/marmalade.png" width="85%" height="85%">

**harmon**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/harmon.png" width="85%" height="85%">

**abed**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/abed.png" width="85%" height="85%">

**shirley**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/shirley.png" width="85%" height="85%">

**annie**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/annie.png" width="85%" height="85%">

**pierce**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pierce.png" width="85%" height="85%">

**britta**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/britta.png" width="85%" height="85%">

**eeyore**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/eeyore.png" width="85%" height="85%">

**neko**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/neko.png" width="85%" height="85%">

**maggie**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/maggie.png" width="85%" height="85%">

**peanuts**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/peanuts.png" width="85%" height="85%">

**eleven**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/eleven.png" width="85%" height="85%">

**naval**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/naval.png" width="85%" height="85%">

**fugazi**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/fugazi.png" width="85%" height="85%">

**clementine**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/clementine.png" width="85%" height="85%">

**alice**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/alice.png" width="85%" height="85%">

**wes**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/wes.png" width="85%" height="85%">

**diverging**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/diverging.png" width="85%" height="85%">

**lutz**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/lutz.png" width="85%" height="85%">

**moonbow**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/moonbow.png" width="85%" height="85%">


**chilaquiles**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/chilaquiles.png" width="85%" height="85%">

**fiestaware**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/fiestaware.png" width="85%" height="85%">

**polya**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/polya.png" width="85%" height="85%">

**splenda**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/splenda.png" width="85%" height="85%">

**riley**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/riley.png" width="85%" height="85%">

**pollen**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pollen.png" width="85%" height="85%">

**fraiche**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/fraiche.png" width="85%" height="85%">

**cheshire**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/cheshire.png" width="85%" height="85%">

**pugsley**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pugsley.png" width="85%" height="85%">

**oolong**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/oolong.png" width="85%" height="85%">

**bellhooks**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/bellhooks.png" width="85%" height="85%">

**belle**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/belle.png" width="85%" height="85%">

**phoebe**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/phoebe.png" width="85%" height="85%">

**ostrich**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/ostrich.png" width="85%" height="85%">

**yoshi**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/yoshi.png" width="85%" height="85%">

**carmine**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/carmine.png" width="85%" height="85%">

## `monochrome continuous`

**salvia\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/salvia.png" width="85%" height="85%">

**pom\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pom.png" width="85%" height="85%">

**lava\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/lava.png" width="85%" height="85%">

**moxxi\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/moxxi.png" width="85%" height="85%">

**joan\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/joan.png" width="85%" height="85%">

**waitomo\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/waitomo.png" width="85%" height="85%">

**warble\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/warble.png" width="85%" height="85%">


**vylette\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/vylette.png" width="85%" height="85%">

**pumpkin\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pumpkin.png" width="85%" height="85%">

**crest\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/crest.png" width="85%" height="85%">

**nacre\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/nacre.png" width="85%" height="85%">

**salvia256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/salvia256.png" width="85%" height="85%">

**warble256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/warble256.png" width="85%" height="85%">

**waitomo256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/waitomo256.png" width="85%" height="85%">

**vylette256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/vylette256.png" width="85%" height="85%">

**pom256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pom256.png" width="85%" height="85%">

**moxxi256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/moxxi256.png" width="85%" height="85%">


**lava256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/lava256.png" width="85%" height="85%">

**pumpkin256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pumpkin256.png" width="85%" height="85%">

**joan256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/joan256.png" width="85%" height="85%">

**nacre256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/nacre256.png" width="85%" height="85%">

**crest256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/crest256.png" width="85%" height="85%">

## `polychromatic continuous`

**joker\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/joker.png" width="85%" height="85%">

**rach\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/rach.png" width="85%" height="85%">

**orb\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/orb.png" width="85%" height="85%">

**blink\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/blink.png" width="85%" height="85%">

**rue\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/rue.png" width="85%" height="85%">

**betan\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/betan.png" width="85%" height="85%">

**bluefish**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/bluefish.png" width="85%" height="85%">

**otterpop\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/otterpop.png" width="85%" height="85%">

**gummi\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/gummi.png" width="85%" height="85%">

**emporium\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/emporium.png" width="85%" height="85%">

**perl256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/perl256.png" width="85%" height="85%">

**orb256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/orb256.png" width="85%" height="85%">

**blink256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/blink256.png" width="85%" height="85%">

**otterpop256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/otterpop256.png" width="85%" height="85%">

**gummi256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/gummi256.png" width="85%" height="85%">

**emporium256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/emporium256.png" width="85%" height="85%">

**betan256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/betan256.png" width="85%" height="85%">

**rue256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/rue256.png" width="85%" height="85%">

**rach256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/rach256.png" width="85%" height="85%">

**joker256**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/joker256.png" width="85%" height="85%">

## `bokeh`

**paired**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/paired.png" width="85%" height="85%">

**category20a**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/category20a.png" width="85%" height="85%">

**category20b**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/category20b.png" width="85%" height="85%">

**category20c**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/category20c.png" width="85%" height="80%">

<br>

*"The last color she remembered was the indigo chips in the headstone. After that she became as color conscious as a hen."*
