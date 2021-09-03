import cv2
import numpy as np



resim = cv2.imread("kucukmanzara.png")
buyukresim = cv2.pyrUp(resim)         ### İki kat büyütme
kucukresim = cv2.pyrDown(resim)

cv2.imshow("Orjinal resim", resim)
cv2.imshow("Iki kat büyük resim", buyukresim)
cv2.imshow("Iki kat kucuk resim", kucukresim)

cv2.waitKey(0)
cv2.destroyallWindows()
