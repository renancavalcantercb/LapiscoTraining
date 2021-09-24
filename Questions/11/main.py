import cv2
import numpy as np
img = cv2.imread('image.jpg')

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Input grayscale img', grayscale_img)

rows, cols = grayscale_img.shape[:2]
new_img = np.zeros((rows, cols), dtype=np.uint8)

for row in range(rows):
    for col in range(cols):
        new_img[row, col] = grayscale_img[row, col]

xc = 0
yc = 0
count = 0

for row in range(rows):
    for col in range(cols):
        if new_img[row, col] == 0:
            xc += row
            yc += col
            count += 1

xc = int(xc/count)
yc = int(yc/count)

cv2.circle(new_img, (xc, yc), 5, (255, 255, 255), -1)

cv2.imshow('Centroid', new_img)
cv2.waitKey(0)

cv2.imwrite('centroid.jpg', new_img)