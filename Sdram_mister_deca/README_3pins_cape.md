## SDRAM 3 pins Mister module testings with DECA

### Objectives and considerations

* Test convenience of using separate pins for CKE/DQML/DQMH instead of Mister modules using shared pins

### Modules tested with memtest (Duponts hack)

Tested with memtest_deca_3pins_211020.sof:

* "A2" dual memory: Result: 140 MHz 

* "O1" dual memory:  Result: 120 MHz 
* "O3" dual memory (tested by Rhoderik): Result: 120 MHz 
* XS v2.2 Mister module 32 MB (winbond): Result: 160 MHz 
* XS-D v2.5 Mister module 128 MB (alliance): Result 120 MHz



### Modules tested with memtest (CAPE)

Tested with memtest_deca_220409.sof:

* "A2" dual memory: Result: 120 MHz 
* "O1" dual memory:  Result: 140 MHz 
* "O3" dual memory (tested by Rhoderik): Result:  MHz 
* XS v2.2 Mister module 32 MB (winbond): Result: 160 MHz 
* XS-D v2.5 Mister module 128 MB (alliance): Result  MHz



