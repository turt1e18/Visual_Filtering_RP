from filter import get_display, apply_fillter
import time
import json

WIDTH, HEIGHT = get_display()

# with open ("_INTENSITY.json", "r") as f :
#     data = json.load(f)

# RGB intensity
INTENSITY = [0,0,0]

# print("start")

apply_fillter(width = WIDTH,
              height = HEIGHT,
              r_intensity = INTENSITY[0],
              g_intensity = INTENSITY[1],
              b_intensity = INTENSITY[2])

# print("finish")