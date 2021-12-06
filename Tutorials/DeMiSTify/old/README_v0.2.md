## Some notes about DeMiSTifyng a MiST core

[DeMiSTify](https://github.com/robinsonb5/DeMiSTify)  is support code intended to assist in the porting of MiST FPGA cores to other target boards (Copyright (c) 2021 by Alastair M. Robinson).

Follows a brief guide on how to use it. In notes below "AMR" indicates comments from Alastair M. Robinson.

This guide is for main branch. For somhic branch follow this [readme.md.](README_somhic.md)

### Download DeMiSTify template and Mist core

* Clone DeMiSTify template from https://github.com/DECAfpga/DeMiSTify-template

```
git clone https://github.com/DECAfpga/DeMiSTify-template
```

* Download the target Mist core to be ported to DECA or any other board supported 
  * In the following tutorial where you see "deca" replace it with your own board name. 
  
* Copy Mist core files into the DeMiSTify template folder. 
  * overwrite README.md, but not .gitmodules or .gitignore
  
* You can safely delete board folders which you are not porting to.

* Template already includes /sys folder for Sorgelig cores. If you don't use it you can safely remove it. In case the core is using mist_modules from  Slingshot you need to add original core missing submodules.

* Add original core missing submodules (check .gitmodules file from Mist repo):

  ```sh
  #e.g. required submodules for Mist NES core
  cd DeMiSTify-template
  cd mist
  rm -r mist-modules
  git submodule add https://github.com/mist-devel/mist-modules.git
  cd ..
  cd src
  rm -r T65
  git submodule add https://github.com/mist-devel/T65.git
  cd ..
  git submodule update --init
  ```

### Root project folder

Modify / create the following files and folders:

* Makefile: Edit Makefile and change the name of the PROJECT and the BOARDs you want to port. The rest should be fine.

* xxx.qip: Create a file named corename.qip (e.g. nes.qip) and fill it in with the original Mist project files found in .qsf file

  * Respect the following format [file join $::quartus(qip_path) xxxxxxx] for all the project files:

    ```verilog
    set_global_assignment -name VERILOG_FILE [file join $::quartus(qip_path) src/dsp.v]
    ```

  * Comment out the pll file, as you will include your board specific pll into top.qip file at deca folder.

  * You might need to comment out the original Mist sdram controller file. If you need your own memory controller include it later in top.qip file at deca folder.

  * Leave the original constraint file, but it would require to be edited as commented below.

* project_files.rtl is a bit like a .qip file but not quartus-specific. 

  * remove included .qip files in template for your own ones (usually just a corename.qip file in the root folder (e.g. nes.qip))
  * If pre-flow scripts build_id.tcl is not used in core remove it
    * AMR: It isn't needed for the some cores.  If it's needed, there'll be a TCL script with the MiST core which generates the build_id.v file, so we just add that script so it gets run at the appropriate time. Most of them generate a version string which is included in the config string.  

* project_defs.tcl  edit and check parameters project, requires_sdram, optimizeforspeed

  * optimizeforspeed 1 Remove this line to avoid  OPTIMIZATION_MODE "AGGRESSIVE PERFORMANCE" which takes long time to generate output bitstream.

* demistify_config_pkg.vhd  file usually does not need to be modified. This file is included in project_files.rtl 

* firmware: Create a folder named "firmware" 

  * Copy here the file /DeMiSTify/templates/config.h and change definitions accordingly
    * set to #undef if your core does not use those options
  * Create inside a file named "overrides.c". Edit file and add the following if the core needs to boot a ROM during bootup:

```
/* Initial ROM for NES core*/
const char *bootrom_name="AUTOBOOTNES";
```

### Deca folder

Modify / create the following files:

* Board specific files: audio folder and LOOP.hex are deca specific board files to deal with I2S audio output. These files are defined in Board/deca/deca_support.tcl

* PLL: In deca folder you will need to add the pll files from the original Mist core but adapting the clock source from 27 MHz to 50 MHz (and optionally adapting it to the Altera family).

  * AMR: What I usually do is open the MiST project, and have a look at the PLL, then create a new one for the target board, with the same output frequencies, but the appropriate input frequency.  
  * AMR: the Clock27 input on the MiST core that we're wrapping - it's not 27MHz, it's whatever clock the board provides.  It'd just be too much of a pain to rename it.

* Memory controllers: add specific memory controllers for your board

* top.qip: Create a new file named "top.qip" and include board project specific files like deca_top.vhd,  PLLs and specific memory controllers. 

  * Respect the following format [file join $::quartus(qip_path) xxxxxxx] for all the project files:

    ```verilog
    set_global_assignment -name VERILOG_FILE [file join $::quartus(qip_path) sdram.v]
    ```

  * AMR: I normally have a root .qip which has all the project files and the project constraints file.  Then in each board directory I have top.qip which references the toplevel file for that board, and also any PLLs needed for the project - and if there's anything else needed, like some defines, they can be added too.

* .hex files:  if the Mist project include .hex files, copy them to board folder as it's the place where they can be found

* deca_top.vhd is a wrapper for the original Mist core.  

  * Edit it and change the guest module name.
  * If the audio's super-loud and scratchy then you probably have a problem with signed vs. unsigned.  If it's unsigned and your DAC needs signed audio you'll need to invert the most significant bit.
  * AMR: deca_top.vhd will probably be nearly identical to the one for the Mist core - it just has to deal with the name of the Mist core changing from core to core, and other subtleties like whether or not Clock27 is defined with one input or two (annoyingly that varies from core to core!).


### Changes in Mist core

From the original Mist core it may be needed to adapt just a few things:

* To supply audio samples for I2S sound you would need to get out the DAC inputs from Mist top to the deca top. 
* If you change memory controller then you would also need to adapt the Mist top controller instantiation
* Constraints file: remove the generic Mist board references that are replaced in the boards target specific constraint file (e.g. DeMiSTify/Board/deca/constraints.sdc)
  * AMR: It'll need adapting - usually it's just a case of removing the MiST names for signals and replacing them with the variables defined in the board-specific constraints files.

### Others

* If needed to adapt anything, adjustments to board definition can be found inside the DeMiSTify/Board/xxxx folder
  * deca_pins.tcl: PIN names can be whatever's appropriate for the board.  The job of the board-specific toplevel file is to wire up the board signals to the guest core's signals.
  * constraints.sdc: non timing-critical  pins would be in the "FALSE_IN" collection
    * AMR: Provided the source core is well constrained, it's not too bad, because you can use the MiST constraints file as a template.  Again, it's about replacing MiST-specific stuff with generic stuff defined by DeMiSTify. 
* Quartus log: execute `tail -f compile.log` in ther deca folder

### Compile the project

```sh
#Do a first make (will finish in error). It will download missing submodules 
make
#when asked just accept default settings with Enter key
#edit file site.mk and add your own PATHs to Quartus (e.g. /home/jordi/bin/intelFPGA_lite/17.1/quartus/bin)
cd DeMiSTify
cp site.template site.mk
gedit site.mk
#go back to root folder and do a make with board target (deca, sidi, neptuno, ...)
cd ..
make
```

* "make" will do make init, followed by make compile for all boards defined in the makefile.
* makefile recognizes commands "init" "compile" "firmware" and "firmware_clean". If you don't supply a command it does everything.
* "make BOARDS=deca" will create the project files and then compile them.  If you want to just create the project so you can open it in Quartus, then use make BOARDS=deca init
* When you do "make BOARDS=deca" the scripts will generate a new quartus project file in deca/ pulling together the files in project_files.rtl, the stuff in DeMistify/Boards/deca and the deca/top.qip file. When if finishes you will have the ported core inside the deca folder. Generated bitstream will be at deca/output_files.



### Flash bitstream to FGPA

Update with your own PATHs to Quartus and bitstream .sof filename:

```sh
cd deca/output_files/
export PATH="/home/jordi/bin/intelFPGA_lite/17.1/quartus/bin:$PATH"
quartus_pgm --mode=jtag -o "p;NES_deca.sof"
```



### Troubleshooting

* Problems loading initial ROM file:    You may have to override a function in firmware/overrides.c to make sure the io index is correct, adding the line    `const char *bootrom_name="SVI328  ROM";`  to firmware/overrides.c  ( note the filename must be in 8/3 format with no dot).



### Notes about Constraint files

* It's ok to have two constraint files in the core, one project specific and one board specific
  * AMR: the board-specific one does things like "set RAM_OUT {DRAM_DQ* DRAM_ADDR* DRAM_BA* DRAM_RAS_N DRAM_CAS_N DRAM_WEN DRAM*DQM DRAM_CS_N DRAM_CKE}".  The SPI clock is defined in the board constraints too.
  * AMR: the project one does things like "set_output_delay -clock [get_clocks $sdram_clk] -reference_pin [get_ports ${RAM_CLK}] -max 1.5 [get_ports ${RAM_OUT}]"
  * AMR: It avoids having to write the whole constraints file for every board, every time you port a core.
  * AMR: What's nice is that variables defined in one .sdc file are visible from within subsequent .sdc files.
* The constraints file will need adapting.  Each board has its own constraints files which define things like the pin names for the RAM, which pins can be treated as false paths, etc.  That way a single project constraints file can be shared between targets.

* set topmodule guest| 
  * AMR: I use it in project-specific constraints files.  For instance, on NES I do this:

    ```
    set mem_clk   "${topmodule}clock_21mhz|altpll_component|auto_generated|pll1|clk[0]"
    ```

    Then I can use the same constraints file with MiST, just by having a MiST-specific constraints file set topmodule to ""

    The path to the PLL is then evaluated as guest|clock_21mhz|altpll_component.... on DeMiSTified platforms, and clock_21mhz|altpll_component.... on MiST, using the same constraints file.

    Basically, I'm exploiting a neat trick I discovered: if you define a variable in a constraints file, it's visible from subsequent constraints files.  So I use a board-specific constraints files to set a bunch of variables for each board, which allows me to use one single constraints file for the project, rather than tediously adapting it for every board individually.

