import cv2
import numpy as np



resim = cv2.imread("manzara.jpeg")


aynaresim = cv2.copyMakeBorder(resim,80,160,140,280,cv2.BORDER_REFLECT)         #### Yansıma (TOP,BOTTOM,LEFT,RIGHT, YANSIMA TÜRÜ)
uzatmaresim = cv2.copyMakeBorder(resim,20,200,20,20,cv2.BORDER_REPLICATE)       #### (TOP,BOTTOM,LEFT,RIGHT, YANSIMA TÜRÜ)
tekrar = cv2.copyMakeBorder(resim,400,400,400,400,cv2.BORDER_WRAP)
cerceveliresim = cv2.copyMakeBorder(resim,30,30,30,30,cv2.BORDER_CONSTANT,value=(100,100,255))

cv2.imshow("Aynalanmis Resim", aynaresim)
cv2.imshow("uzatilmis resim", uzatmaresim)
cv2.imshow("tekrarlanmis resim", tekrar)
cv2.imshow("cerceveli resim", cerceveliresim)



cv2.waitKey(0)
cv2.destroyallWindows()
