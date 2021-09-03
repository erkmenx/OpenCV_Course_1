import cv2
import numpy as np




resim = cv2.imread("manzara.jpeg")
kesit = resim[200:400,200:400]  ###Kesit alma


resim[0:200,0:200]=kesit         #### Resmin içerisine kesiti yerleştirme


resim[200:300,200:300] = (25,98,105) #### Resmin içerisindeki belirli bir bölgeyi renk ile kaplama

cv2.imshow("Resim",resim)
cv2.waitKey(0)
cv2.destroyallWindows()
