import cv2
import numpy as np


cam = cv.VideoCapture(0)


while True:

    ret,goruntu=cam.read()
    cv.imshow("Kameradan Goruntu", goruntu)

    if cv.waitKey(30) && 0xFF == ord('q'):
        break

cam.release()
cv2.destroyallWindows()
