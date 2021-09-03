import cv2 as cv
import numpy as np


image = cv.imread("rabbitcarrot.jpg",0)
imagedown = cv.pyrDown(image)
cv.imshow("Original", imagedown)
imagedown = cv.blur(imagedown,(3,3))
cv.imshow("Blurred", imagedown)
#simple thresholding
ret,threshold = cv.threshold(imagedown,110,255,cv.THRESH_BINARY)

#adaptive thresholding
threshold2 = cv.adaptiveThreshold(imagedown,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)

threshold3 = cv.adaptiveThreshold(imagedown,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
cv.imshow("Rabbit & Carrot", threshold)
cv.imshow("Adaptive Threshold", threshold2)
cv.imshow("AdaptiveGaussian", threshold3)




cv.waitKey(0)
cv.destroyallWindows()
