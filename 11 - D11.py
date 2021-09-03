import cv2 as cv
import numpy as np



resim = np.zeros((300,300,3),dtype='uint8')



cv.line(resim,(0,50),(300,50),(20,60,255),3)                ### (resim,pt1,pt2,renk,kalınlık) ###(yatay,dikey)
cv.line(resim,(0,250),(300,250),(20,60,255),3)
cv.circle(resim,(150,150),75,(255,0,0),5)
cv.putText(resim,"Python",(85,150),cv.FONT_HERSHEY_COMPLEX,1,(200,50,255))
cv.imshow("Line deneme",resim)


cv.waitKey(0)
cv.destroyallWindows()
