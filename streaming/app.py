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
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: cnt receive")
            break
    
        filter = make_filter(frame, R, G, B)
        frame = sample_image(frame, filter)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

