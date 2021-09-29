import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg')
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Input grayscale img', grayscale_img)

ret, threshold_img = cv2.threshold(grayscale_img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('Threshold img', threshold_img)

structuring_elements = [cv2.MORPH_RECT, cv2.MORPH_ELLIPSE, cv2.MORPH_CROSS]

plt.figure(1)
titles = ['Rectangle element', 'Elliptic element', 'Cross element']
for i, element in enumerate(structuring_elements):
    kernel = cv2.getStructuringElement(element, (5, 5))
    erosion = cv2.erode(threshold_img, kernel, iterations=7)
    fig = 130 + (i+1)
    plt.subplot(fig)
    plt.title(titles[i])
    plt.imshow(erosion, cmap='gray')

plt.show()
cv2.waitKey(0)
