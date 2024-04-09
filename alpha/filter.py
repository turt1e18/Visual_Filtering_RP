import win32api
import win32con
import win32gui

from alpha.setting import decimal2RGB, RGB2decimal

# get display size
def get_display() :
    width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    return width, height

# apply RGB fillter
def apply_fillter(width=int, 
                  height=int,
                  r_intensity=int, 
                  g_intensity=int, 
                  b_intensity=int,) :

    for x in range(width) :
        for y in range(height) :

            # get pixel value
            current_color = win32gui.GetPixel(win32gui.GetDC(0), x, y,)
            red, green, blue = decimal2RGB(current_color)

            # change color based on RGB intensity
            red += r_intensity
            green += g_intensity
            blue += b_intensity
            new_color = RGB2decimal(red=red, green=green, blue=blue)
            
            # set pixel value
            win32gui.SetPixel(win32gui.GetDC(0), x, y, new_color,)