import cv2
import numpy as np


resim = cv2.imread("manzara.jpeg")


resim[200:400,20:200,0]=255                                 #### Bölge belirleme

cv2.rectangle(resim,(200,400),(20,200),[0,0,255],3)         #### Belirli bir bölgeyi dikdörtgen içerisine alma

cv2.imshow("Resim",resim)



cv2.waitKey(0)
cv2.destroyallWindows()
