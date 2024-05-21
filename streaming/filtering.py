import numpy as np
import cv2


def make_filter(height, width, R, G, B):
    blue_filter = np.full((height, width, 3), (B, 0, 0), dtype=np.uint8)
    green_filter = np.full((height, width, 3), (0, G, 0), dtype=np.uint8)
    red_filter = np.full((height, width, 3), (0, 0, R), dtype=np.uint8)

    filt = blue_filter + green_filter + red_filter
    return filt


def sample_image(image, filt):
    if np.all(filt == 0):
        return image
    else:
        blended = cv2.addWeighted(image, 0.8, filt, 0.2, 0)
        return blended
