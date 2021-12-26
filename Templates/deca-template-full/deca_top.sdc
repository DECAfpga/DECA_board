create_clock -name {clk_50} -period 20.000 -waveform {0.000 10.000} { MAX10_CLK1_50 }

#set sysclk pll|altpll_component|auto_generated|pll1|clk[0]

derive_pll_clocks -create_base_clocks
derive_clock_uncertainty

# Create a clock for i2s
#create_clock -name i2sclk -period 20.000 {audio_top:audio_i2s|tcount[4]}

# Some relaxed constrain to the VGA pins. The signals should arrive together, the delay is not really important.
set VGA_OUT {VGA_R[*] VGA_G[*] VGA_B[*] VGA_HS VGA_VS}

#set_output_delay -clock [get_clocks $sysclk] -max 0 [get_ports $VGA_OUT]
#set_output_delay -clock [get_clocks $sysclk] -min -5 [get_ports $VGA_OUT]

#set_multicycle_path -to $VGA_OUT -setup 2
#set_multicycle_path -to $VGA_OUT -hold 1

# non timing-critical pins would be in the "FALSE_IN/OUT" collection (IN inputs, OUT outputs)
#set FALSE_OUT {LED[*] SIGMA_* PS2_* JOYX_SEL_O AUDIO* I2S_* HDMI_I2C* HDMI_LRCLK HDMI_MCLK HDMI_SCLK HDMI_I2S[*] UART_TXD SD_CS_N_O SD_MOSI_O SD_SCLK_O HDMI_TX*}
#set FALSE_IN  {KEY[*] SW[*] PS2_* JOY1* AUDIO* HDMI_I2C* HDMI_LRCLK HDMI_MCLK HDMI_SCLK HDMI_I2S[*] EAR UART_RXD SD_MISO_I HDMI_TX_INT}

set FALSE_OUT {JOYX_SEL_O}
set FALSE_IN  {KEY[*]}


set_false_path -to ${FALSE_OUT}
set_false_path -from ${FALSE_IN}
