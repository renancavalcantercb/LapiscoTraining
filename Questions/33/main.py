import cv2
import numpy as np
image = cv2.imread('image.png')

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny_image = cv2.Canny(grayscale_image, 80, 180)
contours, hierarchy = cv2.findContours(canny_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_poly = [None] * len(contours)
bound_rect = [None] * len(contours)

for i, contour in enumerate(contours):
    contours_poly[i] = cv2.approxPolyDP(contour, 2, True)
    bound_rect[i] = cv2.boundingRect(contours_poly[i])

contour_img = np.copy(image)

for i, contour in enumerate(contours_poly):
    cv2.rectangle(contour_img, (int(bound_rect[i][0]), int(bound_rect[i][1])),
                  (int(bound_rect[i][0]) + int(bound_rect[i][2]), int(bound_rect[i][1]) + bound_rect[i][3]),
                  (255, 0, 0), 2)
    crop = contour_img[int(bound_rect[i][1]):int(bound_rect[i][1]) + bound_rect[i][3],
                       int(bound_rect[i][0]):int(bound_rect[i][0]) + int(bound_rect[i][2])]

    cv2.imshow('Object ' + str(i + 1), crop)
    cv2.waitKey(10)

cv2.imshow('Input grayscale image', grayscale_image)
cv2.imshow('Contours', contour_img)
cv2.waitKey(0)
