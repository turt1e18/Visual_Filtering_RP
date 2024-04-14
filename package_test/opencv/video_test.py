import cv2

camera = cv2.VideoCapture('/dev/video0')


if not camera.isOpened():
    print("camera not opened\n")

while True:
    ret, frame = camera.read()
    if not ret:
        print(ret)
        break

    cv2.imshow("test", frame)

    if cv2.waitKey(30) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
