# My name is Jacob Baker and this is Chapter 14 CPX 1 which I am doing on July 12

from adafruit_circuitplayground import cp
from notes_dict import notes
from colors import colors

def fill_pixels(color_tuple):
    cp.pixels.fill(color_tuple)
while True:
    if cp.touch_A1:
        cp.start_tone(notes["C4"])
        fill_pixels(colors["purple"])

    elif cp.touch_A3:
        cp.start_tone(notes["E4"])
        fill_pixels(colors["yellow"])
    elif cp.touch_A5:
        cp.start_tone(notes["B4"])
        fill_pixels(colors["cyan"])
    elif cp.touch_A6:
        cp.start_tone(notes["G4"])
        fill_pixels(colors["red"])

    else:
        cp.stop_tone()
        fill_pixels(colors["black"])


