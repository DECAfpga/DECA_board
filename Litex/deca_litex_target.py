#!/usr/bin/env python3

#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2021 Hans Baier <hansfbaier@gmail.com>
# SPDX-License-Identifier: BSD-2-Clause

# To use the MiSTer SDRAM option, please connect the SDRAM
# module as described here:
# https://github.com/SoCFPGA-learning/DECA/tree/main/Projects/sdram_mister_deca

import os
import argparse

from migen import *
from litex_boards.platforms import deca

from litex.soc.cores.clock import Max10PLL
from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *
from litex.soc.cores.video import VideoDVIPHY
from litex.soc.cores.led import LedChaser
from litex.soc.cores.bitbang import I2CMaster

from litex_boards.targets.terasic_sockit import W9825G6KH6
from litex.build.io import DDROutput

from litedram.modules import AS4C32M16
from litedram.phy import HalfRateGENSDRPHY, GENSDRPHY
from litex.build.generic_platform import *


# CRG ----------------------------------------------------------------------------------------------

class _CRG(Module):
    def __init__(self, platform, sys_clk_freq, with_usb_pll=False, with_sdram=False, sdram_rate="1:2", with_video_terminal=False):
        self.rst = Signal()
        self.clock_domains.cd_sys    = ClockDomain()
        self.clock_domains.cd_usb    = ClockDomain()

        if with_video_terminal:
            self.clock_domains.cd_hdmi   = ClockDomain()

        if with_sdram:
            if sdram_rate == "1:2":
                self.clock_domains.cd_sys2x    = ClockDomain()
                self.clock_domains.cd_sys2x_ps = ClockDomain(reset_less=True)
            else:
                self.clock_domains.cd_sys_ps = ClockDomain(reset_less=True)

        # # #

        # Clk / Rst.
        clk50 = platform.request("clk50")

        # PLL
        self.submodules.pll = pll = Max10PLL(speedgrade="-6")
        self.comb += pll.reset.eq(self.rst)
        pll.register_clkin(clk50, 50e6)
        pll.create_clkout(self.cd_sys,  sys_clk_freq)

        if with_video_terminal:
            pll.create_clkout(self.cd_hdmi, 40e6)

        if with_sdram:
            if sdram_rate == "1:2":
                pll.create_clkout(self.cd_sys2x,    2*sys_clk_freq)
                pll.create_clkout(self.cd_sys2x_ps, 2*sys_clk_freq, phase=180)  # Idealy 90° but needs to be increased.
            else:
                pll.create_clkout(self.cd_sys_ps, sys_clk_freq, phase=90)

        # SDRAM clock
        if with_sdram:
            sdram_clk = ClockSignal("sys2x_ps" if sdram_rate == "1:2" else "sys_ps")
            self.specials += DDROutput(1, 0, platform.request("sdram_clock"), sdram_clk)

        # USB PLL.
        if with_usb_pll:
            ulpi  = platform.request("ulpi")
            self.comb += ulpi.cs.eq(1) # Enable ULPI chip to enable the ULPI clock.
            self.submodules.usb_pll = pll = Max10PLL(speedgrade="-6")
            self.comb += pll.reset.eq(self.rst)
            pll.register_clkin(ulpi.clk, 60e6)
            pll.create_clkout(self.cd_usb, 60e6, phase=-120) # -120° from DECA's example (also validated with LUNA).

# BaseSoC ------------------------------------------------------------------------------------------

class BaseSoC(SoCCore):
    def __init__(self, sys_clk_freq=int(50e6), with_video_terminal=False, sdram_rate="1:2", mister_sdram=None, **kwargs):
        self.platform = platform = deca.Platform()

        if mister_sdram != None:
            platform.add_extension([
                # MiSTer SDRAM (via GPIO expansion board on P8).
                ("sdram_clock", 0, Pins("P8:26"), IOStandard("3.3-V LVTTL")),
                ("sdram", 0,
                    Subsignal("a",     Pins(
                        "P8:43 P8:44 P8:45 P8:46 P8:34 P8:31 P8:32 P8:29",
                        "P8:30 P8:27 P8:42 P8:28 P8:25")),
                    Subsignal("ba",    Pins("P8:40 P8:41")),
                    Subsignal("cs_n",  Pins("P8:39")),
                    Subsignal("cke",   Pins("P8:18")), # CKE not connected on XS 2.2/2.4.
                    Subsignal("ras_n", Pins("P8:38")),
                    Subsignal("cas_n", Pins("P8:37")),
                    Subsignal("we_n",  Pins("P8:33")),
                    Subsignal("dq", Pins(
                        "P8:7  P8:8  P8:9  P8:10 P8:11 P8:12 P8:13 P8:14",
                        "P8:24 P8:23 P8:22 P8:21 P8:20 P8:19 P8:15 P8:16"),
                    ),
                    Subsignal("dm", Pins("P8:35 P8:36")), # DQML/DQMH not connected on XS 2.2/2.4
                    IOStandard("3.3-V LVTTL"),
                    Misc("CURRENT_STRENGTH_NEW \"MAXIMUM CURRENT\""),
                )
            ])

        # Defaults to JTAG-UART since no hardware UART.
        if kwargs["uart_name"] == "serial":
            kwargs["uart_name"] = "jtag_atlantic"

        # SoCCore ----------------------------------------------------------------------------------
        SoCCore.__init__(self, platform, sys_clk_freq,
            ident         = "LiteX SoC on Terasic DECA",
            ident_version = True,
            **kwargs)

        # CRG --------------------------------------------------------------------------------------
        self.submodules.crg = self.crg = _CRG(platform, sys_clk_freq, with_usb_pll=False, with_sdram=mister_sdram != None, sdram_rate=sdram_rate, with_video_terminal=False)

        # SDR SDRAM --------------------------------------------------------------------------------
        if mister_sdram is not None:
            sdrphy_cls = HalfRateGENSDRPHY if sdram_rate == "1:2" else GENSDRPHY
            sdrphy_mod = {"xs_v22": W9825G6KH6, "xs_v24": AS4C32M16}[mister_sdram]
            self.submodules.sdrphy = sdrphy_cls(platform.request("sdram"), sys_clk_freq)
            self.add_sdram("sdram",
                phy           = self.sdrphy,
                module        = sdrphy_mod(sys_clk_freq, sdram_rate),
                l2_cache_size = kwargs.get("l2_size", 8192)
            )

        # Video ------------------------------------------------------------------------------------
        if with_video_terminal:
            self.submodules.videophy = VideoDVIPHY(platform.request("hdmi"), clock_domain="hdmi")
            self.add_video_terminal(phy=self.videophy, timings="800x600@60Hz", clock_domain="hdmi")

        # Leds -------------------------------------------------------------------------------------
        self.submodules.leds = LedChaser(
            pads         = platform.request_all("user_led"),
            sys_clk_freq = sys_clk_freq)

# Build --------------------------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="LiteX SoC on DECA")
    parser.add_argument("--single-rate-sdram",   action="store_true", help="clock SDRAM with 1x the sytem clock (instead of 2x)")
    parser.add_argument("--mister-sdram-xs-v22", action="store_true", help="Use optional MiSTer SDRAM module XS v2.2 on J2 on GPIO daughter card")
    parser.add_argument("--mister-sdram-xs-v24", action="store_true", help="Use optional MiSTer SDRAM module XS v2.4 on J2 on GPIO daughter card")
    parser.add_argument("--build",               action="store_true", help="Build bitstream")
    parser.add_argument("--load",                action="store_true", help="Load bitstream")
    parser.add_argument("--sys-clk-freq",        default=50e6,        help="System clock frequency (default: 50MHz)")
    parser.add_argument("--with-video-terminal", action="store_true", help="Enable Video Terminal (VGA)")
    builder_args(parser)
    soc_core_args(parser)
    args = parser.parse_args()

    soc = BaseSoC(
        sys_clk_freq        = int(float(args.sys_clk_freq)),
        sdram_rate          = "1:1" if args.single_rate_sdram else "1:2",
        mister_sdram        = "xs_v22" if args.mister_sdram_xs_v22 else "xs_v24" if args.mister_sdram_xs_v24 else None,
        with_video_terminal = args.with_video_terminal,
        **soc_core_argdict(args)
    )
    builder = Builder(soc, **builder_argdict(args))
    builder.build(run=args.build)

    if args.load:
        prog = soc.platform.create_programmer()
        prog.load_bitstream(os.path.join(builder.gateware_dir, soc.build_name + ".sof"))

if __name__ == "__main__":
    main()
