# chromatose
<hr>
A package for storing and visualizing palettes, and constructing new ones via interpolation. Now pippable!
<br> 



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
rainbow | BuPu9 | BuPu256 | holst | bluefish 
joker | joker256 |  rach |  rach256 | moxxi
moxxi256 | salvia |  salvia256 | 


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

### ct.heatmap( )
Volcano data lifted from R. Hot stuff.   
<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/5heatmap.png" width="56%" height="56%">   

Default interpolation (below) but can also turn this off (above).  

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
 `palpolate` (<em>pal</em>-(ette inter)-<em>polate</em>):   
    input lists of any size and user can control output size. 

There are a multitude of beautiful gradients in packages like bokeh and colorcet that are, for the most part, static. The interpolation scheme here can be used to create entirely new ones given only a few endpoints. This part is still in development, but currently uses linear or polynomial fits in color space metrics RGB, HSL, or HSV. Heatmaps are a good way to visualize the results!

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/3interpolate1.png" width="89%" height="89%">

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/3interpolate2.png" width="110%" height="100%">


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




## gallery :rainbow:
**frieda**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/frieda.png" width="89%" height="89%">



**plath**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/plath.png" width="89%" height="89%">

**selah**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/selah.png" width="89%" height="89%">

**blonde**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/blonde.png" width="89%" height="89%">

**honeycombe**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/honeycombe.png" width="89%" height="89%">

**lysergic**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/lysergic.png" width="89%" height="89%">


**pepo**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pepo.png" width="89%" height="89%">

**reese**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/reese.png" width="89%" height="89%">

**rainbow**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/rainbow.png" width="89%" height="89%">

**lufte**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/lufte.png" width="89%" height="89%">

**pitaya**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pitaya.png" width="89%" height="89%">

**crepuscule**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/crepuscle.png" width="89%" height="89%">

**spiff**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/spiff.png" width="89%" height="89%">

**leather**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/leather.png" width="89%" height="89%">

**eleven**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/eleven.png" width="89%" height="89%">

**chilaquiles**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/chilaquiles.png" width="89%" height="89%">

**fiestaware**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/fiestaware.png" width="89%" height="89%">

**splenda**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/splenda.png" width="89%" height="89%">

**medium**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/medium.png" width="89%" height="89%">

**juniper**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/juniper.png" width="89%" height="89%">

**pollen**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pollen.png" width="89%" height="89%">


**fraiche**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/fraiche.png" width="89%" height="89%">

**polya**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/polya.png" width="89%" height="89%">

**cheshire**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/cheshire.png" width="89%" height="89%">


**joan**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/joan.png" width="89%" height="89%">

**pinot**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pinot.png" width="89%" height="89%">

**salvia**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/salvia.png" width="89%" height="89%">


**addams**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/addams.png" width="89%" height="89%">

**minuit**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/minuit.png" width="89%" height="89%">

**fugazi**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/fugazi.png" width="89%" height="89%">

**clementine**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/clementine.png" width="89%" height="89%">

**mona**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/mona.png" width="89%" height="89%">

**leda**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/leda.png" width="89%" height="89%">

**pugsley**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pugsley.png" width="89%" height="89%">

**bellhooks**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/bellhooks.png" width="89%" height="89%">

**oolong**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/oolong.png" width="89%" height="89%">

**alice**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/alice.png" width="89%" height="89%">

**wes**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/wes.png" width="89%" height="89%">

**belle**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/belle.png" width="89%" height="89%">

**neko**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/neko.png" width="89%" height="89%">

**phoebe**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/phoebe.png" width="89%" height="89%">

**pam**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/pam.png" width="89%" height="89%">

**dwight**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/dwight.png" width="89%" height="89%">

**riley**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/riley.png" width="89%" height="89%">

**ostrich**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/ostrich.png" width="89%" height="89%">

**eeyore**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/eeyore.png" width="89%" height="89%">

**yoshi**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/yoshi.png" width="89%" height="89%">


**moxxi**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/moxxi.png" width="89%" height="89%">


**carmine**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/carmine.png" width="89%" height="89%">

**bluefish**

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/bluefish.png" width="89%" height="89%">

**joker***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/joker.png" width="89%" height="89%">

**rach\***

<img src="https://raw.githubusercontent.com/atisor73/chromatose/master/imgs/rach.png" width="89%" height="89%">



*"The last color she remembered was the indigo chips in the headstone. After that she became as color conscious as a hen."* 
