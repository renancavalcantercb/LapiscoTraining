import cv2

image = cv2.imread('image.jpg')

grayscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale Image', grayscale_img)
cv2.waitKey(0)

cv2.imwrite('grayscale_image.jpg', grayscale_img)