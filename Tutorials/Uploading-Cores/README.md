## Uploading cores from shell command line



## Flash bitstream to FGPA with Quartus

Update with your own PATHs to Quartus and sof filename:

```sh
cd path/to/output_files/
export PATH="/home/jordi/bin/intelFPGA_lite/17.1/quartus/bin:$PATH"
quartus_pgm --mode=jtag -o "p;gameboy_deca.sof"

```



## Flash bitstream to FGPA with OpenOCD

* Install [OpenOCD](https://github.com/arduino/OpenOCD) 

  * Full installation (works in any Linux system)

    ```
    apt-get install openocd
    ```

  * Minimal installation for an ARM SBC like a Raspberry Pi (see compilation flags in notes below)

    * Install [openocd_0.11.0-1_armhf.deb](openocd_0.11.0-1_armhf.deb).

    ```
    sudo dpkg -i openocd_0.11.0-1_armhf.deb
    
    ```

* Copy files [altera-usb-blaster2.cfg](altera-usb-blaster2.cfg) and [blaster_6810.hex](blaster_6810.hex) at some place. 

* Edit altera-usb-blaster2.cfg and update /path/to/quartus/blaster_6810.hex

* Execute script as follows updating /path/to/file.svf

```sh
#Update script to your own path/to/altera-usb-blaster2.cfg 
openocd \
-f /home/jordi/Documents/Arduino-DIY/FPGAs/OpenOCD/altera-usb-blaster2.cfg \
-d0 \
-c init \
-c "svf -quiet /path/to/file.svf" \
-c shutdown

```

### Notes:

* How to generate the SVF files
  * Set project to generate SVF files after each compilation:
    * Open Device, Device and Pin Options..., Programming files and check .svf 
  * [How do I generate a Serial Vector File (SVF) in Quartus](https://www.intel.com/content/www/us/en/support/programmable/articles/000085709.html)

* Compilation flags for OpenOCD minimal installation

```sh
apt install libftdi-dev
./bootstrap
./configure  --prefix=/usr --enable-dummy --enable-ftdi --enable-usb-blaster-2 --enable-usb-blaster --enable-bcm2835gpio --enable-ft232r \
--disable-malloc-logging --disable-rshim --disable-stlink --disable-ti-icdi --disable-ulink --disable-doxygen-html \
--disable-vsllink --disable-xds110 --disable-cmsis-dap-v2 --disable-osbdm --disable-opendous --disable-armjtagew \
--disable-rlink --disable-usbprog --disable-aice --disable-cmsis-dap --disable-nulink --disable-kitprog \
--disable-presto --disable-openjtag --disable-buspirate --disable-jlink --disable-parport --disable-parport-ppdev \
--disable-parport-giveio --disable-jtag_vpi --disable-jtag_dpi --disable-amtjtagaccel --disable-imx_gpio --disable-ep93xx \
--disable-at91rm9200 --disable-gw16012 --disable-sysfsgpio --disable-xlnx-pcie-xvc --disable-remote-bitbang \
--enable-internal-jimtcl --enable-internal-libjaylink
```

