# Firmware files for Makerdiary M60 Keyboard

File | Description
:- | :-
circuitpython-6.0.0-alpha.1-m60-20200827.uf2 | Makerdiary's official release
circuitpython-6.0.0-alpha.1-m60-20210117.uf2 | Makerdiary's official release
circuitpython-7.3.1-9-gbad4446a7-m60-20220702.uf2 | Experimental firmware built by hyx0329
patches-7.x | Related patches to the firmware by hyx0329

## Notes on firmware by hyx0329

pros:

+ compatible with original Keyboard module and code
+ newer circuitpython
+ preserves manual safe mode
+ patch set available

crons:

- do not have "double tap user button to enter bootloader" feature
- storage reset will not give you a default usable keyboard
  code must be written before using the keyboard
- do not have a development repository

