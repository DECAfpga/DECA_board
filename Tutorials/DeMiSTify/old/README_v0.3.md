## Some notes about DeMiSTifyng a MiST core

[DeMiSTify](https://github.com/robinsonb5/DeMiSTify)  is support code intended to assist in the porting of MiST FPGA cores to other target boards (Copyright (c) 2021 by Alastair M. Robinson).

Follows a brief guide on how to use it. 

Notes:

* In notes below "AMR" indicates comments from Alastair M. Robinson.

* Where you see "deca" substitute it for the board you are porting to. 

* Where you see a specific core (e.g. NES, gameboy, ....) substitute it for the core you are porting.


### Controls

* F12 show/hide OSD 
* The reset button resets the controller (so re-initialises the SD card if it's been changed, reloads any autoboot ROM.) The OSD Reset menu item resets the core itself.

### Fork a Mist core and add DeMiSTify as a submodule

* Fork a MiST core to your GitHub account from the web interface (In this example we are forking gameboy core https://github.com/mist-devel/gameboy into https://github.com/DECAfpga/gameboy )

* Clone forked project:

  ```sh
  #https 
  git clone https://github.com/DECAfpga/gameboy
  #or SSH
  git clone git@github.com:DECAfpga/gameboy
  # go to gameboy folder which will be referred as the root folder
  cd gameboy
  
  ```

* Add DeMiSTify as a submodule:

  ```sh
  #submodules urls always is best to use the https version
  git submodule add https://github.com/DECAfpga/DeMiSTify.git
  git submodule update --init 
  
  #[recommended checkout to somhic branch for latest Deca features]
  cd DeMiSTify
  git checkout somhic
  cd ..
  ```

* Copy in the root folder the content of DeMiSTify/templates/deca-template.  You would need to check and adapt template content from DeMiSTify/templates/  for use in other boards:

  ```sh
  cp -r DeMiSTify/templates/deca-template/* .
  #delete sys folder if you are not on a Sorgelig core
  #slingshot cores usually have mist_modules defined as submodules 
  rm -r sys/
  ```
  
  NOTE: Most up to date templates are at DeMiSTify/templates main folder. It's worth keeping up to date with config.h (and demistify_config_pkg if your board toplevels are in VHDL) but don't worry too much about the other files (most of those changes are about tidiness rather than functionality).

### Root project folder

Modify / create the following files and folders:

* Makefile: Edit Makefile and change the name of the PROJECT. The rest should be fine.

* mistcore.qip: Edit and fill it in with the original Mist project files found in .qsf file

  * Respect the following format [file join $::quartus(qip_path) xxxxxxx] for all the project files:

    ```verilog
    set_global_assignment -name VERILOG_FILE [file join $::quartus(qip_path) src/dsp.v]
    ```

  * Comment out the pll file, as you will include your board specific pll later into top.qip file at board folder.

  * You might need to comment out the original Mist sdram controller file. If you need your own memory controller include it later in top.qip file at deca folder.

  * Leave the original constraint file, but it would require to be edited as commented below.

* project_files.rtl is a bit like a .qip file but not quartus-specific. 

  * remove included .qip files in template for your own ones (usually just a mistcore.qip file in the root folder)
  * If pre-flow scripts like build_id.tcl is not used in core remove it

    * AMR: It isn't needed for the some cores.  If it's needed, there'll be a TCL script with the MiST core which generates the build_id.v file, so we just add that script so it gets run at the appropriate time. Most of them generate a version string which is included in the config string.  

* project_defs.tcl  edit and check parameters project, requires_sdram, optimizeforspeed

  * comment out 'set optimizeforspeed 1'  to avoid  OPTIMIZATION_MODE "AGGRESSIVE PERFORMANCE" which takes long time to generate output bitstream.

* demistify_config_pkg.vhd  file usually does not need to be modified. This file is included in project_files.rtl 

  * It contains COMPONENT guest_mist.  AMR: The idea is that you can share the component between boards, instead of having to declare it for each and every board.  I'm generally porting to TC64v1, TC64v2 and DE10Lite, and I got bored with having to adjust the component three times, and keep them all in sync.

* firmware

  * config.h (from DeMiSTify/templates/config.h): edit and change definitions accordingly to your core:
    * set to #undef if your core does not use those options
    * If you have the menu working on F12, but no joystick emulation, then make sure you have both CONFIG_JOYKEYS and CONFIG_EXTJOYSTICK defined.
    *  There's a define in firmware/config.h which chooses whether or not a ROM is required (#undef ROM_REQUIRED)
    * AMR: If you edit config.h  you'll need to do a "make firmware_clean" followed by "make firmware". In the near future I'll push some changes to DeMiSTify to make the firmware get rebuilt when you modify config.h
    
  * Create inside a file named "overrides.c". 
  
    * Edit file and add the following if the core needs to boot a ROM during bootup:
    
    ```c
    // Initial ROM 
    const char *bootrom_name="AUTOBOOTNES";
    //Note the filename must be in 8/3 format with no dot and capital letters. If the name have less than 8 letters then leave spaces so total characters must be 11, e.g.
    const char *bootrom_name="SVI328  ROM";
    ```
    
    NOTE 1: Now this is not needed as the ROM name can be set in config.h, but the override method does still work.
    
    NOTE 2: If the core needs a  BIOS loaded from SD card, the BIOS is loaded as a ROM (with romtype=0) - and then the autobooted ROM, if any, is loaded with romtype 1.  (The romtype is mapped to the ioctl_index variable in the core.) (see gameboy core as example)
    
    * If the core needs to load a VHD drive during bootup checkout the following code ([overrides.c](overrides.c)).
    
      

### Board folder (deca folder)

Modify and/or create the following files:

* Board specific required files are now included and defined in Board/deca/deca_support.tcl

* PLL: In board folder you will need to add the pll files from the original Mist core but adapting the clock source from 27 MHz to 50 MHz (and optionally adapting it to the Altera family).

  * AMR: What I usually do is open the MiST project, and have a look at the PLL, then create a new one for the target board, with the same output frequencies, but the appropriate input frequency.  
  * AMR: the Clock27 input on the MiST core that we're wrapping - it's not 27MHz, it's whatever clock the board provides.  It'd just be too much of a pain to rename it.

* Memory controllers: add specific memory controllers for your board if needed

* top.qip: Create a new file named "top.qip" and include board project specific files like deca_top.vhd,  PLLs and specific memory controllers. 

  * Respect the following format [file join $::quartus(qip_path) xxxxxxx] for all the project files:

    ```verilog
    set_global_assignment -name VERILOG_FILE [file join $::quartus(qip_path) sdram.v]
    ```

  * AMR: I normally have a root qip file which has all the project files and the project constraints file.  Then in each board directory I have top.qip which references the toplevel file for that board, and also any PLLs needed for the project - and if there's anything else needed, like some defines, they can be added too.

* ~~.hex files:  if the Mist project include .hex files, copy them to board folder as it's the place where they can be found~~  

* deca_top.vhd is a wrapper for the original Mist core.  

  * Edit it and change the guest module name.
  
  * If the audio's super-loud and scratchy then you probably have a problem with signed vs unsigned.  If it's unsigned and your DAC needs signed audio you'll need to invert the most significant bit.
  
  * AMR: deca_top.vhd will probably be nearly identical to the one for the Mist core - it just has to deal with the name of the Mist core changing from core to core, and other subtleties like whether or not Clock27 is defined with one input or two (annoyingly that varies from core to core!).
  
  * If you need to extract 16 bit audio from the MiST core to feed an I2S transmitter it's a good idea to make use of this Verilog macro defined in DeMiSTify/Boards/deca/board_support.tcl
  
    ```tcl
    set_global_assignment -name VERILOG_MACRO  "DEMISTIFY_PARALLEL_AUDIO=1"
    ```
  
    Definitions in top mist core. The idea is to add the extra signals without breaking the core on MiST:
  
    ```tcl
    `ifdef DEMISTIFY_PARALLEL_AUDIO
    `else
    `endif
    ```
  
    AMR: Remember that on MiST that top file is the actual toplevel, so its signals are all physical pins on the FPGA.  If they're not defined, Quartus will attempt to allocate unused pins to them, and fail because there aren't 32 spare pins.
  
  * Generic map for substitute_mcu entity: SPI_FASTBIT 
  
    AMR: If the control module is driving SPI too fast for the guest core it will cause problems.  (e.g. the NES core uses a sysclk of just 21MHz for the data-IO module.)  In the generic map for substitute_mcu in your deca_top, add this:   `SPI_FASTBIT=>3,`  
    It defaults to 2, so changing it to 3 halves the speed of the fast-mode SPI comms.

### Changes in Mist core

From the original Mist core it may be needed to adapt just a few things:

* Mist top file
  * To supply audio samples for I2S sound you would need to get out the DAC inputs from Mist top to the board top. 
  * For HDMI output you will have to output also blank signal/s and vga clock
  * If you change memory controller then you would also need to adapt the Mist top controller instantiation
* Constraints file: copy the MiST constraints file to the root folder and remove the generic Mist board references that are replaced in the boards target specific constraint file (e.g. DeMiSTify/Board/deca/constraints.sdc)

  See below "Notes about Constraint files".

### Others

* If needed to adapt anything, adjustments to board definition can be found inside the DeMiSTify/Board/xxxx folder
  * constraints.sdc: non timing-critical  pins would be in the "FALSE_IN/OUT" collections
    * AMR: Provided the source core is well constrained, it's not too bad, because you can use the MiST constraints file as a template.  Again, it's about replacing MiST-specific stuff with generic stuff defined by DeMiSTify. 
  * deca_pins.tcl: PIN names can be whatever's appropriate for the board.  The job of the board-specific toplevel file is to wire up the board signals to the guest core's signals.
  * deca_support.tcl: include specific board HDL files here (hmdi, audio, ...).
  * deca_opts.tcl: include specific board global assignments here.
* Quartus log: execute `tail -f compile.log` in ther deca folder
* If you cloned the repo instead of forking it, you can use the github web interface to create your own fork of the MiST repo and then you can edit .git/config in your local clone so that origin points to your fork instead of mist-devel.  Then you can push to you fork.

### Compile the project

```sh
#Do a first make (will finish in error). It will download missing submodules 
make
#when asked just accept default settings with Enter key
#Create file site.mk in DeMiSTify folder 
cd DeMiSTify
cp site.template site.mk
#Edit site.mk and modify with your PATHs to Quartus and the BOARDS you are porting to
#(chameleon64 chameleon64v2 de10lite deca neptuno sidi uareloaded mist ...)
#(e.g. Q19 = /home/jordi/bin/intelFPGA_lite/17.1/quartus/bin)
gedit site.mk
#[optionally checkout to somhic or other branch if you did it in the first part]
git checkout somhic
#Go back to root folder and do a make with board target (deca, neptuno, uareloaded, ...).  If not specified it will compile for all targets. 
cd ..
make BOARD=deca
#make BOARDS=deca\ neptuno
```

* `make` will do `make init`, followed by `make compile` for all boards defined in the makefile.

* makefile recognizes commands "init" "compile" "firmware" and "firmware_clean". If you don't supply a command it does everything.

* `make BOARD=deca` will create the project files and then compile them.  

* `make BOARD=deca init` It just created the project so you can open it in Quartus and compile there

* When you do `make BOARD=deca` the scripts will generate a new quartus project file in deca/ pulling together the files in project_files.rtl, the stuff in DeMistify/Boards/deca and the deca/top.qip file. When if finishes you will have the ported core inside the deca folder. Generated bitstream will be at deca/output_files.

  

### Flash bitstream to FGPA

Update with your own PATHs to Quartus and sof filename:

```sh
cd deca/output_files/
export PATH="/home/jordi/bin/intelFPGA_lite/17.1/quartus/bin:$PATH"
quartus_pgm --mode=jtag -o "p;gameboy_deca.sof"

```



### Troubleshooting

* If you make changes to firmware and do a make it will not work. You need to do a `make firmware_clean`  or just delete everything in root/firmware folder except for "config.h" and "overrides.c" files.
* If you make changes to demistify board options/pins/... and it does not work compilation, then just delete the board qsf file.




### Notes about Constraint files

* AMR: It's ok to have two constraint files in the core, one project specific and one board specific
  * The board-specific one does things like "set RAM_OUT {DRAM_DQ* DRAM_ADDR* DRAM_BA* DRAM_RAS_N DRAM_CAS_N DRAM_WEN DRAM*DQM DRAM_CS_N DRAM_CKE}".  The SPI clock is defined in the board constraints too.
  * The project one does things like "set_output_delay -clock [get_clocks $sdram_clk] -reference_pin [get_ports ${RAM_CLK}] -max 1.5 [get_ports ${RAM_OUT}]"
  * It avoids having to write the whole constraints file for every board, every time you port a core.
  * What's nice is that variables defined in one .sdc file are visible from within subsequent .sdc files.
  
* The board constraints file will need adapting.  Each board has its own constraints files which define things like the pin names for the RAM, which pins can be treated as false paths, etc.  That way a single project constraints file can be shared between targets.

* The original Mist constraints file will need adapting.  Usually it's just a case of removing the MiST names for signals and replacing them with the variables defined in the board-specific constraints files.

* set topmodule guest| 

  * AMR: I use it in project-specific constraints files.  For instance, on NES I do this:

    ```
    set mem_clk   "${topmodule}clock_21mhz|altpll_component|auto_generated|pll1|clk[0]"
    ```

    Then I can use the same constraints file with MiST, just by having a MiST-specific constraints file set topmodule guest| on DeMiSTified platforms, and set topmodule "" on MiST

    The path to the PLL is then evaluated as guest|clock_21mhz|altpll_component.... on DeMiSTified platforms, and clock_21mhz|altpll_component.... on MiST, using the same constraints file.

    Basically, I'm exploiting a neat trick I discovered: if you define a variable in a constraints file, it's visible from subsequent constraints files.  So I use a board-specific constraints files to set a bunch of variables for each board, which allows me to use one single constraints file for the project, rather than tediously adapting it for every board individually.

    



### Other material

* Porting the VIC20 core https://retroramblings.net/?p=1752



