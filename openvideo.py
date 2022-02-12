import cv2

video = cv2.VideoCapture("video/cartoon.mp4")

while True:
    success,img=video.read()
    cv2.imshow("cartoon",img)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        break