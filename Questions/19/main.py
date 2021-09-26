import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg')

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

Gx = cv2.Sobel(grayscale_img, dx=1, dy=0, ddepth=cv2.CV_64F, ksize=3)
Gy = cv2.Sobel(grayscale_img, dx=0, dy=1, ddepth=cv2.CV_64F, ksize=3)
sobel = (Gx**2 + Gy**2)**(1/2)
sobel = cv2.convertScaleAbs(sobel)


plt.figure(1)
plt.subplot(221)
plt.imshow(grayscale_img, cmap='gray')
plt.subplot(222)
plt.hist(grayscale_img.ravel(), 256, [0, 256])
plt.subplot(223)
plt.imshow(sobel, cmap='gray')
plt.subplot(224)
plt.hist(sobel.ravel(), 256, [0, 256])
plt.show()