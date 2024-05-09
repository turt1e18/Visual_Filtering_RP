import json
import os
import cv2
import numpy as np
import pandas as pd

from streaming.filter import make_filter, sample_image

def main():
    path = os.getcwd()
    COLOR_path = os.path.join(path, "ui", "_COLOR.json")

    with open (COLOR_path, "r") as f :
        data = json.load(f)
    data = pd.DataFrame(data)
    INTENSITY = data['intensity']
    R, G, B = [255 * INTENSITY[0], 255* INTENSITY[1], 255* INTENSITY[2]]
    
    cap = cv2.VideoCapture("/dev/video0")
    
    if not cap.isOpened():
        print("Error: Couldn't open")
        exit()
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    print("width :", width, "height :", height)


    while True:
        start_t = cv2.getTickCount()

        ret, frame = cap.read()
        if not ret:
            print("Error: can't receive")
            break

        frame = cv2.flip(frame, 0)

        filter = make_filter(frame, R, G, B)
        frame = sample_image(frame, filter)

        cv2.imshow('test', frame)

        time_diff = (cv2.getTickCount() - start_t) / cv2.getTickFrequency()
        fps = 1.0 / time_diff
        print(f"FPS :{fps:.2f}")

        if cv2.waitKey(1) & 0xFF == ord('q') :
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

