import cv2
import numpy as np

filename = 'result_question10.txt'
img = []
with open(filename, 'r') as infile:
    for i, line in enumerate(infile):
        row = [int(number) for number in line.split()]
        if i == 0:
            img = np.hstack(row)
        else:
            img = np.vstack(([img, row]))

result = np.asarray(img, np.uint8)

cv2.imshow('Read img', result)
cv2.waitKey(0)