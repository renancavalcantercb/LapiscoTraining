import cv2

image = cv2.imread('image.jpg')

cv2.imshow('Image', image)
cv2.waitKey(0)

cv2.imwrite('saved_image.jpg', image)