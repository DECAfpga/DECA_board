## SDRAM Mister module adapter for DECA

For memory testings and 3 pins old mister modules pictures see [this readme.](README_3pins.md)

### Objectives and considerations

* Build an adapter to plug a 40 pin Mister SDRAM on DECA board
* Memory tested is SDRAM board for MiSTer (extra slim) XS_2.2
* Test memory is working


### Resources of information

* SDRAM XS v2.2 Altium schematics from Sorgelig
* DECA schematics
* De10-nano schematics

### Schematic

See full schematic [sdram_xs-SchDoc.pdf](sdram_xs-SchDoc.pdf) 

See Kicad folder.

![image-20210420203647994](img/schematic.png)



### Assembly instructions 

* Buy an stackable male male header like the ones sold in this [pack](https://www.arrow.com/en/products/205-0001-02/schmartboard).

* Push a little bit down and bend pins in the stackable header that correspond to pins 12, 29, 30 from the SDRAM module (pins 18, 35, 36 from the Deca P8 header). Otherways you can remove those pins an insert larger ones.
* Plug SDRAM module into the stackable header and this into the P8 DECA connector.
* Connect jumper wires at those bended pins in 12, 29 & 30 according to schematic. It is important to connect at least one of the ground pins (I suggest pin 12) from SDRAM module to GND in P8 pins 1 or 2, but better if you connect both ground pins.   Pin 29 (3V3) and pin 30 (GND) from SDRAM can be connected to P9 connector pins 3 (3V3) and 1 (GND).

See below pictures which are self explanatory:

![header](img1/stackable-headers.jpg)

![outward](img1/outward.png)

![total](img1/total.png)



### Memory test

I tested the memory with [Litex](https://github.com/enjoy-digital/litex) memory test. 

```sh
# Download specific Deca target from https://github.com/SoCFPGA-learning/DECA/blob/main/deca-litex-target.py 
#into the folder litex-boards/litex_boards/targets and make it executable. 
#Thanks to Hans Baier for it.
wget https://github.com/DECAfpga/DECA_board/blob/main/Litex/deca_litex_target.py
chmod +x deca-litex-target.py
#Compile and load Litex for DECA board with Mister SDRAM option 
./deca-litex-target.py --uart-name=gpio_serial --mister-sdram-xs-v22 --build --load
#Serial pins ("tx", "P8:3"), ("rx", "P8:4"),  (ground pin 1/2) 
#terminal output
picocom -b 115200 /dev/ttyUSB0
reboot
mem_test 0x40000000 0x2000000
mem_speed 0x40000000 0x2000000
```



![image-20210420212040405](img/litex.png)