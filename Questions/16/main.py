import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg')

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equalized_img = cv2.equalizeHist(grayscale_img)


original_hist = cv2.calcHist(grayscale_img, channels=[0], mask=None, histSize=[256], ranges=[0, 256])
equalized_hist = cv2.calcHist(equalized_img, channels=[0], mask=None, histSize=[256], ranges=[0, 256])



plt.figure(1)
plt.subplot(221)
plt.imshow(grayscale_img, cmap='gray')
plt.subplot(222)
plt.hist(grayscale_img.ravel(), 256, [0, 256])
plt.subplot(223)
plt.imshow(equalized_img, cmap='gray')
plt.subplot(224)
plt.hist(equalized_img.ravel(), 256, [0, 256])
plt.show()