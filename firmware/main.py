# https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf
#  3.9.2. WS2812 LED (NeoPixel)

import array, time
from machine import Pin
import rp2

NUM_LEDS = 5

# assembly code for the PIO from micropy docs
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW,
             out_shiftdir=rp2.PIO.SHIFT_LEFT,
             autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

def pack_color(r, g, b):
    # (RED << 16) | (GREEN << 8) | BLUE
    return (r << 16) | (g << 8) | b

# StateMachine on GPIO25
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(25))
sm.active(1)

ar = array.array("I", [0 for _ in range(NUM_LEDS)])
CENTER, TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3, 4

for i in range(10):
    for led in [TOP, RIGHT, BOTTOM, LEFT]:
        for j in range(NUM_LEDS):
            ar[j] = 0
        
        ar[CENTER] = pack_color(8,8,8)

        ar[led] = pack_color(128,0,0)

        # sends data to LEDs
        for val in ar:
            sm.put(val)
        # sm.put(ar, 8)

        time.sleep_ms(200)

