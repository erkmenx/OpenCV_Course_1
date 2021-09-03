import cv2 as cv
import numpy as np



yazi = cv.imread("yazi2.png")

kernel = np.ones((5,5),np.uint8)


erosion = cv.erode(yazi,kernel,iterations=1)                                    ### Erozyon ayrıntıları silerken,dilation ayrıntıları arttırıyor. Böylece önce erozyon sonra dilation yaparak ayrıntılardan kurtulabiliriz.
dilation=cv.dilate(erosion,kernel,iterations=1)                             ### Küçük ayrıntıları sildik.
cv.imshow("dilation",dilation)


cv.waitKey(0)
cv.destroyallWindows()
