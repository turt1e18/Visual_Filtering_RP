import json
from tkinter import *

interface = Tk()
interface.title('get intensity from user')
interface.geometry("400x400")

def get_intensity_test(R, G, B) :
    R, G, B = red_slider.get(), green_slider.get(), blue_slider.get()
    print(f"R:{red_slider.get()}, G:{green_slider.get()}, B:{blue_slider.get()}")

red_slider = Scale(interface, from_ = 0, to=255, orient=HORIZONTAL)
green_slider = Scale(interface, from_ = 0, to=255, orient=HORIZONTAL)
blue_slider = Scale(interface, from_ = 0, to=255, orient=HORIZONTAL)

red_slider.pack()
green_slider.pack()
blue_slider.pack()

btn = Button(interface, text = '적용', command=get_intensity_test).pack()

interface.mainloop()