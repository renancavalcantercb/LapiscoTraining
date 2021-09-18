import cv2

img = cv2.imread('image.jpg')

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny_img = cv2.Canny(grayscale_img, 80, 180)

cv2.imshow('Input grayscale img', grayscale_img)

cv2.imshow('Canny filter result', canny_img)
cv2.waitKey(0)

cv2.imwrite('canny_filter_result.jpg', canny_img)