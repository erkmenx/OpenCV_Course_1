import cv2 as cv
import numpy as np


cam = cv.VideoCapture(0)

width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

fourcc = cv.VideoWriter_fourcc(*'XVID')
writer = cv.VideoWriter("kayit.avi",fourcc,20,(width,height))
while True:
    ref,frame = cam.read()
    writer.write(frame)
    cv.imsohw("Kayot Videosu",frame)
    if cv.waitKey(25) & 0xFF == ord('q'):
        break


cam.release()
cv.destroyallWindows()
