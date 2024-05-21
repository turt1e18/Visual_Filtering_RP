import numpy as np
import cv2


def make_filter(height, width, R, G, B):
    red_filter = np.full((height, width, 3), (B, 0, 0), dtype=np.uint8)
    green_filter = np.full((height, width, 3), (0, G, 0), dtype=np.uint8)
    blue_filter = np.full((height, width, 3), (0, 0, R), dtype=np.uint8)

    filter = red_filter + green_filter + blue_filter
    return filter


def sample_image(image, filter):
    if np.all(filter == 0):
        return image
    else:
        blended = cv2.addWeighted(image, 0.8, filter, 0.2, 0)
        return blended
