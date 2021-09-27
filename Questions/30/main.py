import cv2
import numpy as np
img = cv2.imread('image.png')

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny_img = cv2.Canny(grayscale_img, 80, 180)
contours, hierarchy = cv2.findContours(canny_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_img = np.copy(img)
cv2.drawContours(contour_img, contours, -1, (0, 0, 255), 3)

cv2.imshow('Input grayscale img', grayscale_img)
cv2.imshow('Contours', contour_img)
cv2.waitKey(0)
