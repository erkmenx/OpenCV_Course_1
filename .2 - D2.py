import cv2
import numpy as np



redresim = cv2.imread("manzara.jpeg")
greenresim = cv2.imread("manzara.jpeg")
blueresim = cv2.imread("manzara.jpeg")
redresim[:,:,2]=255
greenresim[:,:,1]=255
blueresim[:,:,0]=255


cv2.imshow("Manzara2",redresim)
cv2.imshow("Manzara3",greenresim)
cv2.imshow("Manzara4", blueresim)
cv2.waitKey(0)
cv2.destroyallWindows()
