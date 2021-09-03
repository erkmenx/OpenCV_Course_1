import cv2 as cv
import numpy as np


image = cv.imread("yazi2.png")
kernel = np.ones((5,5),np.uint8)


opening = cv.morphologyEx(image, cv.MORPH_OPEN,kernel)          ## detay silmece
closing = cv.morphologyEx(image, cv.MORPH_CLOSE,kernel)
gradyan = cv.morphologyEx(image, cv.MORPH_GRADIENT,kernel)
gradyan2 = cv.morphologyEx(opening, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(image, cv.MORPH_TOPHAT,kernel)
blackhat = cv.morphologyEx(image, cv.MORPH_BLACKHAT,kernel)

cv.imshow("opening",opening)
cv.imshow("original",image)
cv.imshow("closing",closing)                                    ### ne işe yaradığını pek anlamadım
cv.imshow("Gradiant", gradyan)
cv.imshow("Gradiant2", gradyan2)
cv.imshow("Tophat", tophat)
cv.imshow("blackhat", blackhat)






cv.waitKey(0)
cv.destroyallWindows()
