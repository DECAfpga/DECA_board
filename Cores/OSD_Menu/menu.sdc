# Clock constraints
create_clock -period "50.0 MHz" [get_ports iCLK]
create_clock -name {SPI_SCK}  -period 10.000 -waveform { 0.000 0.500 } [get_ports {SPI_SCK}]

# Automatically constrain PLL and other generated clocks
derive_pll_clocks -create_base_clocks

# Automatically calculate clock uncertainty to jitter and other effects.
derive_clock_uncertainty
