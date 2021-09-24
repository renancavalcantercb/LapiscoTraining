import cv2
import numpy as np
img = cv2.imread('image.jpg')

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Input grayscale img', grayscale_img)

rows, cols = grayscale_img.shape[:2]

output_img = np.zeros((rows, cols), np.uint8)

for row in range(1, rows-1):
    for col in range(1, cols-1):
        gx = grayscale_img[row - 1, col - 1] * (-1) + grayscale_img[row, col - 1] * (-2) + \
             grayscale_img[row + 1, col - 1] * (-1) + grayscale_img[row - 1, col + 1] + \
             grayscale_img[row, col + 1] * 2 + grayscale_img[row + 1, col + 1]

        gy = grayscale_img[row - 1, col - 1] * (-1) + grayscale_img[row - 1, col] * (-2) + \
             grayscale_img[row - 1, col + 1] * (-1) + grayscale_img[row + 1, col - 1] + \
             grayscale_img[row + 1, col] * 2 + grayscale_img[row - 1, col + 1]

        output_img[row, col] = (gx**2 + gy**2)**(1/2)

cv2.imshow('Sobel img', output_img)
cv2.waitKey(0)
cv2.imwrite('sobel_result.jpg', output_img)