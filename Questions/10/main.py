import cv2
import numpy as np
img = cv2.imread('image.jpg')

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Input grayscale img', grayscale_img)
cv2.waitKey(0)

rows, cols = grayscale_img.shape[:2]
threshold_matrix = np.zeros((rows, cols), dtype=np.uint8)

for row in range(rows):
    for col in range(cols):
        threshold_matrix[row, col] = grayscale_img[row, col]

with open('result.txt', 'w') as outfile:
    for row in range(rows):
        for col in range(cols):
            if threshold_matrix[row, col] < 127:
                threshold_matrix[row, col] = 0
            else:
                threshold_matrix[row, col] = 255

            outfile.write(str(threshold_matrix[row, col]) + ' ')
        outfile.write('\n')