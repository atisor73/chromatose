
import warnings
import numpy as np
import panel as pn
pn.extension()

from .utils import *

# css = """
# .bk.panel-container {
#     background: "#999999";          /* light gray background*/
#     border-radius: 10px;            /* circular edge */
#     border: 0px #e6472c solid;         /* border properties */
#
# }
# .bk.panel-colorpicker {
#     font-family: "Open Sans"
#     font-size: 33px;
#     background: "#ff0000";
#     border: 0px #e6472c solid;         /* border properties */
# }
# .bk.panel-button {
#     font-family: "Open Sans"
#     font-size: 55px;
# }
# .bk.panel-pane {
#     text-align: center;
# }
# """
# pn.extension(raw_css = [css])

def _get_dimensions(n):
    d_width = {1: 300, 2: 300, 3: 400, 4: 600,
               5: 600, 6: 600, 7: 750, 8: 750,}
    max_width = d_width[n]
    width = int(max_width / n )
    height = int(1.1*width)

    return width, height, max_width

def _widgeting(n=None, palette=None):
    diverging = ['#cb4f70',
                         '#1b718c',
                         '#779e1a',
                         '#f49044',
                         '#46308d',
                         '#2ea58e',
                         '#e97d86',
                         '#7e92bd',
                         '#c21019',
                         '#f56327',
                         '#fab01d',
                         '#026f69',
                         '#750a2b',
                         '#1b9e77',
                         '#d95f02',
                         '#7570b3',
                         '#e7298a',
                         '#66a61e'
                       ]
    if   (n == None) & (palette==None):              n, palette = 5, diverging[:5]
    elif (n == None) & (type(palette) == list):      n = len(palette)
    elif (type(n) == int) & (palette == None):       palette = diverging[:n]
    elif (type(n) == int) & (type(palette) == list): palette = palette[:n]
    elif (type(n) == list):
        palette = n
        n = len(palette)

    elif (type(n) in [str, tuple]):
        return pn.widgets.ColorPicker(value=n, width=350, height=250)

    else:
        warnings.warn("\nInvalid input. Using default...", stacklevel=2)
        n, palette = 5, diverging
    if n > 8:
        warnings.warn("\n'n' too large. Capping n = 8", stacklevel=2)
        n = 8
    palette = hex_palette(palette)

    width, height, max_width = _get_dimensions(n)

    widgets = [ pn.widgets.ColorPicker(
                    value=palette[i],
                    width=width,
                    height=height,
                    margin=(-10, -10, -10, -10),
                    sizing_mode="stretch_both"
                    )
               for i in range(min(n, len(palette))) ]

    return widgets, max_width, min(n, len(palette))

def palpicker(n=None, palette=None):
    """
    Pass in either integer number or palette
    Max of 8.
    """
    button = pn.widgets.Button(name="record", button_type="primary",
                               height=40, margin=[15, 0, 0, 0])
    def prnt(event):
        print("[", end="")
        for widget in widgets:
            print(f" \"{widget.value},\" ", end="    ")
        print("]")
    button.on_click(prnt)

    if type(n) in [str, tuple]:
        picker = pn.widgets.ColorPicker(
                    value=n,
                    width=300,
                    height=125,
                    background="grey",
                    margin=[0, 0, 0, 0]
                )
        pane = pn.pane.Markdown(
                    object=str(picker.value),
                    sizing_mode="stretch_height",
                    style={
                    'font-family': 'Courier',
                        'font-size':'12px',
                         'font-style':'normal',
                         'color':'#666666',
                    }
                )

        def callback(*events):
            for event in events:
                if event.name == "value":
                    pane.object = f"# {event.new}"

        watcher = picker.param.watch(callback, ["value"])
        picker.param.trigger('value')
        return pn.Row(picker, pane)

    widgets, max_width, n = _widgeting(n, palette)
    panes = [pn.pane.Markdown(object=f"# {widgets[_].value}",
                              sizing_mode="stretch_both",
                              style={
                                  'font-family': 'Courier',
                                     'font-size':'12px',
                                     'font-style':'normal',
                                     'color':'#666666',
                                    },
                             ) for _ in range(n)]

    def callback0(*events):
        for event in events:
            if event.name == "value":
                panes[0].object = f"# {event.new}"
    def callback1(*events):
        for event in events:
            if event.name == "value":
                panes[1].object = f"# {event.new}"
    def callback2(*events):
        for event in events:
            if event.name == "value":
                panes[2].object = f"# {event.new}"
    def callback3(*events):
        for event in events:
            if event.name == "value":
                panes[3].object = f"# {event.new}"
    def callback4(*events):
        for event in events:
            if event.name == "value":
                panes[4].object = f"# {event.new}"
    def callback5(*events):
        for event in events:
            if event.name == "value":
                panes[5].object = f"# {event.new}"
    def callback6(*events):
        for event in events:
            if event.name == "value":
                panes[6].object = f"# {event.new}"
    def callback7(*events):
        for event in events:
            if event.name == "value":
                panes[7].object = f"# {event.new}"

    callbacks = [callback0, callback1, callback2, callback3,
                 callback4, callback5, callback6, callback7 ]
    try:
        watcher0 = widgets[0].param.watch(callbacks[0], ["value"])
        watcher1 = widgets[1].param.watch(callbacks[1], ["value"])
        watcher2 = widgets[2].param.watch(callbacks[2], ["value"])
        watcher3 = widgets[3].param.watch(callbacks[3], ["value"])
        watcher4 = widgets[4].param.watch(callbacks[4], ["value"])
        watcher5 = widgets[5].param.watch(callbacks[5], ["value"])
        watcher6 = widgets[6].param.watch(callbacks[6], ["value"])
        watcher7 = widgets[7].param.watch(callbacks[7], ["value"])

        widgets[0].param.trigger("value")
        widgets[1].param.trigger("value")
        widgets[2].param.trigger("value")
        widgets[3].param.trigger("value")
        widgets[4].param.trigger("value")
        widgets[5].param.trigger("value")
        widgets[6].param.trigger("value")
        widgets[7].param.trigger("value")

    except:
        pass

    return pn.Column(
            pn.Row(*panes, width=max_width),
            pn.Row(*widgets, width=max_width),
            button
           )
