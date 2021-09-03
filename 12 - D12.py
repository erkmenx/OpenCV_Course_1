import cv2 as cv
import numpy as np


yazi = cv.imread("yazi2.png")


kernel= np.ones((5,5),np.uint8)

normal_erosion = cv.erode(yazi,kernel,iterations=1)
dilation = cv.dilate(yazi,kernel,iterations=1)
erosion = cv.erode(dilation,kernel,iterations=1)
cv.imshow("Normal", yazi)
cv.imshow("Early Erosion", normal_erosion)
cv.imshow("Dilation", dilation)
cv.imshow("Normal3",erosion)









cv.waitKey(0)
cv.destroyallWindows()
