import json

import cv2
import numpy as np

#get user customed color intensity
with open ("_COLOR.json", "r") as f :
    data = json.load(f)
RED, GREEN, BLUE = data[0]['intensity'], data[1]['intensity'], data[2]['intensity']

#get video
video = cv2.VideoCapture(0)

while(True):
    # [1] intensity에 따른 필터링
    # [2] 비디오 output
    break

video.release()
cv2.destroyAllWindows()