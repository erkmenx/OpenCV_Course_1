import cv2 as cv
import numpy as np



resim1 = cv.imread("resim1.png")
resim2 = cv.imread("resim2.png")


bit_And = cv.bitwise_and(resim1,resim2)
bit_Or = cv.bitwise_or(resim1,resim2)
bit_XOR = cv.bitwise_xor(resim1,resim2)
bit_XOR_NOT = cv.bitwise_not(bit_XOR)
cv.imshow("AND",bit_And)
cv.imshow("OR",bit_Or)
cv.imshow("XOR",bit_XOR)
cv.imshow("XOR_NOT",bit_XOR_NOT)





cv.waitKey(0)
cv.destroyallWindows()
