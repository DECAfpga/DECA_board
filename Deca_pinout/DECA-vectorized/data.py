legend = [
    ("PIN NUMBER", "pinid"),
    ("POWER", "pwr"),
    ("GROUND", "gnd"),
    ("PULL-UP RESISTOR", "touch"),
    ("FPGA PIN LOCATION", "gpsingle"),
    ("GPIO", "gpio"),
    ("ANALOG/GPIO", "analog"),
]

# Pin labels
gnd = ("GND", "gnd")
pwr = ("3.3V", "pwr")

##############################
# LHS
lhs_outer_numbered = [
    [
        ("1", "pinid", {"body": {"width": 30, "height": 20}}),
        ("GND", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("3", "pinid", {"body": {"width": 30, "height": 20}}),
        ("VDD 3V3", "pwr", {"body": {"width": 60, "height": 20}}),
    ],
    [
        ("5", "pinid", {"body": {"width": 30, "height": 20}}),
        ("VDD 5V", "pwr", {"body": {"width": 60, "height": 20}}),
    ],
    [
        ("7", "pinid", {"body": {"width": 30, "height": 20}}),
        ("VDD 5V", "pwr", {"body": {"width": 60, "height": 20}}),
    ],
    [
        ("9", "pinid", {"body": {"width": 30, "height": 20}}),
        ("U6", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("PWR_BUT", "gpio", {"body": {"width": 85, "height": 20}}),
        ("10K", "touch", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("11", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y5", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[0]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("13", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W6", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[2]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("15", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W8", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[4]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("17", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB8", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[6]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("19", "pinid", {"body": {"width": 30, "height": 20}}),
        ("R11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[8]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("21", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB6", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[10]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("23", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA6", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[12]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("25", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V10", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[14]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("27", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W9", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[16]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("29", "pinid", {"body": {"width": 30, "height": 20}}),
        ("R9", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[18]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("31", "pinid", {"body": {"width": 30, "height": 20}}),
        ("P9", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[20]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("33", "pinid", {"body": {"width": 30, "height": 20}}),
        ("K5", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("AIN6", "analog", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("35", "pinid", {"body": {"width": 30, "height": 20}}),
        ("J4", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("AIN4", "analog", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("37", "pinid", {"body": {"width": 30, "height": 20}}),
        ("J8", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("AIN2", "analog", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("39", "pinid", {"body": {"width": 30, "height": 20}}),
        ("F5", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("AIN0", "analog", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("41", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V17", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[21]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("43", "pinid", {"body": {"width": 30, "height": 20}}),
        ("GND", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("45", "pinid", {"body": {"width": 30, "height": 20}}),
        ("GND", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
]

lhs_inner_numbered = [
    [
        ("2", "pinid", {"body": {"width": 30, "height": 20}}),
        ("GND", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("4", "pinid", {"body": {"width": 30, "height": 20}}),
        ("VDD 3V3", "pwr", {"body": {"width": 60, "height": 20}}),
    ],
    [
        ("6", "pinid", {"body": {"width": 30, "height": 20}}),
        ("VDD 5V", "pwr", {"body": {"width": 60, "height": 20}}),
    ],
    [
        ("8", "pinid", {"body": {"width": 30, "height": 20}}),
        ("VDD 5V", "pwr", {"body": {"width": 60, "height": 20}}),
    ],
    [
        ("10", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA2", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("SYS_RESET_n", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("12", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y6", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[1]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("14", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W7", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[3]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("16", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V8", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[5]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("18", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V7", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[7]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("20", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB7", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[9]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("22", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA7", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[11]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("24", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y7", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[13]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("26", "pinid", {"body": {"width": 30, "height": 20}}),
        ("U7", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[15]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("28", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W5", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[17]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("30", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W4", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[19]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("32", "pinid", {"body": {"width": 30, "height": 20}}),
        ("A1V8", "pwr", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("34", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AGND", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("36", "pinid", {"body": {"width": 30, "height": 20}}),
        ("H3", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("AIN5", "analog", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("38", "pinid", {"body": {"width": 30, "height": 20}}),
        ("J9", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("AIN3", "analog", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("40", "pinid", {"body": {"width": 30, "height": 20}}),
        ("F4", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("AIN1", "analog", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("42", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W3", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO1_D[22]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("44", "pinid", {"body": {"width": 30, "height": 20}}),
        ("GND", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("46", "pinid", {"body": {"width": 30, "height": 20}}),
        ("GND", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
]

##############################
# RHS
rhs_outer_numbered = [
    [
        ("2", "pinid", {"body": {"width": 30, "height": 20}}),
        ("GND", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("4", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y18", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[1]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("6", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA17", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[3]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("8", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA19", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[5]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("10", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB20", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[7]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("12", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[9]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("14", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB18", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[11]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("16", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W17", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[13]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("18", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[15]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("20", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[17]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("22", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[19]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("24", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[21]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("26", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[23]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("28", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[25]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("30", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA12", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[27]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("32", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[29]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("34", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[31]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("36", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[33]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("38", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[35]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("40", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[37]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("42", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[39]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("44", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[41]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("46", "pinid", {"body": {"width": 30, "height": 20}}),
        ("R13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[43]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
]

rhs_inner_numbered = [
    [
        ("1", "pinid", {"body": {"width": 30, "height": 20}}),
        ("GND", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("3", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W18", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[0]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("5", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y19", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[2]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("7", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA20", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[4]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("9", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB21", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[6]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("11", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB19", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[8]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("13", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[10]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("15", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[12]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("17", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB17", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[14]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("19", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[16]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("21", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[18]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("23", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[20]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("25", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[22]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("27", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[24]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("29", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB12", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[26]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("31", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[28]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("33", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB10", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[30]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("35", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[32]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("37", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W12", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[34]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("39", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V12", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[36]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("41", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[38]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("43", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y17", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[40]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("45", "pinid", {"body": {"width": 30, "height": 20}}),
        ("U15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO0_D[42]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
]

# Text
title = "<tspan class='h1'>DECA FPGA Pinout</tspan>"

description = "Made with Pinout\n" \
              "For more information please visit\n" \
              "<tspan class='italic strong'>pinout.readthedocs.io</tspan>."

P8 = "<tspan class='h1'>P8 Connector</tspan>"

P9 = "<tspan class='h1'>P9 Connector</tspan>"
