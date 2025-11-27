# Onyx2040
This is a devboard powered by the RP2040 chip! It features 40 pins broken out (20 per side) for easy prototyping and a plus‑sign of 5 RGB LEDs to animate whatever your heart desires.

I built this project as a way to learn full PCB design, from schematics to routing to firmware. It’s also a great way for others to prototype their own ideas, with colorful lighting built in to make experimentation more fun and expressive.

## How to Use It?
1. **Power the board** with USB-C
2. To use MicroPython, hold the button (the board will appear as a USB drive named RPI-RP2) and **flash the MicroPython UF2 firmware** with the [MicroPython RP2040 Documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).
3. Once MicroPython is installed, **copy your Python files** to the board.
4. Then, **experiment!** Use the 40 broken‑out pins (GPIO, power, and ground) to connect sensors, modules, or breadboards. Check out the firmware in the /firmware folder in this repository for an example of how to control the on-board LEDs. Enjoy!


## Images
Here is the **schematic**:

![schematic](readme-images/image.png)


And here is the **finished PCB** in the editor:

![pcb in editor](readme-images/image-1.png)


This is what the **final devboard** will look like:

![devboard front](readme-images/image-2.png)
![devboard back](readme-images/image-3.png)

## Bill of Materials (BOM)

| Item            | Description                  | Qty | Product Link | Price w/ Tax ($) | Running Total |
|-----------------|------------------------------|-----|--------------|------------------|---------------|
| Capacitor       | 1µF                          | 2   | https://jlcpcb.com/partdetail/53938-CL05A105KA5NQNC/C52923 | $0.03 | $0.03 |
| Capacitor       | 0.1µF                        | 11  | https://jlcpcb.com/partdetail/1877-CL05B104KO5NNNC/C1525   | $0.07 | $0.10 |
| Capacitor       | 10µF                         | 2   | https://jlcpcb.com/partdetail/2043-CL10A106MQ8NNNC/C1691   | $0.09 | $0.19 |
| Capacitor       | 33pF                         | 2   | https://jlcpcb.com/partdetail/1914-0402CG330J500NT/C1562   | $0.01 | $0.20 |
| Resistor        | 5.1kΩ                        | 2   | https://jlcpcb.com/partdetail/26648-0402WGF5101TCE/C25905  | $0.01 | $1.05 |
| Resistor        | 27Ω                          | 2   | https://jlcpcb.com/partdetail/25843-0402WGF270JTCE/C25100  | $0.01 | $1.06 |
| Resistor        | 330Ω                         | 1   | https://jlcpcb.com/partdetail/VikingTech-ARG02FTC3300/C284512 | $0.13 | $1.19 |
| Resistor        | 1kΩ                          | 2   | https://jlcpcb.com/partdetail/12256-0402WGF1001TCE/C11702  | $0.01 | $1.19 |
| Resistor        | 10kΩ                         | 1   | https://jlcpcb.com/partdetail/26487-0402WGF1002TCE/C25744  | $0.00 | $1.20 |
| SW Push         | Button                       | 1   | https://www.lcsc.com/product-detail/C720477.html           | $0.42 | $11.33 |
| WS2812B-2020    | RGB SMD LEDs                 | 5   | https://www.lcsc.com/product-detail/C965555.html           | —     | $1.04 |
| RP2040          | Microcontroller              | 1   | https://jlcpcb.com/partdetail/RaspberryPi-RP2040/C2040     | $4.58 | $5.78 |
| USB Receptacle  | USB-C (USB2.0, 14P)          | 1   | https://jlcpcb.com/partdetail/Korean_HropartsElec-TYPE_C_31_M12/C165948 | $0.85 | $1.04 |
| MCP1700x-330xxTT| Voltage Regulator            | 1   | https://jlcpcb.com/partdetail/MicrochipTech-MCP1700T_3302ETT/C39051 | $1.97 | $7.75 |
| W25Q16JVSS      | Firmware storage             | 1   | https://jlcpcb.com/partdetail/WinbondElec-W25Q16JVSSIQ/C82317 | $2.67 | $10.42 |
| Crystal         | Quartz resonator, 12 MHz     | 1   | https://jlcpcb.com/partdetail/YXC_CrystalOscillators-X322512MSB4SI/C9002 | $0.32 | $10.74 |
| Conn_01x03      | 1x03 Pin Header              | 1   | https://www.lcsc.com/product-detail/C42431804.html         | $0.00 | $10.74 |
| Conn_01x20      | 1x20 Pin Headers             | 2   | https://www.lcsc.com/product-detail/C42431804.html         | $0.17 | $10.91 |
| Onyx2040 PCBA   | Board assembly               | 1   | https://cart.jlcpcb.com/                                    | $43.94 | $54.85 |
