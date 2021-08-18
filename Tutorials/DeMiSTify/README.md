## Some notes about DeMiSTifyng a MiST core

[DeMiSTify](https://github.com/robinsonb5/DeMiSTify)  is support code intended to assist in the porting of MiST FPGA cores to other target boards (Copyright (c) 2021 by Alastair M. Robinson)

Follows a brief guide on how to use it:

* Download a new Mist core to be ported to DECA or any other board supported (in the following lines where you see deca replace it with your own board name)
* Get another DeMiSTifyed core and copy the following objects  (** see note below)

![core](core.png)

**Note: to get the latest version of DeMiSTify don't copy the DeMiSTify folder but add the following into the .gitmodules file

```sh
[submodule "DeMiSTify"]
	path = DeMiSTify
	url = git@github.com:DECAfpga/DeMiSTify.git
#url will soon be changed to main DeMiSTify Alastair Repository when it's merged
```

* Change file name of Oric.qip to deca.qip and fill in with the original core files from Mist project (qsf) respecting the format of Oric.qip.  Don't include the pll file, as it will be included in the deca project.

* In deca folder just leave the following files:

  ![deca](deca.png)

* Replace pll.xxx with the Mist core pll, changing clock source from 27 MHz to 50 MHz and adapting it to the Altera family.

* deca_top.vhd is a wrapper for the original Mist core.  

  * Edit it and change the guest module name.

* If needed to adapt anything, adjustments to board definition can be found inside the DeMiSTify/Board/xxxx folder

* From the original Mist core it may be needed to adapt just few things, e.g.:
  * To supply audio samples for I2S sound you would need to get out the DAC inputs from Mist top to the deca top.

* Compile the project:

```sh
#in the root folder of project (where you copied the makefile)
make
#submodules will be downloaded, including DeMiSTify if you added it in the .gitmodules
cd DeMiSTify
#following is not going to be needed when dev branch is merged with main 
git checkout dev
#edit file site.mk and add your own PATHs to Quartus
gedit site.mk
#go back to root folder and do a make with board target (deca, sidi, neptuno, ...)
cd ..
make BOARD=deca
```

* When if finishes you will have the ported core inside the deca folder including the bitstream in output_files folder



## Troubleshooting

* Problems loading initial ROM file:    You may have to override a function in firmware/overrides.c to make sure the io index is correct, adding the line    `const char *bootrom_name="SVI328  ROM";`  to firmware/overrides.c  ( note the filename must be in 8/3 format with no dot).