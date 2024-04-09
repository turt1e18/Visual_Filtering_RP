import json

import cv2
import numpy as np

image = cv2.imread('image\image.png')

with open ("_COLOR.json", "r") as f :
    data = json.load(f)
RED, GREEN, BLUE = data[0]['intensity'], data[1]['intensity'], data[2]['intensity']


################################## [case 1] ##################################

# def make_filter(image, R, G, B) :
#     height, width = image.shape[0], image.shape[1]

#     red_fillter = np.full((height, width, 3), (R, 0, 0), dtype=np.uint8)
#     green_fillter = np.full((height, width, 3), (0, G, 0), dtype=np.uint8)
#     blue_fillter = np.full((height, width, 3), (0, 0, B), dtype=np.uint8)

#     filter = red_fillter + green_fillter + blue_fillter
#     return filter

# def sample_image(image, filter) :
#     blended = cv2.addWeighted(image, 0.7, filter, 0.3, 0)
#     return blended

# R, G, B = [255, 255, 255]

# image = cv2.imread('image\image.png')
# filter = make_filter(image, R, G, B)

# result = sample_image(image, filter)
# cv2.imshow('test',result)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

################################## [case 1] ##################################


################################## [case 2] ##################################

def make_red_filter(image) :
    img = image.copy()
    img[:, :, 0] = 0
    img[:, :, 1] = 0
    return img

def make_green_filter(image) :
    img = image.copy()
    img[:, :, 0] = 0
    img[:, :, 2] = 0
    return img

def make_blue_filter(image) :
    img = image.copy()
    img[:, :, 1] = 0
    img[:, :, 2] = 0
    return img

def sample_image(image, red_filter, green_filter, blue_filter) :
    weight = [0.1, -0.002, 0.0]
    blended = image*(1-sum(weight)) + red_filter*(weight[0])    \
                                    + green_filter*(weight[1])  \
                                    + blue_filter*(weight[2])
    blended = blended.astype(np.uint8)
    return blended

red_filter = make_red_filter(image)
blue_filter = make_blue_filter(image)
green_filter = make_green_filter(image)

sample_image = sample_image(image, red_filter, green_filter, blue_filter)

cv2.imshow('', sample_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

################################## [case 2] ##################################