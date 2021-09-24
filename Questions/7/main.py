import cv2

img = cv2.imread('image.jpg')
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold_img = cv2.threshold(grayscale_img, 70, 255, cv2.THRESH_BINARY)
cv2.imshow('Input grayscale img', grayscale_img)
cv2.imshow('Threshold result', threshold_img)

cv2.waitKey(0)

cv2.imwrite('threshold_result.jpg', threshold_img)