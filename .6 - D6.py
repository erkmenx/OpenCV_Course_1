import cv2
import numpy as np



resim1 = cv2.imread("manzara2.jpg")
resim2 = cv2.imread("manzara3.jpg")


toplam = cv2.add(resim1,resim2)

agirliklitoplam = cv2.addWeighted(resim1,0.7,resim2,0.3,0)
cv2.imshow("Resim",toplam)
cv2.imshow("Agirlikli toplam",agirliklitoplam)

cv2.waitKey(0)
cv2.destroyallWindows()
