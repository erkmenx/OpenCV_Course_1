import cv2
import numpy as np




resim = cv2.imread("manzara2.jpg")

resimGri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

cv2.imshow("Orjinal",resim)

cv2.imshow("Siyah Beyaz", resimGri)

yukseklik,genislik,kanalSayisi = resim.shape

print("Orjinal", yukseklik,genislik,kanalSayisi)




## direkt siyah beyaz okuma satırı

resimdirectlygrey = cv2.imread("manzara2.jpg",0)

cv2.imshow("Direkt siyahbeyaz okuma", resimdirectlygrey)



cv2.waitKey(0)
cv2.destroyallWindows()
