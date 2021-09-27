import cv2

img = cv2.imread('image.jpg')
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresholded_img = cv2.adaptiveThreshold(grayscale_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)


cv2.imshow('Input grayscale img', grayscale_img)
cv2.imshow('Threshold result', thresholded_img)
cv2.waitKey(0)
