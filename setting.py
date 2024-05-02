import json
import cv2
import numpy as np


with open ("_COLOR.json", "r") as f :
    data = json.load(f)
RED, GREEN, BLUE = data[0]['intensity'], data[1]['intensity'], data[2]['intensity']


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


if __name__ == '__main__':

    cap = cv2.VideoCapture('/dev/video0')

    if not cap.isOpened():
        print("CAN NOT OPEN")
        exit(0)


    while True:
        ret, frame = cap.read()
        if not ret:
            break

        red_filter = make_red_filter(frame)
        blue_filter = make_blue_filter(frame)
        green_filter = make_green_filter(frame)

        frame = sample_image(frame, red_filter, green_filter, blue_filter)

        cv2.imshow('caputure HDMI', frame)

        if cv2.waitKey(30) == ord('q'):
            break
    
    camera.release()
    cv2.destroyAllWindows()

