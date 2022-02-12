import cv2

cam = cv2.VideoCapture(0)
while True:
    success,img= cam.read()
    cv2.imshow("camera",img)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        break

