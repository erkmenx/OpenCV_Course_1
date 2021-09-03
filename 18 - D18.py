import cv2 as cv
import numpy as np

# XXX:

image = cv.imread("galatatower2.jpg")
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(5,5),0)
blur=cv.pyrDown(blur)


canny = cv.Canny(blur,50,60)


def autoCanny(blur, sigma=0.33):
    median=np.median(blur)
    lower=int(max(0,(1.0-sigma)*median))
    upper = int(min(255,(1.0+sigma)*median))
    canny = cv.Canny(blur,lower,upper)

    return canny


wide = cv.Canny(blur,10,220)
tight = cv.Canny(blur,200,230)

auto = autoCanny(blur)

cv.imshow("Blurred image", blur)
cv.imshow("Edges", np.hstack([wide,tight,auto]))





cv.waitKey(0)
cv.destroyallWindows()
