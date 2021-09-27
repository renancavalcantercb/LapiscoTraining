import cv2
import numpy as np
img = cv2.imread('image.png')

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(grayscale_img, cv2.HOUGH_GRADIENT, 1, 30,
                           param1=150, param2=25, minRadius=0, maxRadius=0)

try:
    circles = np.uint16(np.around(circles))
except AttributeError:
    print('None circles found! Try change the parameters.')
    exit()


circles_img = np.copy(img)

for xc, yc, radius in circles[0, :]:
    cv2.circle(circles_img, (xc, yc), radius, (0, 0, 255), 2)

cv2.imshow('Input grayscale img', grayscale_img)
cv2.imshow('Threshold result', circles_img)
cv2.waitKey(0)
