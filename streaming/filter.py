import numpy as np
import cv2


def make_filter(image, R, G, B) :
    height, width = image.shape[0], image.shape[1]

    red_filter = np.full((height, width, 3), (R, 0, 0), dtype=np.uint8)
    green_filter = np.full((height, width, 3), (0, G, 0), dtype=np.uint8)
    blue_filter = np.full((height, width, 3), (0, 0, B), dtype=np.uint8)

    filter = red_filter + green_filter + blue_filter
    return filter

def sample_image(image, filter) :
    blended = cv2.addWeighted(image, 0.8, filter, 0.2, 0)
    return blended
