# DECA board target for Litex

[deca_litex_target.py](deca_litex_target.py)  is part of [LiteX-Boards](https://github.com/litex-hub/litex-boards) and was made by [Hans Baier](https://github.com/hansfbaier).

It includes the DECA board pin locations for MiSTer SDRAM ([via GPIO expansion board on P8](https://github.com/DECAfpga/DECA_board/tree/main/Sdram_mister_deca)).



[LiteX installation guide](https://github.com/enjoy-digital/litex/wiki/Installation)



Go to the litex boards targets folder and export paths to Quartus:

```sh
cd /home/jordi/bin/litex-boards/litex_boards/targets

export PATH="/home/jordi/bin/intelFPGA_lite/17.1/quartus/bin:$PATH"

#only if RiscV code needs to be compiled
export PATH=$PATH:/home/jordi/bin/riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-linux-ubuntu14/bin/
```



Example testing MiSTer SDRAM with [Litex](https://github.com/enjoy-digital/litex) memory test. 

```sh
# Download specific Deca target from 
# https://github.com/SoCFPGA-learning/DECA/blob/main/deca-litex-target.py 
# into the folder litex-boards/litex_boards/targets and make it executable. 
# Thanks to Hans Baier for it.
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



**Other examples usign the stock terasic_deca.py target:**

```sh
#Serial over USB-Blaster

./terasic_deca.py --uart-name=serial --build   --load
#build generat a /home/jordi/bin/litex-boards/litex_boards/targets/build/deca

./terasic_deca.py --load

#Alternativament programar manualment

# cd ~/bin/litex-boards/litex_boards/targets/build/deca/gateware

# ./build_deca.sh

# quartus_pgm -m jtag -o "p;deca.sof"

nios2-terminal 
```



```sh
#GPIO Serial
#Subsignal("tx", Pins("P8:3")),-> pin 03 (White C96 cable) GPIO0_D0
#Subsignal("rx", Pins("P8:4")),-> pin 04 (Green C96 cable) GPIO0_D1

#                       ground -> pin 1 / 2 (Black)  

./terasic_deca.py --uart-name=gpio_serial --build --load

#terminal
lxterm --serial-boot  /dev/ttyUSB0
picocom -b 115200 /dev/ttyUSB0
```





```sh
#adding RAM for avoiding upload fails (CRC errors)
./terasic_deca.py --uart-name=gpio_serial --integrated-main-ram-size 0x4000 --build --load

#terminal
picocom -b 115200 /dev/ttyUSB0
```





```sh
#to load an app
litex_bare_metal_demo --build-path=build/terasic_deca
litex_term --serial-boot --kernel demo.bin /dev/ttyUSB0
[enter]
litex>serialboot
```

