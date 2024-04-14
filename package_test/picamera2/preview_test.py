from picamera2 import Picamera2, Preview
import time
import cv2


picam2 = Picamera2()
config = picam2.create_preview_configuration()
picam2.configure(config)
picam2.start()

while True:
    frame = picam2.capture_array()
    cv2.imshow('Preview', frame)

    if cv2.waitKey(1) == ord('q'):
        break

picam2.stop_preview()
cv2.destroyAllWindows()

