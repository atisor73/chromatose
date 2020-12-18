# chromatose
<hr>
A package for storing and visualizing palettes, and constructing new ones via interpolation.<br> 
The stored palettes are typically diverging, and mostly for personal record. Visualizations include swatches, pies, points, lines, scatters, and heatmaps. There are a multitude of beautiful gradients in packages like bokeh and colorcet that are,  for the most part, static. The interpolation scheme here can be used to create entirely new ones given only a few endpoints. This part is still in development, but currently uses linear or polynomial fits in color space metrics RGB, HSL, or HSV. Heatmaps are a great way to visualize the results. Chromatose is now pippable!




## `viz` :eyes:

### ct.swatch( )
- **`palette`** : list or iterable  
    any combination of hex strings or rgb tuples or HTML names
- `alpha` : fraction between 0.0 and 1.0  
    *alpha transparency of entire palette*

### ct.palplot( ) 
Visualizations include swatches, pies, points, lines, scatters. Somewhat helpful for seeing how colors behave on a plot, in dense or scattered visuals. Sometimes colors look great together on a swatch, but not so great in their pointillistic forms. 
- **`palette`** : list or iterable  
    any combination of hex strings or rgb tuples or HTML
- `bg_color` : HTML or hex string  
    *background fill color*
- `alpha` : fraction between 0.0 and 1.0  
    *alpha transparency of entire palette* 
- `shuffle` : boolean  
    *shuffles palette*

### ct.heatmap( )
Volcano data lifted from R.

- **`palette`** : list or iterable   
    any combination of hex strings or rgb tuples or HTML
- `interpolate` : boolean  
    *if True, interpolates palette*
    *if False, generates heatmap with input directly*
- `desired_length` : integer  
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





## `interpolation` :scissors:

### ct.palpolate( )
Rough RGB interpolator called `palpolate` (<em>pal</em>-(ette inter)-<em>polate</em>), can handle input lists of any size and user can control output size. 

There are a multitude of beautiful gradients in packages like bokeh and colorcet that are, for the most part, static. The interpolation scheme here can be used to create entirely new ones given only a few endpoints. This part is still in development, but currently uses linear or polynomial fits in color space metrics RGB, HSL, or HSV. Heatmaps are a great way to visualize the results.

- **`palette`** : list or iterable   
    any combination of hex strings or rgb tuples or HTML
- **`desired_length`** : integer  
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


## `palettes` :art:
|       |      |      |      |          |
|----------|----------|----------|----------|----------|
frieda | plath | selah | blonde | honeycombe
crepuscule | leather | gucci | sandbar | fiestaware
chilaquiles | eleven | splenda | gremlin | pollen
medium | juniper | polya | ostrich | fraiche
cheshire | carmine | joan | pinot | addams
minuit | fugazi | clementine | leda | pugsley
bellhooks | wes | lysergic | pepo |  reese
lufte | oolong | pitaya | alice | neko
belle | spiff | yoshi | phoebe | pam
menthol | dwight | riley | mona | eeyore
rainbow


**frieda**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/frieda.png" width="80%" height="80%">



**plath**

![](imgs/plath.png)

**selah**

![](imgs/selah.png)

**blonde**

![](imgs/blonde.png)

**honeycombe**

![](imgs/honeycombe.png)

**lysergic**

![](imgs/lysergic.png)

**pepo**

![](imgs/pepo.png)

**reese**

![](imgs/reese.png)

**rainbow**

![](imgs/rainbow.png)

**lufte**

![](imgs/lufte.png)

**pitaya**

![](imgs/pitaya.png)

**crepuscule**

![](imgs/crepuscule.png)

**spiff**

![](imgs/spiff.png)

**leather**

![](imgs/leather.png)

**eleven**

![](imgs/eleven.png)

**chilaquiles**

![](imgs/chilaquiles.png)

**fiestaware**

![](imgs/fiestaware.png)

**splenda**

![](imgs/splenda.png)

**medium**

![](imgs/medium.png)

**juniper**

![](imgs/juniper.png)

**pollen**

![](imgs/pollen.png)

**gremlin**

![](imgs/gremlin.png)

**fraiche**

![](imgs/fraiche.png)

**polya**

![](imgs/polya.png)

**cheshire**

![](imgs/cheshire.png)


**carmine**

![](imgs/carmine.png)


**joan**

![](imgs/joan.png)

**pinot**

![](imgs/pinot.png)

**addams**

![](imgs/addams.png)

**minuit**

![](imgs/minuit.png)

**fugazi**

![](imgs/fugazi.png)

**clementine**

![](imgs/clementine.png)

**mona**

![](imgs/mona.png)

**leda**

![](imgs/leda.png)

**pugsley**

![](imgs/pugsley.png)

**bellhooks**

![](imgs/bellhooks.png)

**oolong**

![](imgs/oolong.png)

**alice**

![](imgs/alice.png)

**wes**

![](imgs/wes.png)

**belle**

![](imgs/belle.png)

**neko**

![](imgs/neko.png)

**phoebe**

![](imgs/phoebe.png)

**pam**

![](imgs/pam.png)

**dwight**

![](imgs/dwight.png)

**menthol**

![](imgs/menthol.png)

**riley**

![](imgs/riley.png)

**ostrich**

![](imgs/ostrich.png)

**eeyore**

![](imgs/eeyore.png)

**yoshi**

![](imgs/yoshi.png)

**gucci**

![](imgs/gucci.png)

**sandbar**

![](imgs/sandbar.png)

*"The last color she remembered was the indigo chips in the headstone. After that she became as color conscious as a hen."* 
