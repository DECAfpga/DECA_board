# DECA Resources

Follows a list of useful resources that were published mainly in the [DECA telegram group](https://t.me/Deca_Max10_FPGA) that are related to  DECA and Max10 FPGA family.

(updated until 20/06/21)

[See also General FPGA Resources list](https://github.com/SoCFPGA-learning/General/blob/main/resources.md)

### General:

* Buy DECA at Arrow https://www.arrow.com/en/products/deca/arrow-development-tools

* Terasic website https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&CategoryNo=&No=944&PartNo=1 

* Video overview https://www.youtube.com/watch?v=8SaMVaniz8U

* DECA collaborative community repository https://github.com/SoCFPGA-learning/DECA  Repositorio colaborativo de la comunidad DECA

* Porting cores to DECA board  https://github.com/SoCFPGA-learning/DECA/tree/main/Tutorials/Porting-Cores

* Using DECA's integrated TLV320AIC3254 Audio DAC https://github.com/SoCFPGA-learning/DECA/tree/main/Tutorials/Porting-Cores/AudioCODEC

  

### Documentation:

* Intel Community Knowledge Base -DECA https://community.intel.com/t5/FPGA-Wiki/DECA/ta-p/735458

* Intel® MAX® 10 FPGA Configuration User Guide  https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/hb/max-10/ug_m10_config.pdf

* Intel® Max® 10 FPGAs Support https://www.intel.com/content/www/us/en/programmable/products/fpga/max-series/max-10/support.html

  

### DECA Labs / Tutorials:

*  **DECA Intel Community Knowledge Base** https://community.intel.com/t5/FPGA-Wiki/DECA/ta-p/735458      (GitHub with material from  Intel Community Knowledge Base  https://github.com/snikrepmada/DECA )
*  DECA Linux Tutorial For the MAX® 10 DECA FPGA Evaluation Kit https://www.intel.com/content/dam/altera-www/global/en_US/uploads/c/ca/DECA-Linux-Tutorial_15_1.pdf

### MAX10 Labs / Tutorials:

*  MAX1000:  All Verilog, C, and Quartus project files for the Texas State University EE Senior Design team 2.09FPGA/Verilog Project [Fall2019/Spring2020] - Creating FPGA examples for future students using the Arrow Max1000 https://github.com/Grant-Seligman/Max1000-FPGA-Senior-Design-Verilog-Code 
*  MAX1000: Tutorial and example projects for the Arrow MAX1000 FPGA board  https://github.com/vpecanins/max1000-tutorial 
*  DE10-Lite: EEC 180 - Digital Systems II - Spring 2021 - University of California - https://www.ece.ucdavis.edu/~bbaas/180/



### Reference Designs:

* Arrow Max 10 DECA Baseline Pinout | Design Store for Intel® FPGAs https://fpgacloud.intel.com/devstore/platform/16.0.0/Standard/arrow-max-10-deca-baseline-pinout/
* Design examples and reference designs for Intel® FPGAs https://fpgacloud.intel.com/devstore/platform/?page=1&board=9



### DECA Projects:

* Examples of bare metal RiscV programming with softcore on a fpga https://github.com/infphyny/FpgaRiscV

* Interfacing a BeagleBone BLE/Wi-Fi Cape with an Arrow Max10 DECA board: Part 1 https://e2e.ti.com/blogs_/b/process/archive/2015/10/12/interfacing-a-beaglebone-ble-wi-fi-cape-with-an-arrow-max10-deca-board-part-1

* Proyecto final de carrera - Desarrollo de una aplicación de detección de gestos y medida de distancias http://oa.upm.es/52363/

* Stepper Motor Design Example on MAX 10 DECA Board  https://fpgacloud.intel.com/devstore/platform/16.0.0/Standard/stepper-motor-design-example-on-max-10-deca-board/

* Quickly update a bitstream with new RAM contents https://github.com/tomverbeure/fpga_quick_ram_update

* Altera MAX10 DECA Board Fun Projects – Part 1 Graphics https://tingcao.wordpress.com/2015/09/22/deca-projects-part-1-graphics/  This design implements frame buffer based graphics on Altera MAX10 Arrow/Terasic DECA board in VIP (Video and Image Processing Suite).  [needs VIP license]

* Audio card with USB interface https://github.com/stsrc/audioCard

* Others (without source code):

  * Data I/O Sensor and LED Prototype https://ceias.nau.edu/capstone/projects/EE/2018/InternetFPGA/prototyping
  * Graphics Rendering on Altera MAX10 Arrow/Terasic DECA with VIP https://twitter.com/artchula/status/945177626431442944?s=20

  

### DECA peripherals related projects:

* Test for video output using the ADV7513 chip on a de10 nano board  https://github.com/nhasbun/de10nano_vgaHdmi_chip.  Includes programing and reference guide for ADV7513 chip.

* HDMI video (ADV7513) https://github.com/chriz2600/DreamcastHDMI/tree/develop/Core/source/adv7513

  

### Max10 Projects:

* maXimator - Altera MAX10 FPGA development board https://maximator-fpga.org/examples/ (maXimator)
* Consoles / Arcades
  * NES, C64, Vextrex, Arcades  http://darfpga.blogspot.com/  (VHDL code)  https://sourceforge.net/projects/darfpga/files/Software%20VHDL/ (DE10-Lite)  
  * HLS NES emulator https://github.com/kura197/NES-HLS (DE10-Lite (MAX10 10M50DAF484C7G))
  * DE10-Lite FPGA-based emulation of the Nintendo Gameboy https://github.com/sethsawant/de10boy (DE10-Lite)
  * Implemented a small CGA -> VGA scandoubler on the DE10-Lite https://twitter.com/_stderr/status/966592365321441280 (DE10-Lite)
* Zephyr OS + NIOS II https://docs.zephyrproject.org/latest/boards/nios2/altera_max10/doc/index.html (Altera Max 10)
* RISC-V https://github.com/syntacore/scr1-sdk (DE10-Lite)
* Pico RISCV32 for the DE10-Lite (MAX10 based) https://github.com/raps500/07_PicoRV32 (DE10-Lite)
* FPGA SDRAM controller https://github.com/Muellegr/FPGA-Max10-SDRAM-Project-1 (DE10-Lite)
* Flicker fixer for Amiga 500/2000 https://github.com/niklasekstrom/flickerfixer DE10-Lite)
* Easy FPGA CPU with MAX1000 (NIOS II) https://hackaday.com/2018/10/05/easy-fpga-cpu-with-max1000/  (MAX1000)
* Run DOS with 8086 on FPGA based on the next186 https://github.com/hi631/FPGA_DOS   (MAX1000)
* CPU86, the Free VHDL CPU8088 IP core https://github.com/nsauzede/cpu86 (MAX1000)
* Persistence of vision hack https://hackaday.com/2018/08/31/max1000-tutorial-is-quite-persistent/ (MAX1000)
* MAX1000 VHDPlus accelerometer Lab  https://www.youtube.com/watch?v=zSNgOrOqXTg (MAX1000)
* The FPGA FM Stereo Radio project for the CQ MAX10-FB https://github.com/Rapidnack/MAX10FB_FM_Stereo   ( CQ MAX10-FB )
* The FPGASID-Project aims to rebuild the famous Synthesizer chip MOS6581 know from Commodore 8-bit computers.  http://www.fpgasid.de/project-definition  (Altera MAX10 FPGA)
* X-Ray Vision for FPGAs: Using Verifla https://hackaday.com/2018/11/09/x-ray-vision-for-fpgas-using-verifla/  (MAX10)
* FM-transmitter project https://github.com/natanvotre/fm-transmitter/tree/master/src (Terasic Max10 plus)



### Other MAX10 boards:

* Terasic DE10-Lite https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&CategoryNo=218&No=1021 (MAX10M50 , 64MB SDRAM, 444 VGA)
* MAX1000 https://www.arrow.com/en/products/max1000/arrow-development-tools (10M08, 8 MB SDRAM)
  * Arrow's Max-1000: A gem for all the wrong reasons https://zipcpu.com/blog/2017/12/16/max1k.html
* maXimator https://maximator-fpga.org
* CQ MAX10-FB (Japanesse board)
* MAX® 10 FPGA 10M50 Evaluation Kit https://www.intel.com/content/www/us/en/programmable/products/boards_and_kits/dev-kits/altera/kit-max-10m50-evaluation.html
* Intel® MAX® 10 FPGA Development Kit https://www.intel.com/content/www/us/en/programmable/products/boards_and_kits/dev-kits/altera/max-10-fpga-development-kit.html
* Intel MAX® 10 - 10M08 Evaluation Kit https://www.intel.com/content/www/us/en/programmable/products/boards_and_kits/dev-kits/altera/kit-max-10-evaluation.html



### Beaglebone Black Capes:

* BLE WIFI CAPE (Compatible with DECA board). Product page is broken. Go to www.arrow.com, search "ble wifi cape" and in the search results click buy. 
* MikroBUS Cape Extension Board for Beaglebone Black , MIKROE-1857 by MikroElektronika, https://www.arrow.com/en/products/mikroe-1857/mikroelektronika
  * Click modules https://www.mikroe.com/click

* Wireless Connectivity Cape for BeagleBone Black https://www.element14.com/community/docs/DOC-79264/l/wireless-connectivity-cape-for-beaglebone-black

  