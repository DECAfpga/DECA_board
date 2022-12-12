legend = [
    ("PIN NUMBER", "pinid"),
    ("POWER", "pwr"),
    ("GROUND", "gnd"),
    ("PULL-UP RESISTOR", "touch"),
    ("FPGA PIN LOCAT.", "gpsingle"),
    ("GPIO 3V3", "gpio"),
    ("GPIO 2V5 (AIN)", "analog"),
    ("",""),
    ("VGA", "pwm"),
    ("PS2","comms"),
    ("SDRAM","sdram"),
    #("PMOD3","touch"),
    ("JOYSTICK","pmod5"),
    ("PMOD3","pmod3"),
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
        ("3V3", "pwr", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("5", "pinid", {"body": {"width": 30, "height": 20}}),
        ("5V", "pwr", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("7", "pinid", {"body": {"width": 30, "height": 20}}),
        ("5V", "pwr", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("9", "pinid", {"body": {"width": 30, "height": 20}}),
        ("U6", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("PWR", "gpio", {"body": {"width": 40, "height": 20}}),
        ("PS2-DAT-MOUS", "comms", {"body": {"width": 100, "height": 20}}),
        ("10K", "touch", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("11", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y5", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D0", "gpio", {"body": {"width": 40, "height": 20}}),
        ("PS2-CLK-KEYB", "comms", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("13", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W6", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D2", "gpio", {"body": {"width": 40, "height": 20}}),
        ("VGA-VSYNC", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("15", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W8", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D4", "gpio", {"body": {"width": 40, "height": 20}}),
        ("VGA-BLUE0", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("17", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB8", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D6", "gpio", {"body": {"width": 40, "height": 20}}),
        ("VGA-GREEN0", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("19", "pinid", {"body": {"width": 30, "height": 20}}),
        ("R11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D8", "gpio", {"body": {"width": 40, "height": 20}}),
        ("VGA-GREEN2", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("21", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB6", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D10", "gpio", {"body": {"width": 40, "height": 20}}),
        ("VGA-BLUE3", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("23", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA6", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D12", "gpio", {"body": {"width": 40, "height": 20}}),
        ("VGA-BLUE2", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("25", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V10", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D14", "gpio", {"body": {"width": 40, "height": 20}}),
        ("VGA-BLUE1", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("27", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W9", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D16", "gpio", {"body": {"width": 40, "height": 20}}),
        #("VGA/PMOD12", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("29", "pinid", {"body": {"width": 30, "height": 20}}),
        ("R9", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D18", "gpio", {"body": {"width": 40, "height": 20}}),
        ("MIDI_WSBD", "pmod3", {"body": {"width": 100, "height": 20}}), 
    ],
    [
        ("31", "pinid", {"body": {"width": 30, "height": 20}}),
        ("P9", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D20", "gpio", {"body": {"width": 40, "height": 20}}),
        ("MIDI_DABD", "pmod3", {"body": {"width": 100, "height": 20}}),         
    ],
    [
        ("33", "pinid", {"body": {"width": 30, "height": 20}}),
        ("K5", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("AIN6", "analog", {"body": {"width": 40, "height": 20}}),
        ("JOY-P7", "pmod5", {"body": {"width": 100, "height": 20}}), 
    ],
    [
        ("35", "pinid", {"body": {"width": 30, "height": 20}}),
        ("J4", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("AIN4", "analog", {"body": {"width": 40, "height": 20}}),
        ("JOY-P9", "pmod5", {"body": {"width": 100, "height": 20}}), 
    ],
    [
        ("37", "pinid", {"body": {"width": 30, "height": 20}}),
        ("J8", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("AIN2", "analog", {"body": {"width": 40, "height": 20}}),
        ("JOY-UP", "pmod5", {"body": {"width": 100, "height": 20}}), 
    ],
    [
        ("39", "pinid", {"body": {"width": 30, "height": 20}}),
        ("F5", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("AIN0", "analog", {"body": {"width": 40, "height": 20}}),
        ("JOY-RIGHT", "pmod5", {"body": {"width": 100, "height": 20}}), 
    ],
    [
        ("41", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V17", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D21", "gpio", {"body": {"width": 40, "height": 20}}),
        #("PMOD4/MCU", "pmod4", {"body": {"width": 100, "height": 20}}), 
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
        ("3V3", "pwr", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("6", "pinid", {"body": {"width": 30, "height": 20}}),
        ("5V", "pwr", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("8", "pinid", {"body": {"width": 30, "height": 20}}),
        ("5V", "pwr", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("10", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA2", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("RES", "gpio", {"body": {"width": 40, "height": 20}}),
        ("PS2-CLK-MOUS", "comms", {"body": {"width": 100, "height": 20}}),
        
    ],
    [
        ("12", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y6", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D1", "gpio", {"body": {"width": 40, "height": 20}}),
        ("PS2-DAT-KEYB", "comms", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("14", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W7", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D3", "gpio", {"body": {"width": 40, "height": 20}}),
        ("VGA-HSYNC", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("16", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V8", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D5", "gpio", {"body": {"width": 40, "height": 20}}),
        ("VGA-RED0", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("18", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V7", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D7", "gpio", {"body": {"width": 40, "height": 20}}),
        ("VGA-GREEN3", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("20", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB7", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D9", "gpio", {"body": {"width": 40, "height": 20}}),
        ("VGA-GREEN1", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("22", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA7", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D11", "gpio", {"body": {"width": 40, "height": 20}}),
        ("VGA-RED3", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("24", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y7", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D13", "gpio", {"body": {"width": 40, "height": 20}}),
        ("VGA-RED2", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("26", "pinid", {"body": {"width": 30, "height": 20}}),
        ("U7", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D15", "gpio", {"body": {"width": 40, "height": 20}}),
        ("VGA-RED1", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("28", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W5", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D17", "gpio", {"body": {"width": 40, "height": 20}}),
        #("VGA/PMOD12", "pwm", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("30", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W4", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D19", "gpio", {"body": {"width": 40, "height": 20}}),
        #("PMOD4/MCU", "pmod4", {"body": {"width": 100, "height": 20}}), 
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
        ("JOY-P6", "pmod5", {"body": {"width": 100, "height": 20}}), 
    ],
    [
        ("38", "pinid", {"body": {"width": 30, "height": 20}}),
        ("J9", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("AIN3", "analog", {"body": {"width": 40, "height": 20}}),
        ("JOY-DOWN", "pmod5", {"body": {"width": 100, "height": 20}}), 
    ],
    [
        ("40", "pinid", {"body": {"width": 30, "height": 20}}),
        ("F4", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("AIN1", "analog", {"body": {"width": 40, "height": 20}}),
        ("JOY-LEFT", "pmod5", {"body": {"width": 100, "height": 20}}), 
    ],
    [
        ("42", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W3", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("1D22", "gpio", {"body": {"width": 40, "height": 20}}),
        #("PMOD4/MCU", "pmod4", {"body": {"width": 100, "height": 20}}), 
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
        ("0D1", "gpio", {"body": {"width": 40, "height": 20}}),
        ("UART_RXD", "pmod3", {"body": {"width": 100, "height": 20}}), 

    ],
    [
        ("6", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA17", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D3", "gpio", {"body": {"width": 40, "height": 20}}),
        #("AUDIO-R", "pmod3", {"body": {"width": 100, "height": 20}}), 
    ],
    [
        ("8", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA19", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D5", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("10", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB20", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D7", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("12", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D9", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("14", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB18", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D11", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("16", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W17", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D13", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("18", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D15", "gpio", {"body": {"width": 40, "height": 20}}),
        ("UDQM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("20", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D17", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("22", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D19", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("24", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D21", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("26", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D23", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("28", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D25", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("30", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA12", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D27", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("32", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D29", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("34", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D31", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("36", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D33", "gpio", {"body": {"width": 40, "height": 20}}),
        ("CKE", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("38", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D35", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("40", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D37", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("42", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D39", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("44", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D41", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("46", "pinid", {"body": {"width": 30, "height": 20}}),
        ("R13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D43", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
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
        ("0D0", "gpio", {"body": {"width": 40, "height": 20}}),
        ("UART_TXD", "pmod3", {"body": {"width": 100, "height": 20}}), 
    ],
    [
        ("5", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y19", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D2", "gpio", {"body": {"width": 40, "height": 20}}),
        ("MIDI_CLKBD", "pmod3", {"body": {"width": 100, "height": 20}}), 

    ],
    [
        ("7", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA20", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D4", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("9", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB21", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D6", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("11", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB19", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D8", "gpio", {"body": {"width": 40, "height": 20}}),
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("13", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D10", "gpio", {"body": {"width": 40, "height": 20}}),      
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),
    ],
    [
        ("15", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D12", "gpio", {"body": {"width": 40, "height": 20}}),   
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),   
    ],
    [
        ("17", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB17", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D14", "gpio", {"body": {"width": 40, "height": 20}}),     
        ("LDQM", "sdram", {"body": {"width": 100, "height": 20}}),  
    ],
    [
        ("19", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D16", "gpio", {"body": {"width": 40, "height": 20}}),    
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),  
    ],
    [
        ("21", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D18", "gpio", {"body": {"width": 40, "height": 20}}),     
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}), 
    ],
    [
        ("23", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D20", "gpio", {"body": {"width": 40, "height": 20}}),    
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),  
    ],
    [
        ("25", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D22", "gpio", {"body": {"width": 40, "height": 20}}),    
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),  
    ],
    [
        ("27", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D24", "gpio", {"body": {"width": 40, "height": 20}}),    
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),  
    ],
    [
        ("29", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB12", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D26", "gpio", {"body": {"width": 40, "height": 20}}),   
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),   
    ],
    [
        ("31", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D28", "gpio", {"body": {"width": 40, "height": 20}}),  
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),    
    ],
    [
        ("33", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB10", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D30", "gpio", {"body": {"width": 40, "height": 20}}),   
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),   
    ],
    [
        ("35", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D32", "gpio", {"body": {"width": 40, "height": 20}}),   
        #("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),   
    ],
    [
        ("37", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W12", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D34", "gpio", {"body": {"width": 40, "height": 20}}),   
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),   
    ],
    [
        ("39", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V12", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D36", "gpio", {"body": {"width": 40, "height": 20}}),   
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),   
    ],
    [
        ("41", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D38", "gpio", {"body": {"width": 40, "height": 20}}),   
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),   
    ],
    [
        ("43", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y17", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D40", "gpio", {"body": {"width": 40, "height": 20}}), 
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),     
    ],
    [
        ("45", "pinid", {"body": {"width": 30, "height": 20}}),
        ("U15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("0D42", "gpio", {"body": {"width": 40, "height": 20}}), 
        ("SDRAM", "sdram", {"body": {"width": 100, "height": 20}}),     
    ],
]

# Text
title = "<tspan class='h1'>DECA Cores Pinout v1.2</tspan>"

description = "Made with Pinout\n" \
              "For more information please visit\n" \
              "<tspan class='italic strong'>pinout.readthedocs.io</tspan>."

notes =       "<tspan class='strong'>NOTES:</tspan>\n" \
              "- Some features are optional to be connected\n" \
              "- 10k pull up resistor is internal of Deca board\n" \
              "\n" \
              "<tspan class='italic'>NOT ALL JOYSTICKS WILL WORK ATM. JOYSTICK CAN ONLY BE POWERED AT MAX 2.5V</tspan>.\n" \
              "<tspan class='italic strong'>ABOVE 2.6V MAY DAMAGE THE BOARD</tspan>.\n" \


#notes = "<tspan class='h1'>P8 Connector</tspan>"

P8 = "<tspan class='h1'>P8 Connector</tspan>"

P9 = "<tspan class='h1'>P9 Connector</tspan>"
