import cv2 as cv
import numpy as np



image = cv.imread("rainbow.jpg",0)              #### Siyah-beyaz yapma

ret,threshold=cv.threshold(image,127,255,cv.THRESH_BINARY)
ret,threshold2=cv.threshold(image,127,255,cv.THRESH_BINARY_INV)
ret,threshold3 = cv.threshold(image,127,255,cv.THRESH_TRUNC)
ret,threshold4 = cv.threshold(image,127,255,cv.THRESH_TOZERO)
ret,threshold5 = cv.threshold(image,127,255,cv.THRESH_TOZERO_INV)

cv.imshow("Image", image)
cv.imshow("Th binary", threshold)
cv.imshow("Th binary INV", threshold2)
cv.imshow("Th TRUNC", threshold3)
cv.imshow("Th TOZERO", threshold4)
cv.imshow("Th TOZERO INV", threshold5)




cv.waitKey(0)
cv.destroyallWindows()
