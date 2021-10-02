###########################################
# Script to build pinout diagram.
# Build from cmd:
# >>> python3 -m pinout.manager --export pinout_deca pinout_deca.png
###########################################

from pinout.core import Group, Image
from pinout.components.layout import Diagram_2Rows
from pinout.components.pinlabel import PinLabelGroup, PinLabel
from pinout.components.text import TextBlock
from pinout.components import leaderline as lline
from pinout.components.legend import Legend


# Import data for the diagram
import data

# Create a new diagram
# The Diagram_2Rows class provides 2 panels,
# 'panel_01' and 'panel_02', to insert components into.
diagram = Diagram_2Rows(1750, 930, 800, "diagram")

# Add a stylesheet
diagram.add_stylesheet("styles.css", embed=True)

# Create a group to hold the pinout-diagram components.
graphic = diagram.panel_01.add(Group(540, 20))

# Add and embed an image
hardware_img = graphic.add(
    Image("./board_deca.png", width=652, height=1462, embed=True)
)

# Right hand side double-header P8 connector
############################################

# Create a single pin label
graphic.add(
    PinLabel(
        content="1",
        x=44,
        y=55,
        tag="pwr",
        body={"width": 20, "height": 20},
    )
)

# P8 connector text label
diagram.panel_01.add(
    TextBlock(
        data.P8,
        x=1300,
        y=60,
        line_height=10,
        tag="panel P8_connector",
    )
)

# Create pin label on the outer side
graphic.add(
    PinLabelGroup(
        x=626,
        y=85,
        body={"width": 110, "height": 20},
        pin_pitch=(0, 28),
        label_start=(310, 0),
        label_pitch=(0, 28),
        scale=(1, 1),
        labels=data.rhs_outer_numbered,
    )
)

# Create pin label on the inner side
graphic.add(
    PinLabelGroup(
        x=600,
        y=85,
        body={"width": 110, "height": 20},
        pin_pitch=(0, 28),
        label_start=(60, 0),  # 15 to Offset
        label_pitch=(0, -28),
        scale=(1, -1),
        labels=data.rhs_inner_numbered,
        leaderline=lline.Curved(direction="vh"),
    )
)



# Left hand side double-header P9 connector
###########################################

# Create a single pin label
graphic.add(
    PinLabel(
        content="1",
        x=585,
        y=55,
        tag="pwr",
        body={"width": 20, "height": 20},
    )
)

# P9 connector text label
diagram.panel_01.add(
    TextBlock(
        data.P9,
        x=310,
        y=60,
        line_height=10,
        tag="panel P9_connector",
    )
)

# Create pin label on the outer side
graphic.add(
    PinLabelGroup(
        x=62,
        y=85,
        body={"width": 110, "height": 20},
        pin_pitch=(0, 28),
        label_start=(300, 0),
        label_pitch=(0, 28),
        scale=(-1, 1),
        labels=data.lhs_outer_numbered,
    )
)

# Create pin label on the inner side
graphic.add(
    PinLabelGroup(
        x=88,
        y=85,
        body={"width": 110, "height": 20},
        pin_pitch=(0, 28),
        label_start=(50, 0),  # 15 to Offset
        label_pitch=(0, 28),
        scale=(-1, 1),
        labels=data.lhs_inner_numbered,
        leaderline=lline.Curved(direction="vh"),
    )
)


# Legend
###########################################


# Create a title and a text-block
title_block = diagram.panel_02.add(
    TextBlock(
        data.title,
        x=20,
        y=30,
        line_height=18,
        tag="panel title_block",
    )
)

diagram.panel_02.add(
    TextBlock(
        data.description,
        x=20,
        y=60,
        width=title_block.width,
        height=diagram.panel_02.height - title_block.height,
        line_height=18,
        tag="panel text_block",
    )
)

# Create a legend
legend = diagram.panel_02.add(
    Legend(
        data.legend,
        x=360,
        y=8,
        max_height=136,
    )
)

# Export the diagram via commandline:
# >>> python3 -m pinout.manager --export pinout_deca pinout_deca.svg
