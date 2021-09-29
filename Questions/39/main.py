import cv2
img = cv2.imread('image.jpg')
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Input grayscale img', grayscale_img)

ret, threshold_img = cv2.threshold(grayscale_img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('Threshold img', threshold_img)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))

for i in range(9):
    erosion = cv2.erode(threshold_img, kernel, iterations=i)

    cv2.imshow('Dilated img', erosion)
    cv2.waitKey(1000)
