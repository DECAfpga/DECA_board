###########################################
#
# DECA FPGA based on example script to build a
# pinout diagram. Includes basic
# features and convenience classes.
#
###########################################

from pinout.core import Group, Image, Rect
from pinout.components.layout import Diagram, Panel, ClipPath
from pinout.components.pinlabel import PinLabelGroup, PinLabel
from pinout.components.text import TextBlock
from pinout.components import leaderline as lline
from pinout.components.legend import Legend


# Import data for the diagram
import data

# Create a new diagram
diagram = Diagram(1480, 920, "diagram")

# Add a stylesheet
diagram.add_stylesheet("styles.css", embed=True)

# Create a layout
content = diagram.add(
    Panel(
        width=1480,
        height=800,
        inset=(2, 2, 2, 2),
    )
)
panel_main = content.add(
    Panel(
        width=content.inset_width,
        height=content.inset_height,
        inset=(2, 2, 2, 2),
        tag="panel--main",
    )
)
panel_info = content.add(
    Panel(
        x=0,
        y=panel_main.height,
        width=panel_main.width,
        height=content.inset_height - panel_main.height,
        inset=(2, 2, 2, 2),
        tag="panel--info",
    )
)

# Create a group to hold the pinout-diagram components.
graphic = panel_main.add(Group(420, 20))

# Add and embed an image
hardware_img = graphic.add(
    Image("./decaboard.png", width=652, height=1462, embed=True)
)

# Right hand side double-header P8 connector
############################################

# Create a single pin label
#graphic.add(
#    PinLabel(
#        content="P8",
#        x=650,
#        y=30,
#        tag="gnd",
#        body={"x": 0, "y": 0},
#    )
#)

# P8 connector text label
P8_connector = panel_main.add(
    TextBlock(
        data.P8,
        x=1200,
        y=60,
        line_height=10,
        tag="panel P8_connector",
    )
)

# Create pinlabels on the outer side
graphic.add(
    PinLabelGroup(
        x=598,
        y=129,
        body={"width": 110, "height": 20},
        pin_pitch=(0, 27),
        label_start=(260, 0),
        label_pitch=(0, 27),
        scale=(1, 1),
        labels=data.rhs_outer_numbered,
    )
)

# Create pinlabels on the inner side
graphic.add(
    PinLabelGroup(
        x=572,
        y=129,
        body={"width": 110, "height": 20},
        pin_pitch=(0, 27),
        label_start=(100, 15),
        label_pitch=(0, -27),
        scale=(1, -1),
        labels=data.rhs_inner_numbered,
        leaderline=lline.Curved(direction="vh"),
    )
)

# Left hand side double-header P9 connector
###########################################

# P9 connector text label
P8_connector = panel_main.add(
    TextBlock(
        data.P9,
        x=200,
        y=60,
        line_height=10,
        tag="panel P9_connector",
    )
)

# Create pinlabels on the inner side
graphic.add(
    PinLabelGroup(
        x=78,
        y=129,
        body={"width": 110, "height": 20},
        pin_pitch=(0, 27),
        label_start=(100, 15),
        label_pitch=(0, 27),
        scale=(-1, 1),
        labels=data.lhs_inner_numbered,
        leaderline=lline.Curved(direction="vh"),
    )
)

# Create pinlabels on the outer side
graphic.add(
    PinLabelGroup(
        x=52,
        y=129,
        body={"width": 110, "height": 20},
        pin_pitch=(0, 27),
        label_start=(280, 0),
        label_pitch=(0, 27),
        scale=(-1, 1),
        labels=data.lhs_outer_numbered,
    )
)


# Create a title and a text-block
title_block = panel_info.add(
    TextBlock(
        data.title,
        x=20,
        y=30,
        line_height=18,
        tag="panel title_block",
    )
)

panel_info.add(
    TextBlock(
        data.description,
        x=20,
        y=60,
        width=title_block.width,
        height=panel_info.height - title_block.height,
        line_height=18,
        tag="panel text_block",
    )
)

# Create a legend
legend = panel_info.add(
    Legend(
        data.legend,
        x=340,
        y=8,
        max_height=132,
    )
)


# build from cmd:
# >>> python3 -m pinout.manager --export pinout_deca pinout_deca.svg
