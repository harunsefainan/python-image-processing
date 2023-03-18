import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread('image/lena.png')
KucukResim=cv2.pyrDown(resim)


cv2.imshow("Orijinal resim",resim)
cv2.imshow("Kucuk resim",KucukResim)

cv2.waitKey(0)
cv2.destroyAllWindows()